"""
Control flow exercises.

Try solving each question before checking the answer.
"""


# ============================================================
# Question 1
# Print whether a number is positive, negative, or zero.
# ============================================================

number = -5

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# ============================================================
# Question 2
# Print all numbers from 1 to 10 using a for loop.
# ============================================================

for number in range(1, 11):
    print(number)


# ============================================================
# Question 3
# Print only even numbers from 1 to 20.
# ============================================================

for number in range(1, 21):
    if number % 2 == 0:
        print(number)


# ============================================================
# Question 4
# Calculate the sum of numbers from 1 to 5.
# ============================================================

total = 0

for number in range(1, 6):
    total += number

print("Total:", total)


# ============================================================
# Question 5
# Find the first document with the title "PyTorch".
# Stop searching after finding it.
# ============================================================

documents = [
    {"id": 1, "title": "Python"},
    {"id": 2, "title": "FastAPI"},
    {"id": 3, "title": "PyTorch"},
    {"id": 4, "title": "LangChain"},
]

for document in documents:
    if document["title"] == "PyTorch":
        print("Found:", document)
        break


# ============================================================
# Question 6
# Skip documents whose status is "skipped".
# ============================================================

documents = [
    {"title": "Python", "status": "ready"},
    {"title": "FastAPI", "status": "skipped"},
    {"title": "PyTorch", "status": "ready"},
]

for document in documents:
    if document["status"] == "skipped":
        continue

    print("Processing:", document["title"])


# ============================================================
# Question 7
# Use a while loop to print 5, 4, 3, 2, 1.
# ============================================================

counter = 5

while counter >= 1:
    print(counter)
    counter -= 1