from art import logo

# Add
def add(n1, n2):
    return n1 + n2

# Substract
def substract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    should_continue = True
    num1 = float(input("What's the first number?: "))

    while should_continue:
        num2 = float(input("What's the second number?: "))

        for operation in operations:
            print(operation)

        operation_symbol = input("Pick an operation from the line above: ")

        if operation_symbol in operations:
            answer = operations[operation_symbol](num1, num2)
        else:
            print("Operation non existe")

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        will_continue = input("Type 'y' to continue calculating with 8, or type 'n' to exit.: ")

        if will_continue != "y":
            should_continue = False
            calculator()
        else:
            num1 = answer

calculator()