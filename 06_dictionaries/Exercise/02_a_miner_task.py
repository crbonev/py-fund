my_string = input()
current_line = 1
last = ''
commodities = {}
while my_string != 'stop':
    if current_line % 2 != 0:
        last = my_string
        if my_string not in commodities.keys():
            commodities[my_string] = 0
    else:
        if last in commodities.keys():
            commodities[last] += int(my_string)
    current_line += 1
    my_string = input()
for key, value in commodities.items():
    print(f'{key} -> {value}')
