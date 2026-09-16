import numpy as np

# numbers = np.array([1, 2, 3, 4, 5])
# print("Numpy Array:", numbers)

# print("First 3 elements:", numbers[:3])  # Slicing the first 3 elements
# print("Elements from index 2 to 4:", numbers[2:5])  # Slicing elements from index 2 to 4
# print("Every second element:", numbers[::2])  # Slicing every second element
# print("Reversed array:", numbers[::-1])  # Reversing the array



matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\n2D Numpy Array:\n", matrix)
print("First row:", matrix[0])  # Accessing the first row
print("Second row, second column:", matrix[1, -1])  # Accessing the element at second row, second column
print("Second row", matrix[1])  # Accessing the second row
print("Last row:", matrix[2])  # Accessing the last row
