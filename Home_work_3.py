number_1 = float(input("Select number:"))
number_2 = float(input("Select next number:"))
action = input("Choose an action; +, -, *, /:")


if action == '+':
    result = number_1 + number_2
elif action == '-':
    result = number_1 - number_2
elif action == '*':
    result = number_1 * number_2
elif action == '/':
    result = number_1 / number_2
else:
    result = "Invalid action selected"

print("Result:", result)