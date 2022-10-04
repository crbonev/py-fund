import re

sentence = input()
search_for = input()
pattern = fr'\b{search_for}\b'
matches = re.findall(pattern, sentence, flags=re.IGNORECASE)
print(len(matches))
