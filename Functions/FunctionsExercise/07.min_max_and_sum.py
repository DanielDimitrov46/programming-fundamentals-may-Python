def min_number(numbers):
    min_number_of_all = min(numbers)
    return min_number_of_all

def max_number(numbers):
    max_number_of_all = max(numbers)
    return max_number_of_all

def sum_of_all_number(numbers):
    sum_number_of_all = sum(numbers)
    return sum_number_of_all

list_of_numbers = [int(x) for x in input().split()]

print(f'The minimum number is {min_number(list_of_numbers)}\nThe maximum number is {max_number(list_of_numbers)}\nThe sum number is: {sum_of_all_number(list_of_numbers)}')