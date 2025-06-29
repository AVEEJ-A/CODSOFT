
def basic_calculator():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /): ")

    if op == '+':
        print(f"Result: {a + b}")
    elif op == '-':
        print(f"Result: {a - b}")
    elif op == '*':
        print(f"Result: {a * b}")
    elif op == '/':
        if b != 0:
            print(f"Result: {a / b}")
        else:
            print("Cannot divide by zero.")
    else:
        print("Invalid operation.")
