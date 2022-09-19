passs = input()


def is_pass_valid(password):
    is_len = False
    is_allnum = False
    is_2num = False
    count = 0

    if 6 <= len(password) <= 10:
        is_len = True
    else:
        print('Password must be between 6 and 10 characters')

    if password.isalnum() is False and '_!"' not in password:
        print('Password must consist only of letters and digits')
    else:
        is_allnum = True

    for x in password:
        if x in '1234567890':
            count += 1
    if count < 2:
        print("Password must have at least 2 digits")
    else:
        is_2num = True

    if is_len and is_allnum and is_2num is True:
        return 'Password is valid'
    else:
        return exit()


print(is_pass_valid(passs))
