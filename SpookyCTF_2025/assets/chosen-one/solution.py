from pwn import *

p = remote("45.55.60.238", 1337)

flag = ""
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ{}!@#$%^&*()_:/;?.,=+-"
total = 64 #128 hex characters, so 64 bytes/64 characters
done = False

for i in range(total):
    if done == True:
        break
    current = i + 1
    found = False
    
    for j in alphabet:
        if found == True:
            break
        c = j.encode().hex()
        p_real = "00"*(total - current)
        p_fake = "00"*(total - current) + flag.encode().hex() + c

        p.recvuntil(b"Enter p (hexadecimal):")
        p.sendline(p_real.encode())
        output_real = p.recvline(timeout=2, keepends=False).strip().decode()[:128]

        p.recvuntil(b"Enter p (hexadecimal):")
        p.sendline(p_fake.encode())
        output_fake = p.recvline(timeout=2, keepends=False).strip().decode()[:128]

        for one in range(16):
            if found == True:
                    break
            for two in range(16):
                if found == True:
                    break
                final1 = ""
                final2 = ""
                for l in output_fake:
                    a = (int(l, 16) - one) % 16
                    a = f"{a:x}"
                    final1 += a
                for l in final1:
                    c = (int(l, 16) + two) % 16
                    c = f"{c:x}"
                    final2 += c

                if output_real == final2:
                    flag = flag + j
                    if j == "}":
                        done = True
                    found = True

p.close()
print(flag)
