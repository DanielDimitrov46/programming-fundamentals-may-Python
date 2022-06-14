# numbers_as_digits = [int(s) for s in input().split()]
# is_even = lambda x: x%2==0
# result = list(filter(is_even,numbers_as_digits))
# print(result)
def check_even(number):
    if int(number) % 2 == 0:
        return True
    return False

filtered_numbers = []
sequence_of_numbers = input().split()
for current_num in sequence_of_numbers:
    if check_even(current_num):
        filtered_numbers.append(int(current_num))
print(filtered_numbers)