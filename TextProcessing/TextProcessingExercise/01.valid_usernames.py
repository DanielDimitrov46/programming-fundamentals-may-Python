# def valid_length(username):
#     if 3 <= len(username) <= 16:
#         return True
#     return False
#
#
# def valid_symbols(username):
#     for character in username:
#         if not (character.isalnum() or character == "-" or character == "_"):
#             return False
#         return True
#
#
# def valid_no_redundant(username):
#     if " " in username:
#         return False
#     return True
#
#
# def username_is_valid(username):
#     if valid_length(username) and valid_symbols(username) and valid_no_redundant(username):
#         return True
#     return False
#
#
# usernames = input().split(", ")
# for username in usernames:
#     if username_is_valid(username):
#         print(username)

usernames = input().split(", ")
for username in usernames:
    username_is_valid = True
    if not 3 <= len(username) <= 16:
        username_is_valid = False
    for character in username:
        if not (character.isalnum() or character == "-" or character == "_"):
            username_is_valid = False
    if ' ' in username:
        username_is_valid = False
    if username_is_valid:  # if username_is_valid == True
        print(username)
