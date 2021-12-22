# token encrypter

- トークン暗号化スクリプト
- [fernet](https://github.com/fernet/spec/blob/master/Spec.md) 方式を採用しています。

## 初期設定

1. python3 をインストール
1. `$ python3 -m pip install -U cryptography`

### pipenv(仮想環境)を使う場合

1. python3 -m pip install pipenv
1. `$ pipenv install`
1. 以降 `$ python3 ...` を `$ pipenv run python ...` に置き換えて実行

## キー生成

`$ python3 generate_key.py`

実行すると暗号化/復号用のキーが出力されます。
環境変数 `CIPHER_KEY` に保存してください。

## トークン暗号化

`$ python3 encrypt.py 生トークン`

実行すると指定したトークンが暗号化されて出力されます。

## 暗号化トークンの復号

`$ python3 decrypt.py 暗号化トークン`

実行すると指定した暗号化トークンが復号されて出力されます。
