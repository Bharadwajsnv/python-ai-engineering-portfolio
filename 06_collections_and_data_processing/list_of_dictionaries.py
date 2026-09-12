documents = [
    {
        "id": 1,
        "title": "Python Basics",
        "content": "Python is useful for AI Engineering",
    },
    {
        "id": 2,
        "title": "FastAPI",
        "content": "FastAPI is used to build APIs",
    },
    {
        "id": 3,
        "title": "PyTorch",
        "content": "PyTorch is used for deep learning",
    },
    {
        "id": 4,
        "title": "LangChain",
        "content": "LangChain helps build LLM applications",
    },
]


def find_documents_by_keyword(documents, keyword):
    keyword = keyword.lower()

    return [
        document
        for document in documents
        if keyword in document["content"].lower()
    ]


ai_documents = find_documents_by_keyword(documents, "AI")
python_documents = find_documents_by_keyword(documents, "Python")
api_documents = find_documents_by_keyword(documents, "API")

print("AI documents:", ai_documents)
print("Python documents:", python_documents)
print("API documents:", api_documents)