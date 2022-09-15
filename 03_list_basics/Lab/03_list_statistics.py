total_lines = int(input())
list_positive = []
list_negative = []
lines = 0
while lines < total_lines:
    lines += 1
    number = int(input())
    if number >= 0:
        list_positive.append(number)
    else:
        list_negative.append(number)
print(list_positive)
print(list_negative)
print(f"Count of positives: {len(list_positive)}")
print(f"Sum of negatives: {sum(list_negative)}")
