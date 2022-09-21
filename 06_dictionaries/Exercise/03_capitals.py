countries = input().split(', ')
capitals = input().split(', ')
dictionary = {countries[index]: capitals[index] for index in range(0, len(countries))}
for key, value in dictionary.items():
    print(f'{key} -> {value}')
