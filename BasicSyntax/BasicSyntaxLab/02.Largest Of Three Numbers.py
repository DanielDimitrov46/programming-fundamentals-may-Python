first = int(input())
second = int(input())
third = int(input())

max=0
if first>second and first>third:
    max=first
elif second>third and second>first:
    max=second
else:
    max=third

print(max)