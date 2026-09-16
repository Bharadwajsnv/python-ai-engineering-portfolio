import numpy as np


def cosine_similarity(vector_a, vector_b):
    """
    Calculate cosine similarity between two vectors.
    """

    magnitude_a = np.linalg.norm(vector_a)
    magnitude_b = np.linalg.norm(vector_b)

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    return np.dot(vector_a, vector_b) / (
        magnitude_a * magnitude_b
    )


# Simulated embedding for the user query
query_embedding = np.array([0.9, 0.8, 0.1, 0.2])


# Simulated document embeddings
documents = {
    "Python programming document": np.array([0.8, 0.7, 0.2, 0.1]),
    "Machine learning document": np.array([0.7, 0.8, 0.3, 0.2]),
    "Cooking recipes document": np.array([0.1, 0.2, 0.9, 0.8]),
}


similarities = []

for document_name, document_embedding in documents.items():
    similarity = cosine_similarity(
        query_embedding,
        document_embedding
    )

    similarities.append((document_name, similarity))


# Sort documents by similarity score
similarities.sort(
    key=lambda item: item[1],
    reverse=True
)


print("Query embedding:")
print(query_embedding)

print("\nDocument similarity scores:")

for document_name, score in similarities:
    print(f"{document_name}: {score:.4f}")


print("\nMost relevant document:")
print(similarities[0][0])