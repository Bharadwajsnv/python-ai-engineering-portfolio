pairs = []

for first in [1, 2, 3]:
    for second in [10, 20]:
        pairs.append((first, second))

print(f"Traditional pairs: {pairs}")


# Nested list comprehension


pairs = [
    (first, second)
    for first in [1, 2, 3]
    for second in [10, 20]
]

print(f"Comprehension pairs: {pairs}")


# Create a multiplication table


multiplication_table = [
    number * multiplier
    for number in range(1, 4)
    for multiplier in range(1, 4)
]

print(f"Multiplication values: {multiplication_table}")


# Flatten a nested list


nested_numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

flattened_numbers = [
    number
    for row in nested_numbers
    for number in row
]

print(f"Flattened numbers: {flattened_numbers}")


# AI-oriented example: flatten document chunks


document_chunks = [
    ["Python", "is", "useful"],
    ["AI", "needs", "data"],
    ["RAG", "uses", "retrieval"],
]

all_words = [
    word
    for chunk in document_chunks
    for word in chunk
]

print(f"All words: {all_words}")