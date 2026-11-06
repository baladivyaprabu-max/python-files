# Task 5: Lists
# A list stores multiple values in one variable.

numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)
print("First element:", numbers[0])
print("Number of elements:", len(numbers))
print("Sum of elements:", sum(numbers))

numbers.append(60)
print("After adding 60:", numbers)

numbers.remove(20)
print("After removing 20:", numbers)

print("Elements one by one:")
for item in numbers:
    print(item)
