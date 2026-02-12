import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def sqrt(a):
    return math.sqrt(a)


def main():
    print("Simple Calculator")
    print("Available operations: +, -, *, /, sqrt")
    operation = input("Enter operation: ")

    if operation == "sqrt":
        a = float(input("Enter number: "))
        result = sqrt(a)
    elif operation in {"+", "-", "*", "/"}:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if operation == "+":
            result = add(a, b)
        elif operation == "-":
            result = subtract(a, b)
        elif operation == "*":
            result = multiply(a, b)
        else:
            result = divide(a, b)
    else:
        print("Invalid operation")
        return

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
