"""
Python fundamentals exercises.

Try each question before checking the answer.
"""

# ============================================================
# Question 1
# Create variables for your name, age, and learning status.
# Print their values and types.
# ============================================================

name = "Bharadwaj"
age = 30
is_learning = True

print(name, type(name))
print(age, type(age))
print(is_learning, type(is_learning))


# ============================================================
# Question 2
# Given a string, print its first character, last character,
# and first three characters.
# ============================================================

language = "Python"

print(language[0])
print(language[-1])
print(language[:3])


# ============================================================
# Question 3
# Add "PyTorch" to the following list.
# ============================================================

tools = ["Python", "FastAPI", "Pydantic"]

tools.append("PyTorch")

print(tools)


# ============================================================
# Question 4
# Unpack this tuple into two variables.
# ============================================================

dimensions = (640, 480)

width, height = dimensions

print("Width:", width)
print("Height:", height)


# ============================================================
# Question 5
# Remove duplicate values using a set.
# ============================================================

numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = set(numbers)

print(unique_numbers)


# ============================================================
# Question 6
# Create a dictionary representing an AI document.
# ============================================================

document = {
    "id": 1,
    "title": "Python Basics",
    "content": "Python is useful for AI Engineering",
}

print(document["title"])
print(document["content"])