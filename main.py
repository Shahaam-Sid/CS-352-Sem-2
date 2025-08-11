from vector2d import vector2d


a = vector2d(7.7, 8.0)
b = vector2d(-1.0, 2.0)
o = vector2d(0.0, 0.0)

    
    
print(f"Vector Coordinates for A: {a}")
print(f"Vector Coordinates for B: {b}")
print(f"Vector Coordinates for C: {o}")

print()

print(f"vector2d objects: ")
print(repr(a))
print(repr(b))
print(repr(o))

print()

print(f"Are A and O equal: {a == o}")

print()

print(f"A + B: {a + b}")
print(f"A - B: {a - b}")

print()

print(f"Multiply B by 2.5: {b * 2.5}")

print()

print(f"Magnitude of B: {abs(b)}")

print()

print(f"x coordinate of A: {a[0]}")
print(f"y coordinate of A: {a[1]}")