import math
import logging
from pathlib import Path


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

HISTORY_FILE = Path("history.txt")


def add(a, b):
    _validate_number(a, "a")
    _validate_number(b, "b")
    result = a + b
    logger.info("add(%s, %s) = %s", a, b, result)
    _save_history(f"add({a}, {b}) = {result}")
    return result


def subtract(a, b):
    _validate_number(a, "a")
    _validate_number(b, "b")
    result = a - b
    logger.info("subtract(%s, %s) = %s", a, b, result)
    _save_history(f"subtract({a}, {b}) = {result}")
    return result


def multiply(a, b):
    _validate_number(a, "a")
    _validate_number(b, "b")
    result = a * b
    logger.info("multiply(%s, %s) = %s", a, b, result)
    _save_history(f"multiply({a}, {b}) = {result}")
    return result


def divide(a, b):
    _validate_number(a, "a")
    _validate_number(b, "b")
    if b == 0:
        logger.error("divide(%s, %s) - division by zero", a, b)
        raise ValueError("Cannot divide by zero")
    result = a / b
    logger.info("divide(%s, %s) = %s", a, b, result)
    _save_history(f"divide({a}, {b}) = {result}")
    return result


def sqrt(a):
    _validate_number(a, "a")
    if a < 0:
        raise ValueError("Square root of a negative number is not supported")
    result = math.sqrt(a)
    logger.info("sqrt(%s) = %s", a, result)
    _save_history(f"sqrt({a}) = {result}")
    return result


def _validate_number(x, name="value"):
    if not isinstance(x, (int, float)):
        raise TypeError(f"{name} must be int or float, got {type(x).__name__}")


def _save_history(entry: str) -> None:
    HISTORY_FILE.write_text(
        (HISTORY_FILE.read_text() if HISTORY_FILE.exists() else "") + entry + "\n",
        encoding="utf-8",
    )

def _read_history() -> list[str]:
    if not HISTORY_FILE.exists():
        return []
    return [
    line.strip() for line in HISTORY_FILE.read_text(encoding="utf-8").splitlines()
    if line.strip()
]



def main():
    print("Simple Calculator")
    print("Available operations: +, -, *, /, sqrt, history")
    operation = input("Enter operation: ")

    if operation == "history":
        items = _read_history()
        if not items:
            print("History is empty")
        else:
            print("History:")
            for i, item in enumerate(items, start=1):
                print(f"{i}. {item}")
        return

    try:
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

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")



if __name__ == "__main__":
    main()
