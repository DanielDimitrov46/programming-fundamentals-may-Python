percent_input = int(input())

def check_loading_bar(percent_number):
    if percent_number==100:
        return "100% Complete!\n[%%%%%%%%%%]"

    return f"{percent_number}% [{'%'*(percent_number//10)}{'.'*(10-percent_number//10)}]\nStill loading..."
print(check_loading_bar(percent_input))