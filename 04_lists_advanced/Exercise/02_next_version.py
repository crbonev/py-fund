# current_version = list(map(int, input().split('.')))
# n1 = current_version[0]
# n2 = current_version[1]
# n3 = current_version[2]
# next_version = []
# n3 += 1
#
# if n3 > 9:
#     n2 += 1
#     n3 = 0
# if n2 > 9:
#     n1 += 1
#     n2 = 0
#
# print(f'{n1}.{n2}.{n3}')

data = input().split('.')
data = int(''.join(data)) + 1
result = [str(number) for number in str(data)]

print('.'.join(result))
# data = input().split('.')
#
#
# def next_version(version):
#     version = int(''.join(version)) + 1
#     result = [str(number) for number in str(version)]
#     return '.'.join(result)
#
#
# print(next_version(data))
