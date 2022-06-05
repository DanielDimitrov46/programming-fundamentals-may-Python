n = int(input())
filter_word = input()
texts_list = []
for _ in range(0,n):
    strings = input()
    texts_list.append(strings)
print(texts_list)
for i in range(len(texts_list)-1,-1,-1):
    element = texts_list[i]
    if filter_word not in element:
        texts_list.remove(element)
print(texts_list)