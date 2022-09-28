data = input()
crypt = ''
for ch in data:
    new_ch = chr(ord(ch) + 3)
    crypt += new_ch
print(crypt)