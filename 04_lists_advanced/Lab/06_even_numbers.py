numbers = list(map(int, input().split(', ')))
even = [num for num in range(len(numbers)) if numbers[num] % 2 == 0]
# even = [x for x in range(len(numbers)) if x % 2 == 0]


print(even)

# new_numbers = list(map(lambda x: x*2, numbers))
# new_numbers2 = list(filter(lambda x: x % 2 == 0, numbers))
# print(new_numbers)
# print(new_numbers2)
#
# print(list(map(lambda x: x * 2, [1, 2, 3, 4, 5])))
