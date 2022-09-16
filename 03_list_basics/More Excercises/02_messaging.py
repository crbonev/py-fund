numbers_list = input().split(' ')
message = input()
message_list = []

for number in numbers_list:
    current = 0
    for i in number:
        i = int(i)
        current += i

    current %= len(message)

    message_list.append(message[current])
    message = message.replace(message[current], '', 1)

print(''.join(message_list))


