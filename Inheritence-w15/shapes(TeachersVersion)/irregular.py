from shapeInterace import Polygon

class IrregularPolygon(Polygon):
    """A polygon defined by arbitrary vertices (Point objects or (x, y) tuples)."""
    
    def __init__(self, vertices):
        """
        Accepts either:
        - A list of Point objects, or 
        - A list of (x, y) coordinate tuples.
        Normalization to Point objects is handled by Polygon.
        """
        super().__init__(vertices)  # parent handles normalization
    
    def area(self):
        """
        Compute the polygon's area using the Shoelace theorem:
        A = 1/2 * |Σ (x_i*y_{i+1} - y_i*x_{i+1})|
        """
        n = self.n
        x = [p.x for p in self.vertices]
        y = [p.y for p in self.vertices]
        return 0.5 * abs(
            sum(x[i] * y[(i + 1) % n] - y[i] * x[(i + 1) % n] for i in range(n))
        )
    
    def __str__(self):
        """Readable summary for display or polymorphism demo."""
        return (
            f"IrregularPolygon with {self.n} vertices, "
            f"Perimeter={self.perimeter():.2f}, "
            f"Area={self.area():.2f}"
        )