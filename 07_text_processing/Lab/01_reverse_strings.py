while True:
    word = input()
    if word == 'end':
        break
    text_reversed = ''
    for character in reversed(word):
        text_reversed += character
    print(word + ' = ' + text_reversed)
