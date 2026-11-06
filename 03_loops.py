# Task 3: Loops
# Print numbers from 1 to 10 using a for loop.

print("Numbers from 1 to 10:")
for number in range(1, 11):
    print(number)

# Print a multiplication table using a while loop.
value = int(input("\nEnter a number for its multiplication table: "))
count = 1

while count <= 10:
    print(value, "x", count, "=", value * count)
    count += 1
