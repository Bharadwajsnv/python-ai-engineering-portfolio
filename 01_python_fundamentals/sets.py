"""
Python set examples.

Topics:
- Unique values
- Adding values
- Removing values
- Union
- Intersection
"""

skills = {"Python", "Java", "Python", "AI"}

print("Unique skills:", skills)

skills.add("FastAPI")
print(skills)

other_skills = {"AI", "PyTorch", "FastAPI"}

print("Union:", skills | other_skills)
print("Intersection:", skills & other_skills)