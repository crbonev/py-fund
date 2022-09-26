text = input()
digit = ''
letter = ''
others = ''
for ch in text:
    if ch.isdigit():
        digit += ch
    elif ch.isalpha():
        letter += ch
    else:
        others += ch

print(digit)
print(letter)
print(others)