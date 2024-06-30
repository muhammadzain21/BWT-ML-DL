from mymath import add, subtract, multiply, divide, mod, power, sqrt


def main():
    # Demonstration of basic arithmetic operations
    print("Addition (3 + 5):", add(3, 5))
    print("Subtraction (10 - 2):", subtract(10, 2))
    print("Multiplication (4 * 7):", multiply(4, 7))

    try:
        print("Division (15 / 3):", divide(15, 3))
        print("Division (15 / 0):", divide(15, 0))  # Should raise an error
    except ValueError as e:
        print("Error:", e)

    try:
        print("Modulus (20 % 6):", mod(20, 6))
        print("Modulus (20 % 0):", mod(20, 0))  # Should raise an error
    except ValueError as e:
        print("Error:", e)

    # Advanced operations
    print("Exponentiation (2 ** 3):", power(2, 3))

    try:
        print("Square Root (16):", sqrt(16))
        print("Square Root (-16):", sqrt(-16))  # Should raise an error
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
