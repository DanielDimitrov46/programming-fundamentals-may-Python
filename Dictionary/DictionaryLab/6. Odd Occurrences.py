words = input().split(" ")

final_dict = {}

for word in words:
    word = word.lower()
    if word not in final_dict:
        final_dict[word] = 0
    final_dict[word]+=1

for key,value in final_dict.items():
    if value%2!=0:
        print(key, end= " ")