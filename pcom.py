from socket import *
import threading
from logger import *
import time

class TargetDisconnected(Exception):
    pass

class Pcom:

    tcp_client:socket
    receiver_thread:threading.Thread
    reply_string:str
    reply_string_fixed:str
    logger:Logger
    target_address:str
    target_port:int

    def __init__(self,address:str ,port:int,logger:Logger=None):
        """Pcomオブジェクトの生成

        Args:
            address (str): 接続先のIPアドレス
            port (int): 接続先のポート番号
        """
        if logger == None:
            self.logger = Logger()
        else:
            self.logger = logger

        self.tcp_client = socket(AF_INET,SOCK_STREAM)
        self.tcp_client.connect((address,port))

        self.reply_string = ""
        
        self.target_address = address
        self.target_port = port

        self.receiver_thread = threading.Thread(target=self.receiver)
        self.receiver_thread.setDaemon(True)
        self.receiver_thread.start()
        pass

    def send_and_receive(self,cmd:str):
        """コマンドの送受信

        Args:
            cmd (str): 送信する文字列（CRは自動で付加される）

        Returns:
            str: 応答文字列
        """
        self.reply_string_fixed = ""
        cmd = cmd + "\r"
        self.logger.SendMessage(cmd)
        self.tcp_client.send(bytes(cmd,encoding="ascii"))

        while self.reply_string_fixed == "":
            time.sleep(0.01)

        self.logger.ReceiveMessage(self.reply_string_fixed)
        return self.reply_string_fixed
        pass

    def receiver(self) -> str:
        """受信スレッド
        """
        while True:
            try:
                receive_byte = self.tcp_client.recv(1)
                receive_str = receive_byte.decode("ascii")
                pass
            except Exception as exc:
                self.logger.Message("TCP/IP has disconnected. Try to connect again.")
                raise TargetDisconnected("\x1b[31mLost the link with the RC-53x\x1b[37m")

            if receive_str == '\r':
                # 確定
                self.reply_string_fixed = self.reply_string
                self.reply_string = ""
            else:
                self.reply_string = self.reply_string + receive_str


