n = int(input())
flag = False

for _ in range(0,n):
    word = input()
    if ","in word or "." in word or "_" in word:
        print(f"{word} is not pure!")
        continue
    print(f"{word} is pure.")