n = int(input())
numbers = []
final_list = []
EVEN_COMMAND = "even"
ODD_COMMAND = "odd"
NEGATIVE_COMMAND = "negative"
POSITIVE_COMMAND = "positive"
for i in range (0,n):
    number = int(input())
    numbers.append(number)
command = input()

for element in numbers:
    filter_command = (
        (command==EVEN_COMMAND and element%2==0) or
        (command==ODD_COMMAND and element%2!=0) or
        (command==NEGATIVE_COMMAND and element<0) or
        (command==POSITIVE_COMMAND and element>=0)
    )
    if filter_command:
        final_list.append(element)
print(final_list)
