text = input()
new = ''
explosion = 0
for index in range(explosion, len(text)):
    if explosion > 0 and text[index] != '>':
        explosion -= 1
    elif text[index] == '>':
        explosion += int(text[index + 1])
        new += text[index]
    else:
        new += text[index]

print(new)








# for index, char in enumerate(data):
#     if char != '>':
#         new += char
#     else:
#         explosion = data[index]







    # if char == '>':
    #     explosion = int(data[index + 1])
    #     ch = data[index:(index+explosion):]
    #     print(ch)