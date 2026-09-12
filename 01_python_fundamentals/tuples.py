"""
Python tuple examples.

Topics:
- Tuple creation
- Indexing
- Immutability
- Unpacking
"""

coordinates = (17.4948, 78.3996)

print("Coordinates:", coordinates)
print("Latitude:", coordinates[0])
print("Longitude:", coordinates[1])

latitude, longitude = coordinates

print("Latitude:", latitude)
print("Longitude:", longitude)

# Tuples are immutable.
# The following line would raise a TypeError:
#
# coordinates[0] = 20.0