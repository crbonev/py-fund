number = int(input())


def sequence(n):
    final = []
    if n == 1:
        seq = [1]
    elif n == 2:
        seq = [1, 1]
    else:
        seq = [1, 1, 2]
        for n in range(3, n):
            num = seq[- 1] + seq[- 2] + seq[- 3]
            seq.append(num)
    for x in seq:
        final += str(x) + ' '
    return final


print(''.join(sequence(number)))