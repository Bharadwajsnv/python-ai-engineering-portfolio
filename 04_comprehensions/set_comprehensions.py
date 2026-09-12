numbers = [1, 2, 2, 3, 4, 4, 5]

squares = {
    number * number
    for number in numbers
}

print(f"Unique squares: {squares}")


# Unique lowercase words


words = [
    "Python",
    "python",
    "AI",
    "ai",
    "RAG",
]

unique_words = {
    word.lower()
    for word in words
}

print(f"Unique words: {unique_words}")


# Unique word lengths


word_lengths = {
    len(word)
    for word in words
}

print(f"Unique word lengths: {word_lengths}")


# AI-oriented example: unique document categories


documents = [
    {"name": "doc1", "category": "AI"},
    {"name": "doc2", "category": "Python"},
    {"name": "doc3", "category": "AI"},
    {"name": "doc4", "category": "RAG"},
]

categories = {
    document["category"]
    for document in documents
}

print(f"Document categories: {categories}")