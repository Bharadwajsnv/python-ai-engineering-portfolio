import dataclasses

"""
Dataclasses

Dataclasses reduce boilerplate code for data-holding classes.
"""

from dataclasses import dataclass, field


@dataclass
class DocumentMetadata:
    document_id: str
    title: str
    source: str
    tags: list[str] = field(default_factory=list)


metadata = DocumentMetadata(
    document_id="doc-001",
    title="Python Fundamentals",
    source="learning-notes",
    tags=["python", "ai"],
)

print(metadata)
print(f"Title: {metadata.title}")
print(f"Tags: {metadata.tags}")


# Updating a field


metadata.title = "Updated Python Fundamentals"

print(metadata)


# Comparing dataclass objects


metadata_one = DocumentMetadata(
    document_id="doc-002",
    title="RAG",
    source="book",
)

metadata_two = DocumentMetadata(
    document_id="doc-002",
    title="RAG",
    source="book",
)

print(metadata_one == metadata_two)


# AI-oriented example


@dataclass
class SearchResult:
    document_id: str
    content: str
    score: float
    metadata: dict = field(default_factory=dict)


result = SearchResult(
    document_id="doc-001",
    content="Python is useful for AI.",
    score=0.95,
    metadata={
        "source": "notes",
        "category": "python",
    },
)

print(result)
print(f"Similarity score: {result.score}")