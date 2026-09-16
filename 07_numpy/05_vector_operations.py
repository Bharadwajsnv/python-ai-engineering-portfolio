# import numpy as np


# vector_a = np.array([1, 2, 3])
# vector_b = np.array([4, 5, 6])

# print("Vector A:", vector_a)
# print("Vector B:", vector_b)


# # Vector addition
# addition = vector_a + vector_b
# print("Vector addition:", addition)


# # Vector subtraction
# subtraction = vector_a - vector_b
# print("Vector subtraction:", subtraction)


# # Scalar multiplication
# scaled_vector = vector_a * 10
# print("Scaled vector:", scaled_vector)


# # Dot product
# dot_product = np.dot(vector_a, vector_b)
# print("Dot product:", dot_product)


# # Alternative dot product syntax
# dot_product_alternative = vector_a @ vector_b
# print("Dot product using @:", dot_product_alternative)


# # Vector magnitude
# magnitude = np.linalg.norm(vector_a)
# print("Magnitude of Vector A:", magnitude)


# # Normalization
# normalized_vector = vector_a / np.linalg.norm(vector_a)
# print("Normalized Vector A:", normalized_vector)


# # Cosine similarity
# cosine_similarity = np.dot(vector_a, vector_b) / (
#     np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
# )

# print("Cosine similarity:", cosine_similarity)


import numpy as np


# Two vectors
vector_a = np.array([3, 4])
vector_b = np.array([6, 8])


# Magnitudes
magnitude_a = np.linalg.norm(vector_a)
magnitude_b = np.linalg.norm(vector_b)

print("Magnitude of A:", magnitude_a)
print("Magnitude of B:", magnitude_b)


# Normalized vectors
normalized_a = vector_a / magnitude_a
normalized_b = vector_b / magnitude_b

print("Normalized A:", normalized_a)
print("Normalized B:", normalized_b)


# Dot product
dot_product = np.dot(vector_a, vector_b)

print("Dot product:", dot_product)


# Cosine similarity
cosine_similarity = dot_product / (
    magnitude_a * magnitude_b
)

print("Cosine similarity:", cosine_similarity)