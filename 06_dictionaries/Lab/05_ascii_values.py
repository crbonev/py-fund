val = {}
chars = input().split(', ')
for ch in chars:
    val[ch] = ord(ch)
print(val)