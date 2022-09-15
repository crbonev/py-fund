number = int(input())
number = str(number)
listed = []
listed2 = []
for digit in number:
    digit = int(digit)
    listed.append(digit)
listed.sort()
listed.reverse()
for digit in listed:
    digit = str(digit)
    listed2.append(digit)
print(''.join(listed2))