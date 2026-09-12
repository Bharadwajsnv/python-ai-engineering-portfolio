"""
Python string examples.

Topics:
- String creation
- Indexing
- Slicing
- String methods
- f-strings
"""

language = "Python"

print(language)
print(language[0])
print(language[-1])
print(language[0:3])
print(language.upper())
print(language.lower())
print(language.replace("Python", "Python AI"))

name = "Bharadwaj"
topic = "AI Engineering"

message = f"{name} is learning {topic} with {language}."

print(message)