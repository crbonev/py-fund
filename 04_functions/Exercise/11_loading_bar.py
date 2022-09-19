num = int(input())


def loading_bar(numbers):
    if numbers < 10:
        print(f'{numbers}% [..........]')
        return f'Still loading...'
    elif 10 > numbers <= 19:
        print(f'{numbers}% [%.........]')
        return f'Still loading...'
    elif 20 <= numbers <= 29:
        print(f'{numbers}% [%%........]')
        return f'Still loading...'
    elif 30 <= numbers <= 39:
        print(f'{numbers}% [%%%.......]')
        return f'Still loading...'
    elif 40 <= numbers <= 49:
        print(f'{numbers}% [%%%%......]')
        return f'Still loading...'
    elif 50 <= numbers <= 59:
        print(f'{numbers}% [%%%%%.....]')
        return f'Still loading...'
    elif 60 <= numbers <= 69:
        print(f'{numbers}% [%%%%%%....]')
        return f'Still loading...'
    elif 70 <= numbers <= 79:
        print(f'{numbers}% [%%%%%%%...]')
        return f'Still loading...'
    elif 80 <= numbers <= 89:
        print(f'{numbers}% [%%%%%%%%..]')
        return f'Still loading...'
    elif 90 <= numbers <= 99:
        print(f'{numbers}% [%%%%%%%%%.]')
        return f'Still loading...'
    elif numbers == 100:
        print(f'{numbers}% Complete!')
        return '[%%%%%%%%%%]'
    else:
        return exit()


print(loading_bar(num))
