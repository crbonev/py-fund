import re

pattern = r'(\+[3][5][9](\s|\-)2\2[0-9]{3}\2[0-9]{4}\b)'
phone = input()
matches = re.findall(pattern, phone)
phones = []
for x in matches:
    phones.append(x[0])
print(', '.join(phones))