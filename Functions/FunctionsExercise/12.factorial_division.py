def factorial_division(first_number):
    for factoriel in range(1,first_number):
        first_number *= factoriel
    return first_number

first_number = int(input())
second_number = int(input())

first_number_factorial = factorial_division(first_number)
second_number_factorial = factorial_division(second_number)
result = first_number_factorial / second_number_factorial
print(f"{result:.2f}")
