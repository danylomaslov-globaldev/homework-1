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


def main():
    print("Simple Calculator")
    print("Available operations: +, -, *, /")

    a = float(input("Enter first number: "))
    operation = input("Enter operation: ")
    b = float(input("Enter second number: "))

    if operation == "+":
        result = add(a, b)
    elif operation == "-":
        result = subtract(a, b)
    elif operation == "*":
        result = multiply(a, b)
    elif operation == "/":
        result = divide(a, b)
    else:
        print("Invalid operation")
        return

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
