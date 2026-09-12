"""
Practice exercises:
Collections and Data Processing

Try solving each question before looking at the answer.
"""


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


# ============================================================
# Question 1
# Print all document titles.
# ============================================================

# Your answer:
for document in documents:
    print(document["title"])


# ============================================================
# Question 2
# Print only documents whose title is "FastAPI".
# ============================================================

# Your answer:
for document in documents:
    if document["title"] == "FastAPI":
        print(document)


# ============================================================
# Question 3
# Create a list containing only document titles.
# ============================================================

# Your answer:
titles = [
    document["title"]
    for document in documents
]

print(titles)


# ============================================================
# Question 4
# Create a list containing documents whose content includes "AI".
# ============================================================

# Your answer:
ai_documents = [
    document
    for document in documents
    if "AI" in document["content"]
]

print(ai_documents)


# ============================================================
# Question 5
# Write a function that returns documents matching a keyword.
# ============================================================

# Your answer:
def search_documents(documents, keyword):
    return [
        document
        for document in documents
        if keyword.lower() in document["content"].lower()
    ]


print(search_documents(documents, "python"))
print(search_documents(documents, "deep"))