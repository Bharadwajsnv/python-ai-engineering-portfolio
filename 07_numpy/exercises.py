import numpy as np


# Exercise 1
# Create a NumPy array containing numbers from 1 to 10.
numbers = np.arange(1, 11)

print("Exercise 1:", numbers)


# Exercise 2
# Print the first, last, and middle elements.
print("Exercise 2 - First:", numbers[0])
print("Exercise 2 - Last:", numbers[-1])
print("Exercise 2 - Middle:", numbers[len(numbers) // 2])


# Exercise 3
# Create an array containing only even numbers from 2 to 20.
even_numbers = np.arange(2, 21, 2)

print("Exercise 3:", even_numbers)


# Exercise 4
# Calculate the sum, mean, minimum, and maximum.
print("Exercise 4 - Sum:", np.sum(numbers))
print("Exercise 4 - Mean:", np.mean(numbers))
print("Exercise 4 - Minimum:", np.min(numbers))
print("Exercise 4 - Maximum:", np.max(numbers))


# Exercise 5
# Filter numbers greater than 5.
greater_than_five = numbers[numbers > 5]

print("Exercise 5:", greater_than_five)


# Exercise 6
# Create a 3x3 matrix containing numbers from 1 to 9.
matrix = np.arange(1, 10).reshape(3, 3)

print("Exercise 6:")
print(matrix)


# Exercise 7
# Print the second row and third column.
print("Exercise 7 - Second row:", matrix[1])
print("Exercise 7 - Third column:", matrix[:, 2])


# Exercise 8
# Create two vectors and calculate their dot product.
vector_a = np.array([2, 4, 6])
vector_b = np.array([1, 3, 5])

dot_product = np.dot(vector_a, vector_b)

print("Exercise 8 - Dot product:", dot_product)


# Exercise 9
# Normalize a vector.
vector = np.array([3, 4])

normalized_vector = vector / np.linalg.norm(vector)

print("Exercise 9 - Normalized vector:", normalized_vector)


# Exercise 10
# Compare two vectors using cosine similarity.
first_vector = np.array([1, 2, 3])
second_vector = np.array([2, 4, 6])

cosine_similarity = np.dot(first_vector, second_vector) / (
    np.linalg.norm(first_vector)
    * np.linalg.norm(second_vector)
)

print("Exercise 10 - Cosine similarity:", cosine_similarity)