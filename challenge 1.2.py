def factorial(n):
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    # Recursive case: factorial of n is n times the factorial of (n-1)
    else:
        return n * factorial(n - 1)

# Example usage:
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")