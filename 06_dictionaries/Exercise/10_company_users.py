companies = {}
while True:
    command = input()
    if command == 'End':
        break
    command = command.split(' -> ')
    company = command[0]
    employee_id = command[1]

    if company not in companies:
        companies[company] = [employee_id]

    if employee_id not in companies[company]:
        companies[company].append(employee_id)


for company, users in companies.items():
    print(f'{company}')
    for user in users:
        print(f'-- {user}')
