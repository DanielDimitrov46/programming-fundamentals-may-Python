def sorted_numbers(sequence):
    result = sorted(sequence)
    return result
sequence_of_numbers = [int(x) for x in input().split()]
print(sorted_numbers(sequence_of_numbers))