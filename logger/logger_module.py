import time
import datetime
import sys

class Logger:

    tx_rx_msg_suppression:bool

    def __init__(self) -> None:
        self.tx_rx_msg_suppression = False
        pass

    def suppress_communication_logs(self, switch:bool):
        """通信ログの抑制のON/OFFスイッチ

        Args:
            switch (bool): True=抑制、False=抑制しない
        """
        self.tx_rx_msg_suppression = switch

    def Message(self, message_text:str):
        """メッセージログの出力

        Args:
            message_text (str): 出力するメッセージ
        """
        current_time = time.localtime()
        print(
            str(datetime.datetime.now()) +
            "[MSG ]" +  
            message_text,
            file=sys.stderr)

    def ErrorMessage(self, message_text:str):
        """メッセージログの出力

        Args:
            message_text (str): 出力するメッセージ
        """
        current_time = time.localtime()
        print(
            "\x1b[31m" + str(datetime.datetime.now()) +
            "[ERR ]" +  
            message_text + "\x1b[37m",
            file=sys.stderr)
    
    def SendMessage(self,message_text:str):
        """送信メッセージの出力

        Args:
            message_text (str): 出力するメッセージ
        """
        if self.tx_rx_msg_suppression == True:
            return

        current_time = time.localtime()
        print(
            str(datetime.datetime.now()) +
            "[SEND]" +  
            message_text,
            file=sys.stderr)

    def ReceiveMessage(self,message_text:str):
        """受信メッセージの出力

        Args:
            message_text (str): 出力するメッセージ
        """
        if self.tx_rx_msg_suppression == True:
            return

        current_time = time.localtime()
        print(
            str(datetime.datetime.now()) +
            "[RECV]" +  
            message_text,
            file=sys.stderr)
