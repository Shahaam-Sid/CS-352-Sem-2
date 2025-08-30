from Point import Point

class Line:
    """
    Creates Lines from Two Point, from Point Class
    """
    def __init__(self, start_point, end_point):
        """
        Takes start_point and end_point as Arguments(uses Point class)
        Creates a Line

        Args:
            start_point (Point): point from where line starts
            end_point (Point): point from where line ends
        """
        self.start_point = start_point
        self.end_point = end_point
        
    @property
    def start_point(self):
        return self._start_point
    
    @property
    def end_point(self):
        return self._end_point
    
    @start_point.setter
    def start_point(self, value):
        if not isinstance(value, Point):
            raise TypeError("Starting Point must be a Point Object")
        
        self._start_point = value
        
    @end_point.setter
    def end_point(self, value):
        if not isinstance(value, Point):
            raise TypeError("End Point must be a Point Object")
        
        self._end_point = value
        
    def length(self):
        """
        Calculates the lenght of line
        
        Returns:
            float
        """
        return self.start_point.distance(self.end_point)
    
    def __str__(self):
        return f"Line from {self.start_point} to {self.end_point}"
