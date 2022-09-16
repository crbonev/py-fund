word = input()


def vowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [string[i] for i in range(len(string)) if string[i].lower() not in vowels]
    return ''.join(result)


print(vowel(word))

# vowels = ['a', 'e', 'i', 'o', 'u']
# result = [ch for ch in word if ch.lower() not in vowels]
# print(''.join(result))

# [x**2 | for x in num | if x > 0]
# [output|   var  input | optional]

#
# result = [x for x in range(0, 15) if x % 2 == 0 and x != 0]
# print(result)
#
# numbers = [1, 2, 3, 4, 5]
# filtered = [True if x % 2 == 0 else False for x in numbers]
# print(filtered)

# matrix = [[x for x in range(1, 3)] for y in range(3)]
# print(matrix)
