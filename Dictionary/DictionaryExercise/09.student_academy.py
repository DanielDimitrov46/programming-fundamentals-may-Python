information_dict = {}
next_pairs = int(input())

for _ in range(0,next_pairs):
    name = input()
    grade = float(input())
    if name not in information_dict:
        information_dict[name] = []
    information_dict[name].append(grade)
for name,value in information_dict.items():
    information_dict[name] = sum(value)/len(value)
    if information_dict[name]>=4.50:
        print(f"{name} -> {information_dict[name]:.2f}")