from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import random

N = 16
key = get_random_bytes(N)
flag = 'NICC{placeholder_flag}'
cipher = AES.new(key, AES.MODE_ECB)

def e1(p):
    p = bytes.fromhex(p)
    one = pad(p + flag.encode(), 16)

    try:
        enc = cipher.encrypt(one)
    except:
        return "Error"

    enc = enc.hex()

    two = random.randint(0, 15)
    txt = ""

    for i in enc:
        c = (int(i, 16) + two) % 16
        c = f"{c:x}"
        txt += c

    return {"C": txt}
