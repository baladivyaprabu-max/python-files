# Task 4: Functions
# A function is a reusable block of code.

def add_numbers(a, b):
    return a + b

def factorial(number):
    result = 1
    for value in range(1, number + 1):
        result *= value
    return result

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
print("Sum:", add_numbers(first, second))

n = int(input("\nEnter a non-negative number to find factorial: "))
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial:", factorial(n))
