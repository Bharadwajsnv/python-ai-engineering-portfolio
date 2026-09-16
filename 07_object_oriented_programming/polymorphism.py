"""
Polymorphism

Different classes can provide the same method name
with different implementations.
"""


class PDFDocument:
    def extract_text(self):
        return "Text extracted from PDF"


class WebDocument:
    def extract_text(self):
        return "Text extracted from web page"


class WordDocument:
    def extract_text(self):
        return "Text extracted from Word document"


def process_document(document):
    print(document.extract_text())


documents = [
    PDFDocument(),
    WebDocument(),
    WordDocument(),
]


for document in documents:
    process_document(document)


# Another example


class Dog:
    def speak(self):
        return "Woof"


class Cat:
    def speak(self):
        return "Meow"


class Robot:
    def speak(self):
        return "Hello, I am a robot"


def make_speak(entity):
    print(entity.speak())


make_speak(Dog())
make_speak(Cat())
make_speak(Robot())


# AI-oriented example


class KeywordRetriever:
    def search(self, query):
        return f"Keyword search results for: {query}"


class VectorRetriever:
    def search(self, query):
        return f"Vector search results for: {query}"


def retrieve_documents(retriever, query):
    return retriever.search(query)


keyword_retriever = KeywordRetriever()
vector_retriever = VectorRetriever()

print(retrieve_documents(keyword_retriever, "Python"))
print(retrieve_documents(vector_retriever, "Python"))