sequence = input().split(', ')


def palindrome(numbers):
    forward = ''
    backward = ''
    for num in numbers:
        forward = num
        backward = num[::-1]
        if forward == backward:
            print(True)
        else:
            print(False)
    exit()


print(palindrome(sequence))

