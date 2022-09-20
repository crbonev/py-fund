types = input()
value = input()


def data_type(operator, mod):
    if operator == 'int':
        return int(mod) * 2
    elif operator == 'real':
        return f'{float(mod) * 1.5:.2f}'
    elif operator == 'string':
        return f'${str(mod)}$'


print(data_type(types, value))