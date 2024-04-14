import pytest
from main import calculate_fibonacci, calculate_lucas

def test_calculate_fibonacci():
    tests = [(1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34), (10, 55)]
    for n, expected_fibonacci_result in tests:
        fibonacci_result = calculate_fibonacci(n)
        assert fibonacci_result == expected_fibonacci_result, f"The {n}th Fibonacci number should be {expected_fibonacci_result}, but got {fibonacci_result}"

def test_calculate_lucas():
    tests = [(1, 1), (2, 3), (3, 4), (4, 7), (5, 11), (6, 18), (7, 29), (8, 47), (9, 76), (10, 123)]
    for n, expected_lucas_result in tests:
        lucas_result = calculate_lucas(n)
        assert lucas_result == expected_lucas_result, f"The {n}th Lucas number should be {expected_lucas_result}, but got {lucas_result}"
