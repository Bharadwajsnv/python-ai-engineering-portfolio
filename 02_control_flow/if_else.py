"""
Examples of if, elif, and else.
"""

score = 85

if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "Needs Improvement"

print("Score:", score)
print("Grade:", grade)


# Practical AI-related example

document_type = "pdf"

if document_type == "pdf":
    print("Process PDF document")
elif document_type == "txt":
    print("Process text document")
elif document_type == "json":
    print("Process JSON document")
else:
    print("Unsupported document type")