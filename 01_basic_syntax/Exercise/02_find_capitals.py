string = input()
letters = []
index = -1
current_index = 0
letter_index = []
for digit in string:
    letters.append(digit)
    index += 1
    if digit.isupper():
        current_index = index
        letter_index.append(current_index)

print(''.join(str(letter_index)))