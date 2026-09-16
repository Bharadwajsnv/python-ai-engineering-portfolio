class DocumentMetadata:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Category: {self.category}" 
    