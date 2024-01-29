# pcom tcp 通信クラス (python)

簡単便利にtcp送受信ができるように、tcp通信クラスを作成。

## 使い方
以下の例のように、Pcomオブジェクトを生成してポートを開き、send_textメソッドで文字列を送るだけです。
応答があれば戻り値として応答（受信文字列）が返されます。

応答がない（通信線が断線など）の場合は、約3秒待っても応答が無ければ ”ERROR” を返します。

```python
from pscom import *
log = Logger()
# log.suppress_communication_logs(True)
pcom = Pcom("172.20.9.15",5000,log)
ans = pcom.send_and_receive("TEXT_COMMAND")
```
### logger について
Pcomクラスは送受信ログを標準エラー出力に出力します。
そのため、PcomクラスはLoggerクラスのインスタンスを必要としますが、
外部で生成したインスタンスを引数で渡した場合はそのインスタンスが使われ、
引数で渡さない場合は Pcom クラスのコンストラクタで自動的に生成します。

**引数で渡す例**
```python
pcom = Pcom("172.20.9.15",5000,log)
```
**引数で渡さない例**
```python
pcom = Pcom("172.20.9.15",5000)
```

### 通信ログのON/OFF
Pcomクラスはデフォルトで通信ログを表示しますが、不要な場合は非表示に設定できます。
これは、suppress_commnication_logsで設定します。

```python
log.suppress_communication_logs(True)
```
|値|  意味|
|--|--|
|True|    表示しない|
|False|   表示する（初期値）|


## 実行
プログラムが main.py だとしたとき、実行は以下の通り。

**Windows**
```bash
python main.py
```

**Mac, Linux**
```bash
python3 main.py
```

## 受信スレッド
このプログラムは受信のためにスレッドを使っています。

スレッドは通信先への接続が完了した時点からプログラムの終了まで存在し続けます。
プログラムが終了するとスレッドも終了します。

## インストール
あなたのプロジェクト（フォルダ）の中に、pcomフォルダと logger フォルダを**マルっとコピー**してください。

## その他
ファイルの構成は以下の通りです。

|ファイル    |内容|
|--|--|
|./main.py| サンプルプログラム|
|./README.md| 説明ファイル（このファイル）|
|./logger/logger_module.py| loggerクラス本体|
|./logger/\_\_init\_\_.py| モジュールの初期化|
|./pcom\pcom_module.py| pcomクラス本体|
|./pcom/\_\_init\_\_.py| モジュールの初期化|

正直、pythonのスレッドが遅い？のか、あんまり動作は速くないです。
experiment1 ブランチを追加 (24.1.29)