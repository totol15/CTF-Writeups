from pwn import *
import ssl

host = "cube-cipher.challs.pwnoh.io"
port = 1337

p = remote(host, port, ssl=True, sni=host)

p.recvuntil(b"Option:")
p.sendline(b"3")
original = p.recvline().strip().decode()

cur = ""
prev = ""

while True:
    p.recvuntil(b"Option:")
    p.sendline(b"4")
    p.recvuntil(b"Option:")
    p.sendline(b"3")
    cur = p.recvline().strip().decode()
    if cur == original:
        break
    prev = cur

print(bytes.fromhex(prev).decode())

p.close()
