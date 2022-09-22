def register(users, commands):
    name = commands[1]
    number = commands[2]
    if users.get(name) == number:
        return f'ERROR: already registered with plate number {number}'
    else:
        users[name] = number
    return f"{name} registered {number} successfully"


def unregister(users, commands):
    name = commands[1]
    if name in users:
        del users[name]
        return f'{name} unregistered successfully'
    else:
        return f'ERROR: user {name} not found'


number_of_commands = int(input())
users = {}


while number_of_commands:
    commands = input().split()
    command = commands[0]
    number_of_commands -= 1
    if command == 'register':
        print(register(users, commands))
    elif command == 'unregister':
        print(unregister(users, commands))

for key, value in users.items():
    print(f"{key} => {value}")