"""
Examples of while loops.
"""

counter = 1

while counter <= 5:
    print("Counter:", counter)
    counter += 1


# Practical retry-style example

attempt = 1
max_attempts = 3

while attempt <= max_attempts:
    print("Processing attempt:", attempt)
    attempt += 1

print("Processing finished")