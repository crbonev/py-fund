text = input()
for index, ch in enumerate(text):
    emoji = ''
    if ch == ':':
        emoji += ch
        emoji += text[index + 1]
        print(emoji)