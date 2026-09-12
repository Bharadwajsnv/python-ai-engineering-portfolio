
# Traditional way


numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number * number)

print(f"Traditional squares: {squares}")


# List comprehension


squares = [number * number for number in numbers]

print(f"Comprehension squares: {squares}")


# Convert numbers to strings


number_strings = [str(number) for number in numbers]

print(f"Number strings: {number_strings}")


# Convert words to uppercase


words = ["python", "machine learning", "ai"]

uppercase_words = [word.upper() for word in words]

print(f"Uppercase words: {uppercase_words}")


# Get word lengths


word_lengths = [len(word) for word in words]

print(f"Word lengths: {word_lengths}")


# AI-oriented example: clean documents


documents = [
    "  Python basics  ",
    "Machine Learning",
    "  AI Engineering",
]

cleaned_documents = [
    document.strip().lower()
    for document in documents
]

print(f"Cleaned documents: {cleaned_documents}")