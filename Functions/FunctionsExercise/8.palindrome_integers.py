def check_palindrome(list_of_numbers):
    for n in list_of_numbers:
        if n == n[::-1]:
            print("True")
        else:
            print("False")

numbers = input().split(", ")
check_palindrome(numbers)