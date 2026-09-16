class Document:
    def __init__(self, content):
        self.content = content

        def word_count(self):
            return len(self.content.split())

        def character_count(self):
            return len(self.content)

        def display_content(self):
            print(f"Document Content: {self.content}")



        document_one = Document("Python is a versatile programming language.")
        document_two = Document("AI engineering involves machine learning and data analysis.")  


        document_one.display_content()
        print(f"Word Count: {document_one.word_count()}")
        print(f"Character Count: {document_one.character_count()}") 


        