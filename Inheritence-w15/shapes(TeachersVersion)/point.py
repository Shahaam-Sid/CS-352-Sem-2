import math


class Point:
    """Represents a 2D point with encapsulated coordinates."""
    
    def __init__(self, x=0.0, y=0.0):
        self.__x = float(x)
        self.__y = float(y)
    
    # --- Property for x ---
    @property
    def x(self):
        """Get the x-coordinate."""
        return self.__x
    
    @x.setter
    def x(self, value):
        """Set the x-coordinate (must be numeric)."""
        if not isinstance(value, (int, float)):
            raise TypeError("x-coordinate must be numeric.")
        self.__x = float(value)
    
    # --- Property for y ---
    @property
    def y(self):
        """Get the y-coordinate."""
        return self.__y
    
    @y.setter
    def y(self, value):
        """Set the y-coordinate (must be numeric)."""
        if not isinstance(value, (int, float)):
            raise TypeError("y-coordinate must be numeric.")
        self.__y = float(value)
    
    # --- Distance method ---
    def distance_to(self, other):
        """Compute Euclidean distance to another Point."""
        if not isinstance(other, Point):
            raise TypeError("distance_to() expects a Point instance.")
        return math.hypot(self.x - other.x, self.y - other.y)
    
    # --- String representations ---
    def __repr__(self):
        """Unambiguous representation for debugging."""
        return f"Point(x={self.x:.2f}, y={self.y:.2f})"
    
    def __str__(self):
        """Readable representation for users."""
        return f"({self.x:.2f}, {self.y:.2f})"
    
    # --- Equality check ---
    def __eq__(self, other):
        """Compare two points for equality."""
        return (
            isinstance(other, Point)
            and math.isclose(self.x, other.x)
            and math.isclose(self.y, other.y)
        )