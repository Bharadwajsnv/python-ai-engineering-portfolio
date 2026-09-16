
"""
Inheritance

A child class inherits behavior from a parent class.
"""


class Document:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Content: {self.content}")


class PDFDocument(Document):
    def extract_text(self):
        return self.content


class WebDocument(Document):
    def get_url_info(self):
        return "This document came from a web page."


pdf_document = PDFDocument(
    "Python PDF",
    "Python is useful for AI.",
)

web_document = WebDocument(
    "AI Article",
    "AI systems process information.",
)


pdf_document.display_info()
print(f"Extracted text: {pdf_document.extract_text()}")

print("---")

web_document.display_info()
print(web_document.get_url_info())


# Using super()


class TextDocument(Document):
    def __init__(self, title, content, encoding="UTF-8"):
        super().__init__(title, content)
        self.encoding = encoding

    def display_encoding(self):
        print(f"Encoding: {self.encoding}")


text_document = TextDocument(
    "Text File",
    "Python text content",
)

text_document.display_info()
text_document.display_encoding()
