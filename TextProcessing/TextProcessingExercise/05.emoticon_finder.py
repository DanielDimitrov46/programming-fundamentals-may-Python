text = input()
# emoticons = []
# counter = 0
# for char in text:
#     if char ==":":
#         emoticons.append()
# counter+=1
# print(emoticons)

for index, letter in enumerate(text):
    if ":"==letter:
        print(f"{letter}{text[index+1]}")