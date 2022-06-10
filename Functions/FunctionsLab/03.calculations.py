def operations(operator, num_one, num_two):
    result = None
    if operator == "multiply":
        result = num_one*num_two
    elif operator == "divide":
        result = num_one//num_two
    elif operator == "add":
        result = num_one+num_two
    elif operator == "subtract":
        result = num_one-num_two
    return  result

operation = input()
first_num = int(input())
second_num = int(input())

print(operations(operation,first_num,second_num))