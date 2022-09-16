tasks = []
while True:
    command = input().split('-')
    if command[0] == 'End':
        break
    importance = int(command[0])
    task = command[1]
    tasks.append((importance, task))

sorted_tasks = [task_data[1] for task_data in sorted(tasks)]
print(sorted_tasks)
