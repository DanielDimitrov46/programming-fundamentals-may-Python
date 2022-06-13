list_of_chars = []
def sequance_of_two_characters(a,b):
    for digit in range(ord(a)+1,ord(b)):
        list_of_chars.append(chr(digit))
    return list_of_chars

first_char = input()
second_char = input()
result = sequance_of_two_characters(first_char,second_char)
print(" ".join(result))