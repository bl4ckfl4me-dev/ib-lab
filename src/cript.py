from cipher.adfgvx import decrypt, encrypt
import os


def encode_access_token(data: tuple) -> str:
    return encrypt('000'.join([str(i) for i in data]), os.getenv('SECRET_KEY'))


def decode_access_token(token: str) -> dict:
    d = decrypt(token, os.getenv('SECRET_KEY'))
    decrypted = [i.lower() for i in d.split('000')]
    return {
        'id': decrypted[0],
        'name': decrypted[1],
    }
