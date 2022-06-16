def validation_six_to_ten_characters(password):
    if 6<=len(password)<=10:
        return True
    print("Password must be between 6 and 10 characters")
def validation_only_letters_and_digits(password):
    if password.isalnum():
        return True
    print("Password must consist only of letters and digits")
    return False
def validation_at_least_two_digits(password):
    digits_counter = 0
    for digit in password:
        if digit.isdigit():
            digits_counter+=1
    if digits_counter>=2:
        return True
    print("Password must have at least 2 digits")
    return False

password_validation = input()
validated = [validation_six_to_ten_characters(password_validation),validation_only_letters_and_digits(password_validation),validation_at_least_two_digits(password_validation)]
if all(validated):
    print("Password is valid")