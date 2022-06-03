word = input()
while word !="End":
    if word =="SoftUni":
        word = input()
        continue
    for i in word:
        chr=""
        chr += i
        print(chr*2, end="")
    print()
    word = input()