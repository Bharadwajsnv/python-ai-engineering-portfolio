import numpy as np


numbers = np.array([10, 20, 30, 40, 50])

print("Original array:", numbers)

# Addition
print("Add 5:", numbers + 5)

# Subtraction
print("Subtract 5:", numbers - 5)

# Multiplication
print("Multiply by 2:", numbers * 2)

# Division
print("Divide by 10:", numbers / 10)

# Square
print("Square:", numbers ** 2)


print("\nOperations between two arrays")

first = np.array([10, 20, 30])
second = np.array([1, 2, 3])

print("First array:", first)
print("Second array:", second)

print("Addition:", first + second)
print("Subtraction:", first - second)
print("Multiplication:", first * second)
print("Division:", first / second)


print("\nUseful mathematical functions")

values = np.array([1, 4, 9, 16, 25])

print("Square root:", np.sqrt(values))
print("Sum:", np.sum(values))
print("Mean:", np.mean(values))
print("Minimum:", np.min(values))
print("Maximum:", np.max(values))
print("Standard deviation:", np.std(values))


print("\nComparison operations")

scores = np.array([45, 60, 75, 30, 90])

print("Scores:", scores)
print("Scores greater than 50:", scores > 50)
print("Scores equal to 60:", scores == 60)

print("Filtered scores greater than 50:")
print(scores[scores > 50])