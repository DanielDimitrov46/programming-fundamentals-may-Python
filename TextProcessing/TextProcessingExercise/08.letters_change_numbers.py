sequence_of_strings = input().split()
total_sum = 0
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]

for current_problem in sequence_of_strings:
    number = ""
    for current_symbol in current_problem:
        if current_symbol.isdigit():
            number += current_symbol
        continue
    for index in range(len(current_problem)):
        number = int(number)
        position = 0
        to_lower=""
        if not current_problem[index].isdigit() and index == 0:
            to_lower = current_problem[index].lower()
            position = alphabet.index(to_lower)
            position+=1
            if current_problem[index].isupper():
                total_sum += number / position
            else:
                total_sum+= number*position
        elif not current_problem[index].isdigit() and index != 0:
            to_lower = current_problem[index].lower()
            position = alphabet.index(to_lower)
            position += 1
            if current_problem[index].isupper():
                total_sum-=position
            else:
                total_sum+=position
print(f"{total_sum:.2f}")
