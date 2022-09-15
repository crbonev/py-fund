number_of_lines = int(input())
total_lines = 0

added = 0
capacity = 255
while total_lines < number_of_lines:
    add = int(input())
    if added + add > capacity:
        print('Insufficient capacity!')
        added -= add
    added += add
    total_lines += 1
print(added)
