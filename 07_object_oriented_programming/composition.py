"""
Composition

Composition means building a class using other classes.
"""


class TextCleaner:
    def clean(self, text):
        return " ".join(text.strip().lower().split())


class TextChunker:
    def chunk(self, text, chunk_size=3):
        words = text.split()

        return [
            words[index:index + chunk_size]
            for index in range(0, len(words), chunk_size)
        ]


class DocumentPipeline:
    def __init__(self):
        self.cleaner = TextCleaner()
        self.chunker = TextChunker()

    def process(self, text):
        cleaned_text = self.cleaner.clean(text)
        chunks = self.chunker.chunk(cleaned_text)

        return {
            "cleaned_text": cleaned_text,
            "chunks": chunks,
        }


pipeline = DocumentPipeline()

document = "  Python is useful for building AI applications  "

result = pipeline.process(document)

print(f"Cleaned text: {result['cleaned_text']}")
print(f"Chunks: {result['chunks']}")


# More realistic AI-oriented example


class DocumentLoader:
    def load(self):
        return [
            "Python is useful for AI.",
            "RAG uses retrieval.",
        ]


class DocumentProcessor:
    def __init__(self):
        self.loader = DocumentLoader()
        self.cleaner = TextCleaner()

    def run(self):
        documents = self.loader.load()

        return [
            self.cleaner.clean(document)
            for document in documents
        ]


processor = DocumentProcessor()

print(processor.run())