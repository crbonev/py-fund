char_one = input()
char_two = input()


def chars_in_range(one, two):
    char1 = ord(one)
    char2 = ord(two)
    chars = []
    final_string = ''
    for x in range(char1 + 1, char2):
        chars.append(chr(x))
    for i in chars:
        final_string += ' ' + i
    return final_string


print(chars_in_range(char_one, char_two))

#
# def chars_in_range(first, second):
#     char1 = ord(first)
#     char2 = ord(second)
#     chars = []
#
#     for x in range(char1, char2 + 1):
#         chars.append(chr(x))
#
#     print(chars)

