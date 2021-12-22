from cryptography.fernet import Fernet
from os import getenv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('raw_token')
raw_token = parser.parse_args().raw_token

key = getenv('CIPHER_KEY')
encrypted_token = Fernet(key).encrypt(raw_token.encode('utf-8')).decode('utf-8')
print(encrypted_token)
