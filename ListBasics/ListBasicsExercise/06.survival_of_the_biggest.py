numbers_strrings = input().split()
n = int(input())
numbers_ints = []
min_number = 0
moment =""


for element in numbers_strrings:
    numbers_ints.append(int(element))

for i in range(n):
    num = min(numbers_ints)
    numbers_ints.remove(num)
print(", ".join(str(x) for x in numbers_ints))
