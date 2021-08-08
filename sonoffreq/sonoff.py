from Crypto.Cipher import AES
from Crypto.Hash import MD5
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from base64 import b64encode
import json
import requests
import time

class Sonoff:
    def __init__(self, addr, api_key):
        self.addr = addr
        self.api_key = api_key
        pass

    def switch(self, state):
        hash = MD5.new()
        hash.update(bytes(self.api_key, 'utf-8'))
        key = hash.digest()
        iv = get_random_bytes(16)

        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        padded = pad(bytes(json.dumps({'switch': state}), 'utf-8'), AES.block_size)
        ciphertext = cipher.encrypt(padded)

        requests.post(
            f'http://{self.addr}:8081/zeroconf/switch',
            headers={
                'Content-Type': 'application/json;charset=UTF-8',
                'Accept': 'application/json',
            },
            data=json.dumps({
                'sequence': str(int(time.time() * 1000)),
                'deviceid': None,
                'selfApikey': '123',
                'iv': b64encode(iv).decode('utf-8'),
                'encrypt': True,
                'data': b64encode(ciphertext).decode('utf-8'),
            })
        )
