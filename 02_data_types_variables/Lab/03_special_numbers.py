number = int(input())
for a in range(1, number + 1):
    sum = 0
    for digit in str(a):
        sum += int(digit)
    if sum == 5 or sum == 7 or sum == 11:
        print(f'{a} -> True')
    else:
        print(f'{a} -> False')