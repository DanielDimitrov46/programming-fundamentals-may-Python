number_of_letters = int(input())
word=''
for i in range(97,97+number_of_letters):
    for m in range(97,97+number_of_letters):
        for n in range(97,97+number_of_letters):
            print(chr(i)+chr(m)+chr(n))