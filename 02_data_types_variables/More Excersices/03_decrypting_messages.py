key = int(input())
lines = int(input())
current_line = 0
lines_ord = []
letter_ord = 0

while current_line < lines:
    current_line += 1
    letter = input()
    letter_ord = ord(letter)
    letter_ord += key
    letter = chr(letter_ord)
    lines_ord.append(letter)


print(''.join(lines_ord))

