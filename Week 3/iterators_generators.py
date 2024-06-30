import random

# Countdown iterator class
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 1:
            raise StopIteration
        else:
            current_value = self.current
            self.current -= 1
            return current_value

# Generator function for Fibonacci numbers
def fibonacci_generator(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

# Generator function for random numbers in a specified range
def random_number_generator(start, end, count):
    for _ in range(count):
        yield random.randint(start, end)

# Main program execution
if __name__ == "__main__":
    # Get user input for Countdown
    countdown_start = int(input("Enter a number to start the countdown: "))
    print(f"\nCountdown from {countdown_start}:")
    countdown = Countdown(countdown_start)
    for number in countdown:
        print(number)

    # Get user input for Fibonacci generator
    fibonacci_limit = int(input("\nEnter the limit for Fibonacci numbers: "))
    print(f"\nFibonacci numbers up to {fibonacci_limit}:")
    for fib in fibonacci_generator(fibonacci_limit):
        print(fib)

    # Get user input for random number generator
    random_start = int(input("\nEnter the start of the range for random numbers: "))
    random_end = int(input("Enter the end of the range for random numbers: "))
    random_count = int(input("Enter the number of random numbers to generate: "))
    print(f"\n{random_count} random numbers between {random_start} and {random_end}:")
    for random_num in random_number_generator(random_start, random_end, random_count):
        print(random_num)
