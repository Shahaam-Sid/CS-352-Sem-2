from triangles import Triangles

a = Triangles()
b = Triangles(2.0)
c = Triangles(4, 3, 5)
d = Triangles(b)

collection = [a, b, c, d]

for item in collection:
    print(item)
    print(f"is Triangle Right Angled: {item.isHypotenuse()}")
    print(f"Perimeter: {item.perimeter()}")
    print()


print(f"# of Traingles: {Triangles.counter()}")