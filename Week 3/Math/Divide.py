def divide(a, b):
    """Return the division of two numbers. Raise an error if divisor is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
