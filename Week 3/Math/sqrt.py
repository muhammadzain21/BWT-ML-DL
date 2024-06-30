import math

def sqrt(a):
    """Return the square root of a number. Raise an error if the number is negative."""
    if a < 0:
        raise ValueError("Cannot compute the square root of a negative number")
    return math.sqrt(a)
