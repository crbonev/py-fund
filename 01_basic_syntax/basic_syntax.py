# # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
# 1. Number definer
#
#
# number = float(input())
# if number == 0:
#     print('zero')
# elif number > 0:
#     if number < 1:
#         print('small positive')
#     elif number > 100000:
#         print('large positive')
#     else:
#         print('positive')
# elif number < 0:
#     if number > -1:
#         print('small negative')
#     elif number < -100000:
#         print('large negative')
#     else:
#         print('negative')
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
# 2. Largest of three numbers
#
#
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# if num1 > num2 and num1 > num3:
#     print(num1)
# elif num2 > num1 and num2 > num3:
#     print(num2)
# elif num3 > num2 and num3 > num1:
#     print(num3)
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
# 3. Word reverse
#
#
# word = input()
# rev_word = ''
# for i in range(len(word) -1, -1, -1):
#     rev_word += word[i]
# print(rev_word)
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
# 4. Even or odd
#
#
# n = int(input())
# for i in range(n):
#     num = int(input())
#     if not num % 2 == 0:
#         print(f"{num} is odd!")
#         break
# else:
#     print('All numbers are even.')
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
# 5. Number between 1-100
#
#
# num = float(input())
# while num < 1 or num > 100:
#     num = float(input())
# else:
#     print(f'The number {num} is between 1 and 100')
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
# 6. Shopping
#
#
# budget = int(input())
# command = input()
# while command != 'End':
#     price = int(command)
#     budget -= price
#     if budget < 0:
#         print('You went in overdraft!')
#         break
#     command = input()
# else:
#     print('You bought everything needed.')
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
# 7. Pattern
#
#
# number_of_stars = int(input())
# for i in range(1, number_of_stars + 1):
#     print(i * '*')
# for n in range(number_of_stars - 1, 0, -1):
#     print(n * '*')
#
#
# # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                 #
#                                                 #
#                   POST LECTURE                  #
#                                                 #
#                                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # #
#
#
# import random
#
#
# questions1 = open("questions.txt", "r")
# content = questions1.read()
# content_list = content.split("\n")
# questions1.close()
# print(random.choice(content_list))
