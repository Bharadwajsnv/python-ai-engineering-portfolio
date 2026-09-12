# Create a dictionary of squares


numbers = [1, 2, 3, 4, 5]

squares = {
    number: number * number
    for number in numbers
}

print(f"Squares dictionary: {squares}")


# Create a dictionary of word lengths


words = ["python", "machine", "learning"]

word_lengths = {
    word: len(word)
    for word in words
}

print(f"Word lengths: {word_lengths}")


# Convert words to uppercase as dictionary values


uppercase_words = {
    word: word.upper()
    for word in words
}

print(f"Uppercase words: {uppercase_words}")


# Conditional dictionary comprehension


even_squares = {
    number: number * number
    for number in numbers
    if number % 2 == 0
}

print(f"Even squares: {even_squares}")


# AI-oriented example: document statistics


documents = {
    "doc1": "Python is useful",
    "doc2": "AI needs data",
    "doc3": "RAG uses retrieval",
}

document_word_counts = {
    document_id: len(content.split())
    for document_id, content in documents.items()
}

print(f"Document word counts: {document_word_counts}")


# Create an inverted lookup


categories = {
    "doc1": "AI",
    "doc2": "Python",
    "doc3": "AI",
}

category_to_documents = {
    category: [
        document_id
        for document_id, document_category in categories.items()
        if document_category == category
    ]
    for category in set(categories.values())
}

print(f"Category lookup: {category_to_documents}")
