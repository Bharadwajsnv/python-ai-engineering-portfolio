# One parameter


def square(number):
    print(f"Square: {number * number}")


square(5)
square(8)


# Multiple parameters


def add_numbers(first_number, second_number):
    print(f"Sum: {first_number + second_number}")


add_numbers(10, 20)
add_numbers(5, 7)


# Different data types


def display_profile(name, age, is_engineer):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"AI Engineer: {is_engineer}")


display_profile("Bharadwaj", 25, True)


# AI-oriented example


def create_prompt(topic, audience):
    prompt = f"Explain {topic} for {audience}."
    print(prompt)


create_prompt("Python functions", "beginners")
create_prompt("RAG", "AI engineers")