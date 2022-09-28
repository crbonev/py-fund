def new_string(text):
    new = ''
    for index, ch in enumerate(text):
        if index == 0:
            new += ch
        else:
            if text[index - 1] != ch:
                new += ch
    return new


text = input()
print(new_string(text))
