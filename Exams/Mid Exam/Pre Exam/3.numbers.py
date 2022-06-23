sequence = [int(x) for x in input().split()]
above_average_list = []
reversed_list = []
average_number = sum(sequence)/len(sequence)

for number in sequence:
    if number>average_number:
        above_average_list.append(number)
above_average_list.sort()
reversed_list = above_average_list.reverse()
print(above_average_list)