numbers = list(map(int, input().split()))
sum_value = 0
while numbers:
    index = int(input())
    removed_elem = 0

    if index < 0:
        removed_elem = numbers[0]
        numbers[0] = numbers[-1]

    elif index >= len(numbers):
        removed_elem = numbers[-1]
        numbers[-1] = numbers[0]

    else:
        # removed_elem = numbers[index]
        removed_elem = numbers.pop(index)
    sum_value += removed_elem
    for i in range(len(numbers)):
        if numbers[i] <= removed_elem:
            numbers[i] += removed_elem
        else:
            numbers[i] -= removed_elem

print(sum_value)
