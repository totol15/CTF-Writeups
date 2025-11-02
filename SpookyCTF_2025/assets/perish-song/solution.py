cipher = ["F", "C#", "A#", "G#", "A#", "C#", "E#", "C", "F", "F#", "E", "C", "A", "C", "F", "A#", "F", "G#", "C#", "G#", "G", "F#", "G#", "G", "G#", "E#", "G", "D", "A#", "D#", "C", "F#"]
c = [4, 6, 11, 10, 11, 6, 8, 0, 4, 9, 3, 0, 1, 0, 4, 11, 4, 10, 6, 10, 5, 9, 10, 5, 10, 8, 5, 2, 11, 7, 0, 9]

a = pow(-5, -1, 12)
b = (9 - 4 * a) % 12
assert (4 * a + b) % 12 == 9
assert (9 * a + b) % 12 == 8

a_inv = pow(a, -1, 12)

def match(a):
    if a == 0:
        return "C"
    elif a == 1:
        return "A"
    elif a == 2:
        return "D"
    elif a == 3:
        return "E"
    elif a == 4:
        return "F"
    elif a == 5:
        return "G"
    elif a == 6:
        return "C#"
    elif a == 7:
        return "D#"
    elif a == 8:
        return "E#"
    elif a == 9:
        return "F#"
    elif a == 10:
        return "G#"
    elif a == 11:
        return "A#"
    else:
        print("fail")
        return ""

flag = "NICC{"
for i in c:
    flag = flag + match((a_inv * (i - b)) % 12)
flag = flag + "}"
print(flag)
