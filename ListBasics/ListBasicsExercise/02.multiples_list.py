# factor = int(input())
# count = int(input())
# ll = []
# num=factor
# for index in range(0,count):
#     ll.append(num)
#     num+=factor
# print(ll)

factor = int(input())
count = int(input())
list_of_numbers = []
for multiplier in range(1,count+1):
    list_of_numbers.append(factor*multiplier)
print(list_of_numbers)