n = int(input())
ll_positive = []
ll_negative = []
for _ in range(0,n):
    number = int(input())
    if number<0:
        ll_negative.append(number)
    else:
        ll_positive.append(number)

print(ll_positive)
print(ll_negative)
print(f"Count of positives: {len(ll_positive)}")
print(f"Sum of negatives: {sum(ll_negative)}")