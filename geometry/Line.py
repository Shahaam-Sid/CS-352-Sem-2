from geometry.Point import Point

class Line:
    def __init__(self, start_point, end_point):
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
        
    