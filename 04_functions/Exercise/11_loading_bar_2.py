num = int(input())


def load_bar(numbers):
    bars = 0
    for x in range(numbers):
        if x % 10 == 0:
            bars += 1
    if bars == 1:
        print(f'{numbers}% [%.........]')
        return f'Still loading...'
    elif bars == 2:
        print(f'{numbers}% [%%........]')
        return f'Still loading...'
    elif bars == 3:
        print(f'{numbers}% [%%%.......]')
        return f'Still loading...'
    elif bars == 4:
        print(f'{numbers}% [%%%%......]')
        return f'Still loading...'
    elif bars == 5:
        print(f'{numbers}% [%%%%%.....]')
        return f'Still loading...'
    elif bars == 6:
        print(f'{numbers}% [%%%%%%....]')
        return f'Still loading...'
    elif bars == 7:
        print(f'{numbers}% [%%%%%%%...]')
        return f'Still loading...'
    elif bars == 8:
        print(f'{numbers}% [%%%%%%%%..]')
        return f'Still loading...'
    elif bars == 9:
        print(f'{numbers}% [%%%%%%%%%.]')
        return f'Still loading...'
    elif bars == 10:
        print(f'{numbers}% Complete!')
        return f'[%%%%%%%%%%]'
    else:
        print(f'{numbers}% [..........]')
        return 'Still loading...'


print(load_bar(num))

