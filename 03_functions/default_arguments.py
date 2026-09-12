# Default parameter


def greet_user(name="Guest"):
    print(f"Hello, {name}!")


greet_user("Bharadwaj")
greet_user()


# Multiple parameters with a default value


def create_user(name, role="User"):
    print(f"Name: {name}")
    print(f"Role: {role}")


create_user("Bharadwaj", "AI Engineer")
create_user("Ravi")


# Default value for document language


def summarize_document(document, language="English"):
    print(f"Summarizing document in {language}: {document}")


summarize_document("Python fundamentals")
summarize_document("Machine learning notes", "Telugu")


# Default processing limit


def process_documents(documents, limit=3):
    for document in documents[:limit]:
        print(f"Processing: {document}")


documents = [
    "Document 1",
    "Document 2",
    "Document 3",
    "Document 4",
    "Document 5",
]

process_documents(documents)
print("---")
process_documents(documents, 5)