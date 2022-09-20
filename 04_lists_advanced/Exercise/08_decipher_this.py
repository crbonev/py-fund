# •	the second and the last letter are switched (e.g., Holle means Hello)
# •	the first letter is replaced by its character code (e.g., 72 means H)

#
# message = input().split()
# first = message[0]
# seconds = message[1]
# third = message[2]
# final = ''
# for x in message:
#
#     letter = chr(int(x[:2:]))
#     scnd = x[-1]
#     last = x[2]
#     final = letter + scnd + x[3:-1] + last
#
#     print(final)

# message = input().split()
# first = message[0]
# second = message[1]
# third = message[2]
# asci = int(''.join(x for x in first if x.isdigit()))
# letter = chr(asci)
# final = letter
# print(final)

#
messages = input().split()
word1 = ''
for message in messages:
    number = ''
    letters = ''
    for character in message:
        if character.isalpha():
            letters += character
        if character.isdigit():
            number += character
    number = int(number)
    if len(letters) >= 2:
        word1 += chr(number) + letters[-1] + letters[1:-1] + letters[0] + ' '
    else:
        word1 += chr(number) + letters[-1] + letters[1:-1] + ' '
print(word1)













