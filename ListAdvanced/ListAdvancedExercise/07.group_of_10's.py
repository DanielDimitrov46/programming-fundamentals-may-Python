number_list = [int(x) for x in input().split(", ")]

for n in range(1, 11):
    check_list = []
    if len(number_list) != 0:
        [check_list.append(i) for i in number_list if i <= (n * 10)]
        [number_list.remove(o) for o in check_list]
        print((f"Group of {n * 10}'s: {check_list}"))
