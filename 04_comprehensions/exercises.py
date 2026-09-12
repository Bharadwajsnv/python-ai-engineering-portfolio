# Exercise 1: Create squares from 1 to 10


squares = [
    number * number
    for number in range(1, 11)
]

print(f"Squares: {squares}")


# Exercise 2: Get even numbers from 1 to 20


even_numbers = [
    number
    for number in range(1, 21)
    if number % 2 == 0
]

print(f"Even numbers: {even_numbers}")


# Exercise 3: Convert words to uppercase


words = ["python", "ai", "rag", "langchain"]

uppercase_words = [
    word.upper()
    for word in words
]

print(f"Uppercase words: {uppercase_words}")


# Exercise 4: Filter words with more than 4 characters


long_words = [
    word
    for word in words
    if len(word) > 4
]

print(f"Long words: {long_words}")


# Exercise 5: Remove empty documents


documents = [
    "Python notes",
    "",
    "AI engineering",
    "   ",
    "RAG tutorial",
]

valid_documents = [
    document.strip()
    for document in documents
    if document.strip()
]

print(f"Valid documents: {valid_documents}")


# Exercise 6: Create a dictionary of document word counts


document_data = {
    "doc1": "Python is easy",
    "doc2": "AI needs data",
    "doc3": "RAG uses retrieval",
}

word_counts = {
    document_id: len(content.split())
    for document_id, content in document_data.items()
}

print(f"Word counts: {word_counts}")


# Exercise 7: Create a set of unique words


text = "python ai python rag ai python"

unique_words = {
    word
    for word in text.split()
}

print(f"Unique words: {unique_words}")


# Exercise 8: Flatten nested lists


nested_lists = [
    [1, 2],
    [3, 4],
    [5, 6],
]

flattened = [
    number
    for group in nested_lists
    for number in group
]

print(f"Flattened list: {flattened}")


# Exercise 9: Label numbers as even or odd


number_labels = {
    number: "Even" if number % 2 == 0 else "Odd"
    for number in range(1, 6)
}

print(f"Number labels: {number_labels}")


# Exercise 10: Calculate total document words using a generator


documents = [
    "Python is useful",
    "AI needs data",
    "RAG uses retrieval",
]

total_words = sum(
    len(document.split())
    for document in documents
)

print(f"Total document words: {total_words}")