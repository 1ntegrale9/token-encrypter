from cryptography.fernet import Fernet
from os import getenv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('encrypted_token')
encrypted_token = parser.parse_args().encrypted_token

key = getenv('CIPHER_KEY')
raw_token = Fernet(key).decrypt(encrypted_token.encode('utf-8')).decode('utf-8')
print(raw_token)
