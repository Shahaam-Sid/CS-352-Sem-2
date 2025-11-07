import copy
from point import Point

class Line:
    """Represents a line segment defined by two Point objects."""
    
    def __init__(self, start_point, end_point):
        if not all(isinstance(p, Point) for p in (start_point, end_point)):
            raise TypeError("Line endpoints must be Point objects.")
        self.start = start_point
        self.end = end_point
    
    @property
    def length(self):
        """Length computed via composed Point objects."""
        return self.start.distance_to(self.end)
    
    def __eq__(self, other):
        """Two lines are equal if both endpoints match (in any order)."""
        return isinstance(other, Line) and (
            (self.start == other.start and self.end == other.end)
            or (self.start == other.end and self.end == other.start)
        )
    
    def __repr__(self):
        return f"Line(start={self.start}, end={self.end}, length={self.length:.2f})"
