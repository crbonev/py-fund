sequence_1 = input().split(', ')
sequence_2 = input().split(', ')
sequence_3 = [word for word in sequence_1 for index in range(len(sequence_2)) if word in sequence_2[index]]

sequence_3 = list(dict.fromkeys(sequence_3))
print(sequence_3)


#
# sequence_1 = input().split(', ')
# sequence_2 = input().split(', ')
# sequence_3 = []
#
# for x in sequence_1:
#     for index in range(len(sequence_2)):
#         if x in sequence_2[index]:
#             sequence_3.append(x)
# sequence_3 = list(dict.fromkeys(sequence_3))
# print(sequence_3)
#
#
