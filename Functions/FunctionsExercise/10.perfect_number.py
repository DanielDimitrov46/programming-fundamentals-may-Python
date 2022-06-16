def perfect_number(number):
    sum = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            sum += divisor
    if number == sum:
        print("We have a perfect number!")
        return True
    print("It's not so perfect.")

number_perfect = int(input())
perfect_number(number_perfect)
