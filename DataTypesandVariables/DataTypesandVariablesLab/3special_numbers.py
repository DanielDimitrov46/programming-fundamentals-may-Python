n = int(input())
for i in range(1,n+1):
    num=0
    for m in str(i):
        num +=int(m)
    if num==5 or num==7 or num==11:
            print(f"{i} -> True")
    else:
            print(f"{i} -> False")