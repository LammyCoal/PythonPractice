def calculator(num1, num2):
    user_input = input('Which operation would you like to perform? *,+,-,/ :')
    try:
        if user_input == '*':
            return num1 * num2
        elif user_input == '+':
            return num1 + num2
        elif user_input == '-':
            return num1 - num2
        elif user_input == '/':
            return num1 / num2
    except ZeroDivisionError:
        print('You cannot divide by zero')

print(calculator(2, 0))

