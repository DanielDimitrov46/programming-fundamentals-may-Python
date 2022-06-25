20 lines (17 sloc)  654 Bytes

def sorted_func(greter_numbers_than_sum):
    top_five_numbers = []

    for num in sorted(greter_numbers_than_sum)[::-1]:
        if len(top_five_numbers)<5:
            top_five_numbers.append(num)
        else:
            break
    return ' '.join([str(num) for num in top_five_numbers])
def number_func(numbers):
    average_number = sum(sequence)/len(sequence)
    greater_numbers_than_average_sum = [num for num in numbers if num>average_number]

    if greater_numbers_than_average_sum:
        print(sorted_func(greater_numbers_than_average_sum))
    else:
        print("No")

sequence = [int(x) for x in input().split()]
number_func(sequence)