import pytest
import math

def calculate_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def calculate_lucas(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    fibonacci_result = calculate_fibonacci(5)
    lucas_result = calculate_lucas(5)

    print("5th Fibonacci number:", fibonacci_result)
    print("5th Lucas number:", lucas_result)
