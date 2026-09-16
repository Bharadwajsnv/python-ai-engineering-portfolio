import numpy as np


matrix_a = np.array([
    [1, 2],
    [3, 4]
])

matrix_b = np.array([
    [5, 6],
    [7, 8]
])

print("Matrix A:")
print(matrix_a)

print("\nMatrix B:")
print(matrix_b)


# Matrix addition
print("\nMatrix addition:")
print(matrix_a + matrix_b)


# Matrix subtraction
print("\nMatrix subtraction:")
print(matrix_a - matrix_b)


# Element-wise multiplication
print("\nElement-wise multiplication:")
print(matrix_a * matrix_b)


# Matrix multiplication
print("\nMatrix multiplication:")
print(matrix_a @ matrix_b)


# Using np.matmul
print("\nMatrix multiplication using np.matmul:")
print(np.matmul(matrix_a, matrix_b))


# Transpose
print("\nTranspose of Matrix A:")
print(matrix_a.T)


# Determinant
print("\nDeterminant of Matrix A:")
print(np.linalg.det(matrix_a))


# Inverse
print("\nInverse of Matrix A:")
print(np.linalg.inv(matrix_a))


# Identity matrix
identity_matrix = np.eye(3)

print("\nIdentity matrix:")
print(identity_matrix)