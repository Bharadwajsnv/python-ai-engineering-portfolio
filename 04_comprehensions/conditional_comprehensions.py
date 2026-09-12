numbers = list(range(1, 11))


# Traditional filtering


even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(f"Traditional even numbers: {even_numbers}")


# Conditional list comprehension


even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print(f"Comprehension even numbers: {even_numbers}")


# Odd numbers


odd_numbers = [
    number
    for number in numbers
    if number % 2 != 0
]

print(f"Odd numbers: {odd_numbers}")


# Numbers greater than 5


large_numbers = [
    number
    for number in numbers
    if number > 5
]

print(f"Numbers greater than 5: {large_numbers}")


# Conditional transformation


labels = [
    "Even" if number % 2 == 0 else "Odd"
    for number in numbers
]

print(f"Number labels: {labels}")


# AI-oriented example: filter valid documents


documents = [
    "Python notes",
    "",
    "Machine learning notes",
    "   ",
    "AI engineering guide",
]

valid_documents = [
    document.strip()
    for document in documents
    if document.strip()
]

print(f"Valid documents: {valid_documents}")


# Filter long documents


document_names = [
    "Python",
    "Machine Learning",
    "Artificial Intelligence",
    "AI",
]

long_document_names = [
    name
    for name in document_names
    if len(name) > 5
]

print(f"Long names: {long_document_names}")