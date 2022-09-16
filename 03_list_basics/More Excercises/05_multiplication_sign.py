one = int(input())
two = int(input())
three = int(input())


def sign(a, b, c):

    count_negative = 0

    if a < 0:
        count_negative += 1
    if b < 0:
        count_negative += 1
    if c < 0:
        count_negative += 1

    if count_negative % 2 == 0:
        return 'positive'
    else:
        return 'negative'


print(sign(one, two, three))
