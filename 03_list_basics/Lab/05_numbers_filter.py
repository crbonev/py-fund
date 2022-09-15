total_lines = int(input())
positive = []
negative = []
even = []
odd = []

for lines in range(total_lines):
    number = int(input())
    if number >= 0:
        positive.append(number)
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    elif number < 0:
        negative.append(number)
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
command = input()
if command == 'even':
    print(even)
if command == 'odd':
    print(odd)
if command == 'negative':
    print(negative)
if command == 'positive':
    print(positive)