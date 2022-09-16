wagons = int(input()) * [0]

while True:
    command = input()

    if command == 'End':
        break

    data = command.split(' ')
    cmd = data[0]
    if cmd == 'add':
        people_to_add = int(data[1])
        wagons[-1] += people_to_add

    elif cmd == 'insert':
        index = int(data[1])
        people_to_add = int(data[2])
        wagons[index] += people_to_add

    elif cmd == 'leave':
        index = int(data[1])
        people_to_add = int(data[2])
        wagons[index] -= people_to_add

print(wagons)
