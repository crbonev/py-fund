key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
other = {}
obtained = False
current = ''
while not obtained:
    data = input().split()
    material = []
    quantity = []
    for index, item in enumerate(data):
        if index % 2 == 0:
            quantity.append(int(item))
        else:
            material.append(item.lower())

    for index, item in enumerate(material):
        if item in key_materials:
            key_materials[item] += quantity[index]

            if key_materials[item] >= 250:
                key_materials[item] -= 250
                obtained = True
                current = item
                break
        else:
            if item not in other:
                other[item] = quantity[index]
            else:
                other[item] += quantity[index]

if current == 'shards':
    print('Shadowmourne obtained!')
elif current == 'fragments':
    print('Valanyr obtained!')
elif current == 'motes':
    print('Dragonwrath obtained!')

for material, value in key_materials.items():
    print(f'{material}: {value}')

for material1, value1 in other.items():
    print(f'{material1}: {value1}')
