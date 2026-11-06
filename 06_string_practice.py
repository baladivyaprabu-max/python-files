# Task 6: String Practice
# Reverse a string and count its characters.

word = input("Enter a word: ")

print("Original word:", word)
print("Reversed word:", word[::-1])
print("Number of characters:", len(word))

if word == word[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
