my_string = input().split()
letters = {}
for word in my_string:
    for letter in word:
        letters[letter] = 0
for word in my_string:
    for letter in word:
        if letter in letters:
            letters[letter] += 1
for key, value in letters.items():
    print(f'{key} -> {value}')
