# class User:
#     platform = "Python AI Engineering Portfolio"  # Class attribute

#     def __init__(self, name):
#         self.name = name  # Instance attribute


# user_one = User("Alice")
# user_two = User("Bob")


# print(f"User One: {user_one.name}, Platform: {User.platform}")
# print(f"User Two: {user_two.name}, Platform: {User.platform}")


class Document:
    document_count = 0  # Class attribute to keep track of the number of documents

    def __init__(self, content):
        self.content = content  # Instance attribute
        Document.document_count += 1  # Increment the document count when a new document is created

    @classmethod
    def get_document_count(cls):
        return cls.document_count  # Class method to get the current document count 

document_one = Document("Python is a versatile programming language.")
document_two = Document("AI engineering involves machine learning and data analysis.")
print(f"Document Count: {Document.get_document_count()}") 