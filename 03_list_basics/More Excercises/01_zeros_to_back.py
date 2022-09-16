numbers = input().split(', ')
count = 0
numbers_final = []
while '0' in numbers:
    numbers.remove('0')
    count += 1
for i in range(count):
    numbers.append('0')
for digit in numbers:
    digit = int(digit)
    numbers_final.append(digit)
print(numbers_final)