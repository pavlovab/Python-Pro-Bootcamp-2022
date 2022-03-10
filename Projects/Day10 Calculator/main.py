from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = { 
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for operation in operations:
        print(operation)
    should_continue = True

    while should_continue:
        symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {symbol} {num2} = {answer}")

        continue_calculating = input(f"Type 'y' if you want to continue calculating with {answer} or 'n' to start a new calculation. Type 'e' to exit.: ").lower()
        if continue_calculating == 'y':
            num1 = answer
        elif continue_calculating == 'n':
            should_continue = False
            calculator()
        elif continue_calculating == 'e':
            should_continue = False
            print("Goodbye!")

calculator()