material = []
value = []
dictionary = {'shards': 0, 'fragments': 0, 'motes': 0}
obtained = False

while not obtained:
    data = input().split()

    for index, thing in enumerate(data):
        if index % 2 == 0:
            value.append(int(thing))
        else:
            material.append(thing.lower())

    for i, m in enumerate(material):
        if m not in dictionary:
            dictionary[m] = value[i]
        else:
            dictionary[m] += value[i]
        if dictionary['shards'] >= 250:
            print('Shadowmourne obtained!')
            dictionary['shards'] -= 250
            obtained = True
            break
        elif dictionary['fragments'] >= 250:
            print('Valanyr obtained!')
            dictionary['fragments'] -= 250
            obtained = True
            break
        elif dictionary['motes'] >= 250:
            print('Dragonwrath obtained!')
            dictionary['motes'] -= 250
            obtained = True
            break
for i, x in dictionary.items():
    print(f'{i}: {x}')
#
#
# """
# 123 silver 6 shards 8 shards 5 motes 9 fangs 75 motes 103 MOTES 8 Shards 86 Motes 7 stones 19 silver
#
# Dragonwrath obtained!
# shards: 22
# fragments: 0
# motes: 19
# silver: 123
# fangs: 9


#
#
# 3 Motes 5 stones 5 Shards 6 leathers 255 fragments 7 Shards
# """