def mod(a, b):
    """Return the remainder of the division of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a % b
