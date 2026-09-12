"""
Examples of range().
range(start, stop, step)
"""

# 0, 1, 2, 3, 4
for number in range(5):
    print(f"Number: {number}")


# 1, 2, 3, 4, 5
for number in range(1, 6):
    print(f"Number: {number}")


# Even numbers from 0 to 10
for number in range(0, 11, 2):
    print(f"Even number: {number}")


# Countdown
for number in range(5, 0, -1):
    print(f"Countdown: {number}")


# Create a list using range
numbers = list(range(1, 6))

print(numbers)