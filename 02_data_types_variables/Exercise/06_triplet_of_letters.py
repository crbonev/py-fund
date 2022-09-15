number = int(input())
for first in range(0, number):
    for second in range(0, number):
        for third in range(0, number):
            print(f'{chr(97 + first)}{chr(97 + second)}{chr(97 + third)}')