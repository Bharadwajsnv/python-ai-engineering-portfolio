# Returning a value


def add_numbers(first_number, second_number):
    return first_number + second_number


result = add_numbers(10, 20)

print(f"Result: {result}")


# Returning a string


def clean_text(text):
    return text.strip().lower()


cleaned_text = clean_text("  Hello Python  ")

print(f"Cleaned text: {cleaned_text}")


# Returning a Boolean


def is_valid_document(document):
    return document.strip() != ""


print(is_valid_document("Python notes"))
print(is_valid_document("   "))


# Returning multiple values


def calculate_statistics(numbers):
    total = sum(numbers)
    count = len(numbers)

    return total, count


total, count = calculate_statistics([10, 20, 30, 40])

print(f"Total: {total}")
print(f"Count: {count}")


# AI-oriented example


def count_words(document):
    words = document.split()
    return len(words)


document = "Python is useful for AI engineering"

word_count = count_words(document)

print(f"Word count: {word_count}")