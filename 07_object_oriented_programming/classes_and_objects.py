class Document:pass

document_one = Document()
document_two = Document()

print(f"Document One: {document_one}")
print(f"Document Two: {document_two}")

class AIEngineer:
    def __init__(self, name, expertise):
        self.name = name
        self.expertise = expertise

    def introduce(self):
        print(f"Hello, I am {self.name}, an AI Engineer specializing in {self.expertise}.")

print("---")
print(f"Creating AI Engineer instances...")
engineer_one = AIEngineer("Alice", "Machine Learning")
engineer_two = AIEngineer("Bob", "Natural Language Processing")

engineer_one.introduce()
engineer_two.introduce()