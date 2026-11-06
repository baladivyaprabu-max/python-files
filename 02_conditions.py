# Task 2: Conditional Statements
# Check whether a number is even or odd.

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")


# Find the largest of three numbers
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number:", a)
elif b >= a and b >= c:
    print("Largest number:", b)
else:
    print("Largest number:", c)
