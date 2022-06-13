even_sum = []
odd_sum = []
def sum_of_even_and_odd_number(single_string):
    for digit in single_string:
        real_digit = int(digit)
        if real_digit%2==0:
            even_sum.append(real_digit)
        else:
            odd_sum.append(real_digit)
    return f"Odd sum = {sum(odd_sum)}, Even sum = {sum(even_sum)}"

string = input()
print(sum_of_even_and_odd_number(string))