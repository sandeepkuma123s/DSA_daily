# a class represent 3d vector with  to caluculate the vectors  magnitude and add two vectors

import math
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def add(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
# Example usage
v1 = Vector3D(1, 2, 3)      
v2 = Vector3D(4, 5, 6)
v3 = v1.add(v2)
print(f"Vector v1: ({v1.x}, {v1.y}, {v1.z})")
print(f"Vector v2: ({v2.x}, {v2.y}, {v2.z})")
print(f"Vector v3 (v1 + v2): ({v3.x}, {
v3.y}, {v3.z})")
print(f"Magnitude of v1: {v1.magnitude()}")     
print(f"Magnitude of v2: {v2.magnitude()}")
print(f"Magnitude of v1: {v1.magnitude()}")     
print(f"Magnitude of v2: {v2.magnitude()}")     
print(f"Magnitude of v3: {v3.magnitude()}")
print(f"Magnitude of v3: {v3.magnitude()}")

print(f"Magnitude of v3: {v3.magnitude()}")
    