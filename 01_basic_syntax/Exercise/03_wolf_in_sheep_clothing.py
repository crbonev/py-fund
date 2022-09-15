# string = input().split(', ')
# listed = string
# list_items = len(listed)
#
# for index in (range(list_items)):
#
#     if listed[index] == 'wolf' and index == list_items - 1:
#
#         print('Please go away and stop eating my sheep')
#
#     elif listed[index] == 'wolf' and index < list_items:
#         print(f'Oi! Sheep number {list_items - 1}! You are about to be eaten by a wolf!')
#
# animals = input()
# animals_list = animals.split(', ')
# animals_list.reverse()
# for index, animal in enumerate(animals_list):
#     if animal == 'wolf' and index == 0:
#         print('Please go away and stop eating my sheep')
#     elif animal == 'wolf':
#         print(f'Oi! Sheep number {index}! You are about to be eaten by a wolf!')


string_list = input().split(', ')
string_list.reverse()

for index, string in enumerate(string_list):
    if string == 'wolf' and index == 0:
        print('Please go away and stop eating my sheep')
    elif string == 'wolf':
        print(f'Oi! Sheep number {index}! You are about to be eaten by a wolf!')