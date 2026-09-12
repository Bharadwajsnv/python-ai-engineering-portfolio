"""
Examples of break, continue, and pass.
"""

# break stops the loop

for number in range(1, 6):
    if number == 4:
        break

    print("Break example:", number)


# continue skips the current iteration

for number in range(1, 6):
    if number == 3:
        continue

    print("Continue example:", number)


# pass does nothing temporarily

for number in range(1, 4):
    if number == 2:
        pass

    print("Pass example:", number)


# Practical document-processing example

documents = [
    {"id": 1, "title": "Python", "status": "ready"},
    {"id": 2, "title": "FastAPI", "status": "skipped"},
    {"id": 3, "title": "PyTorch", "status": "ready"},
]

for document in documents:
    if document["status"] == "skipped":
        continue

    print("Processing:", document["title"])