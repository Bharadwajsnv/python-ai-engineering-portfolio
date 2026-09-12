# Exercise 1: Create a greeting function


def greet():
    print("Welcome to Python functions!")


greet()


# Exercise 2: Function with a parameter


def greet_user(name):
    print(f"Hello, {name}!")


greet_user("Bharadwaj")


# Exercise 3: Return the square of a number


def square(number):
    return number * number


print(f"Square: {square(6)}")


# Exercise 4: Check whether a document is empty


def is_empty_document(document):
    return document.strip() == ""


print(is_empty_document(""))
print(is_empty_document("Python notes"))


# Exercise 5: Count words in a document


def count_words(document):
    return len(document.split())


text = "Python is useful for AI engineering"

print(f"Word count: {count_words(text)}")


# Exercise 6: Use a default argument


def summarize(document, language="English"):
    return f"Summary in {language}: {document}"


print(summarize("Python fundamentals"))
print(summarize("Python fundamentals", "Telugu"))


# Exercise 7: Calculate document statistics


def document_statistics(document):
    words = document.split()
    characters = len(document)

    return {
        "word_count": len(words),
        "character_count": characters,
    }


document = "Python helps build AI applications"

statistics = document_statistics(document)

print(statistics)


# Exercise 8: Filter valid documents


def get_valid_documents(documents):
    valid_documents = []

    for document in documents:
        if document.strip() != "":
            valid_documents.append(document)

    return valid_documents


documents = [
    "Python notes",
    "",
    "Machine learning",
    "   ",
    "AI engineering",
]

print(get_valid_documents(documents))


# Exercise 9: Calculate average


def calculate_average(numbers):
    if len(numbers) == 0:
        return 0

    return sum(numbers) / len(numbers)


print(f"Average: {calculate_average([10, 20, 30])}")
print(f"Average: {calculate_average([])}")


# Exercise 10: Create a prompt


def create_prompt(topic, audience="beginners"):
    return f"Explain {topic} for {audience}."


print(create_prompt("Python functions"))
print(create_prompt("RAG", "AI engineers"))