import re

pattern = r'>>(\w+)<<(\d+\.?\d+)!(\d+)'
total = 0
data = input()
items = []
while data != 'Purchase':
    result = re.findall(pattern, data)
    for item in result:
        items.append(item)

    data = input()

print('Bought furniture:')
for item in items:
    furniture = item[0]
    price = float(item[1])
    count = int(item[2])
    total += price * count
    print(furniture)
print(f'Total money spend: {total:.2f}')