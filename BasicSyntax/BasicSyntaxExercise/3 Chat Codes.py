n = int(input())

for _ in range(0,n):
    num = int(input())
    if num==88:
        print("Hello")
    elif num==86:
        print("How are you?")
    elif not (num==88 and num ==86)and num<88:
        print("GREAT!")
    else:
        print("Bye.")