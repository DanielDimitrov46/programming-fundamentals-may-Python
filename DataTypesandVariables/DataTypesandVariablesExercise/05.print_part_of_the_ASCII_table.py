start_index = int(input())
end_index = int(input())
final_string = ''

for character in range(start_index, end_index + 1):
    final_string += chr(character) + chr(32)
    print(chr(character), end = " ")
