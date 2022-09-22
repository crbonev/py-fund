courses = {}
while True:
    command = input()
    if command == 'end':
        break
    command = command.split(' : ')
    course = command[0]
    name = command[1]
    if course not in courses:
        courses[course] = [name]
    else:
        courses[course].append(name)

for course, names in courses.items():
    print(f'{course}: {len(names)}')
    for name in names:
        print(f'-- {name}')