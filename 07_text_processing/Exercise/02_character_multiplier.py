# print(ord('a'))

data = input().split()
first = data[0]
second = data[1]
total = 0

if len(first) == len(second):
    for ind, ch in enumerate(first):
        total += ord(ch) * ord(second[ind])

elif len(first) > len(second):
    total_len = len(first) - len(second)
    for ind, ch in enumerate(second):
        total += ord(ch) * ord(first[ind])
    for i in range(0, total_len):
        total += ord(first[::-1][i])

elif len(second) > len(first):
    total_len = len(second) - len(first)
    for ind, ch in enumerate(first):
        total += ord(ch) * ord(second[ind])
    for i in range(0, total_len):
        total += ord(second[::-1][i])

print(total)