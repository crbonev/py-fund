import re
sentence = input()
pattern = r'\b_([A-Za-z]+)'
matches = re.findall(pattern, sentence)
print(','.join(matches))
