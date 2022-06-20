def positive_filter(number):
    return [x for x in number if int(x)>=0]
def negative_filter(number):
    return [x for x in number if int(x)<0]
def even_filter(number):
    return [x for x in number if int(x)%2==0]
def odd_filter(number):
    return [x for x in number if int(x)%2!=0]

numbers = input().split(", ")
print(f"Positive: {', '.join(positive_filter(numbers))}")
print(f"Negative: {', '.join(negative_filter(numbers))}")
print(f"Even: {', '.join(even_filter(numbers))}")
print(f"Odd: {', '.join(odd_filter(numbers))}")
