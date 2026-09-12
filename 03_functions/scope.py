# Global variable

app_name = "AI Engineering Portfolio"


def display_app_name():
    print(f"Inside function: {app_name}")


display_app_name()

print(f"Outside function: {app_name}")


# Local variable


def create_message():
    message = "This is a local variable"
    print(message)


create_message()


# The following would cause an error if uncommented:
# print(message)


# Same variable name in different scopes


name = "Global Bharadwaj"


def display_name():
    name = "Local Bharadwaj"
    print(f"Inside function: {name}")


display_name()

print(f"Outside function: {name}")


# Using a global variable inside a function


counter = 0


def show_counter():
    print(f"Counter: {counter}")


show_counter()


# AI-oriented example


default_model = "gpt-model"


def display_model():
    model_name = "embedding-model"

    print(f"Default model: {default_model}")
    print(f"Local model: {model_name}")


display_model()