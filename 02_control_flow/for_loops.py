"""
Examples of for loops.
"""

languages = ["Python", "Java", "JavaScript"]

for language in languages:
    print(language)


# Loop through numbers

for number in [1, 2, 3, 4, 5]:
    print("Number:", number)


# Loop through dictionaries

documents = [
    {"id": 1, "title": "Python"},
    {"id": 2, "title": "FastAPI"},
    {"id": 3, "title": "PyTorch"},
]

for document in documents:
    print(document["id"], document["title"])


# Practical filtering example

for document in documents:
    if document["title"] == "PyTorch":
        print("Found PyTorch document:", document)