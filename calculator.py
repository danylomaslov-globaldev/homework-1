import math
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def add(a, b):
    _validate_number(a, "a")
    _validate_number(b, "b")
    result = a + b
    logger.info("add(%s, %s) = %s", a, b, result)
    return result


def subtract(a, b):
    _validate_number(a, "a")
    _validate_number(b, "b")
    result = a - b
    logger.info("subtract(%s, %s) = %s", a, b, result)
    return result


def multiply(a, b):
    _validate_number(a, "a")
    _validate_number(b, "b")
    result = a * b
    logger.info("multiply(%s, %s) = %s", a, b, result)
    return result


def divide(a, b):
    _validate_number(a, "a")
    _validate_number(b, "b")
    if b == 0:
        logger.error("divide(%s, %s) - division by zero", a, b)
        raise ValueError("Cannot divide by zero")
    result = a / b
    logger.info("divide(%s, %s) = %s", a, b, result)
    return result


def sqrt(a):
    _validate_number(a, "a")
    result = math.sqrt(a)
    logger.info("sqrt(%s) = %s", a, result)
    return result

def _validate_number(x, name="value"):
    if not isinstance(x, (int, float)):
        raise TypeError(f"{name} must be int or float, got {type(x).__name__}")


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
