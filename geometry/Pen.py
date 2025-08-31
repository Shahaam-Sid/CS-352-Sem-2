from geometry.Line import Line
from geometry.Point import Point

class Pen:
    """
    A Pen class that simulates a drawing tool for a canvas.

    The Pen maintains its current position as a Point object and can:
    - Move to a new position without drawing.
    - Draw a line from its current position to a new position.
    
    Attributes
    ----------
    _current_pos : Point
        The current position of the pen represented as a Point object.
    canvas : object
        The drawing surface (e.g., TkPanel) where lines are drawn.
    """

    def __init__(self, canvas):
        """
        Initialize the Pen object with a starting position and a canvas.

        Parameters
        ----------
        canvas : object
            A drawing surface that supports the method `add_line(line)`.
        """
        # Pen starts at coordinates (25, 195)
        self._current_pos = Point(25, 195)

        # Canvas object (responsible for rendering lines)
        self.canvas = canvas

    @property
    def current_pos(self):
        """
        Get the current position of the pen.

        Returns
        -------
        Point
            The current position of the pen.
        """
        return self._current_pos

    @current_pos.setter
    def current_pos(self, updated):
        """
        Update the current position of the pen.

        Parameters
        ----------
        updated : Point
            The new position to set as the pen's current position.
        """
        self._current_pos = updated

    def move_to(self, x, y):
        """
        Move the pen to a new position without drawing a line.

        Parameters
        ----------
        x : int or float
            The new x-coordinate.
        y : int or float
            The new y-coordinate.
        """
        self._current_pos = Point(x, y)

    def line_to(self, x, y):
        """
        Draw a line from the current position to a new position.

        Parameters
        ----------
        x : int or float
            The x-coordinate of the new point.
        y : int or float
            The y-coordinate of the new point.
        """
        # Create the endpoint of the line
        end_point = Point(x, y)

        # Create a line object from the current position to the new endpoint
        line = Line(self._current_pos, end_point)

        # Instruct the canvas to render this line
        self.canvas.add_line(line)

        # Update the pen's current position to the endpoint
        self._current_pos = end_point