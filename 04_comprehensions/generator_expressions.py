# List comprehension creates the complete list immediately


numbers = [number * number for number in range(1, 6)]

print(f"List: {numbers}")


# Generator expression creates values lazily


squares_generator = (
    number * number
    for number in range(1, 6)
)

print(f"Generator object: {squares_generator}")


for square in squares_generator:
    print(f"Generated square: {square}")


# Sum using a generator expression


total = sum(
    number * number
    for number in range(1, 6)
)

print(f"Sum of squares: {total}")


# Check whether any document is empty


documents = [
    "Python notes",
    "AI notes",
    "",
    "RAG notes",
]

has_empty_document = any(
    document.strip() == ""
    for document in documents
)

print(f"Has empty document: {has_empty_document}")


# Check whether all documents are valid


all_documents_valid = all(
    document.strip() != ""
    for document in documents
)

print(f"All documents valid: {all_documents_valid}")


# AI-oriented example: count total words


document_collection = [
    "Python is useful",
    "AI needs data",
    "RAG uses retrieval",
]

total_words = sum(
    len(document.split())
    for document in document_collection
)

print(f"Total words: {total_words}")
