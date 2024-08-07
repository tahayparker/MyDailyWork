def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")
    match operation:
        case '+':
            print(num1 + num2)
        case '-':
            print(num1 - num2)
        case '*':
            print(num1 * num2)
        case '/':
            if num2 == 0:
                print("Cannot divide by zero")
                calculator()
            else:
                print(num1 / num2)
        case _:
            print("Invalid operation")
            calculator()

calculator()
