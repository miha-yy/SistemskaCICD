import pytest
from main import calculate_fibonacci, calculate_lucas

def test_calculate_fibonacci():
    n = 10
    expected_fibonacci_result = 55
    fibonacci_result = calculate_fibonacci(n)
    assert fibonacci_result == expected_fibonacci_result, f"The {n}th Fibonacci number should be {expected_fibonacci_result}, but got {fibonacci_result}"

def test_calculate_lucas():
    n = 10
    expected_lucas_result = 123
    lucas_result = calculate_lucas(n)
    assert lucas_result == expected_lucas_result, f"The {n}th Lucas number should be {expected_lucas_result}, but got {lucas_result}"

def test_calculate_fibonacci_20():
    n = 20
    expected_fibonacci_result = 6765
    fibonacci_result = calculate_fibonacci(n)
    assert fibonacci_result == expected_fibonacci_result, f"The {n}th Fibonacci number should be {expected_fibonacci_result}, but got {fibonacci_result}"

def test_calculate_lucas_20():
    n = 20
    expected_lucas_result = 15127
    lucas_result = calculate_lucas(n)
    assert lucas_result == expected_lucas_result, f"The {n}th Lucas number should be {expected_lucas_result}, but got {lucas_result}"

def test_calculate_fibonacci_30():
    n = 30
    expected_fibonacci_result = 832040
    fibonacci_result = calculate_fibonacci(n)
    assert fibonacci_result == expected_fibonacci_result, f"The {n}th Fibonacci number should be {expected_fibonacci_result}, but got {fibonacci_result}"

def test_calculate_lucas_30():
    n = 30
    expected_lucas_result = 1149851
    lucas_result = calculate_lucas(n)
    assert lucas_result == expected_lucas_result, f"The {n}th Lucas number should be {expected_lucas_result}, but got {lucas_result}"

def test_calculate_fibonacci_40():
    n = 40
    expected_fibonacci_result = 102334155
    fibonacci_result = calculate_fibonacci(n)
    assert fibonacci_result == expected_fibonacci_result, f"The {n}th Fibonacci number should be {expected_fibonacci_result}, but got {fibonacci_result}"

def test_calculate_lucas_40():
    n = 40
    expected_lucas_result = 3524578
    lucas_result = calculate_lucas(n)
    assert lucas_result == expected_lucas_result, f"The {n}th Lucas number should be {expected_lucas_result}, but got {lucas_result}"

def test_calculate_fibonacci_50():
    n = 50
    expected_fibonacci_result = 12586269025
    fibonacci_result = calculate_fibonacci(n)
    assert fibonacci_result == expected_fibonacci_result, f"The {n}th Fibonacci number should be {expected_fibonacci_result}, but got {fibonacci_result}"

def test_calculate_lucas_50():
    n = 50
    expected_lucas_result = 6557470319842
    lucas_result = calculate_lucas(n)
    assert lucas_result == expected_lucas_result, f"The {n}th Lucas number should be {expected_lucas_result}, but got {lucas_result}"

def test_calculate_fibonacci_60():
    n = 60
    expected_fibonacci_result = 1548008755920
    fibonacci_result = calculate_fibonacci(n)
    assert fibonacci_result == expected_fibonacci_result, f"The {n}th Fibonacci number should be {expected_fibonacci_result}, but got {fibonacci_result}"

def test_calculate_lucas_60():
    n = 60
    expected_lucas_result = 35778556603416727
    lucas_result = calculate_lucas(n)
    assert lucas_result == expected_lucas_result, f"The {n}th Lucas number should be {expected_lucas_result}, but got {lucas_result}"
