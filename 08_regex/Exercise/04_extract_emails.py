import re

pattern = r'(?<=\s)([a-z0-9]+[\._\-a-z0-9]*)@[a-z\-]+(\.[a-z]+)+\b'

text = input()
matches = re.finditer(pattern, text)
for w in matches:
    print(w.group())
