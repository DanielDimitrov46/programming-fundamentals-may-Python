def reversed_func(data):
    for string in data:
        print(f"{string} = {string[::-1]}")

words = []

while True:
    word = input()
    if word == "end":
        break
    print(f"{word} = {word[::-1]}")



#
# word = input()
#
# while word != "end":
#     pass
