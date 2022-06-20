numbers_list = [int(x) for x in input().split(", ")]
founded_numbers = []

for index,element in enumerate(numbers_list):
    if element%2==0:
        founded_numbers.append(index)

print(founded_numbers)