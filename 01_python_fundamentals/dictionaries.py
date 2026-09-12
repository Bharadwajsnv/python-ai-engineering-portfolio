"""
Python dictionary examples.

Topics:
- Key-value pairs
- Accessing values
- Updating values
- get()
- items()
- keys()
- values()
"""

employee = {
    "name": "Bharadwaj",
    "role": "Software Engineer",
    "skills": ["Java", "Python", "AI Engineering"],
}

print(employee)
print(employee["name"])
print(employee["role"])

employee["role"] = "AI Engineer"
employee["experience"] = 5

print(employee)

print(employee.get("location", "Location not provided"))

for key, value in employee.items():
    print(key, ":", value)