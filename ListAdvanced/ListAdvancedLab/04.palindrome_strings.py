words = input().split(" ")
palindrome = input()
all_palindromes = []

for element in words:
    if element == "".join(reversed(element)):
        all_palindromes.append(element)
print(f"{all_palindromes}")
print(f"Found palindrome {all_palindromes.count(palindrome)} times")