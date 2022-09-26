# usernames = input().split(', ')
# valid_users = []
# for username in usernames:
#     username_isvalid = True
#     if not 3 <= len(username) <= 16:
#         username_isvalid = False
#     for character in username:
#         if not (character.isalnum() or character == '-' or character == '_'):
#             username_isvalid = False
#     if ' ' in username:
#         username_isvalid = False
#     if username_isvalid:
#         print(username)

def len_is_valid(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def characters_are_valid(username):
    for character in username:
        if character.isalnum():
            return True
        return False


def is_char_under(username):
    for character in username:
        if character == '-' or character == '_':
            return False
    return True


def no_redundant_symbols(username):
    if ' ' in username:
        return False
    return True


usernames = input().split(', ')
for username1 in usernames:
    if characters_are_valid(username1) and no_redundant_symbols(username1) and len_is_valid(username1) and is_char_under(username1):
        print(username1)