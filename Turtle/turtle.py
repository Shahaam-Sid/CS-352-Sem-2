from geometry.Pen import Pen


class Turtle:
    """
    A simplified Turtle graphics class that uses a Pen to draw on a canvas.
    
    The Turtle maintains its current position through the Pen object and
    supports movement in four directions:
      - forward  (upward)
      - backward (downward)
      - left     (towards decreasing x)
      - right    (towards increasing x)
    
    Each movement is restricted by boundary checks so that the Turtle
    does not move outside the canvas limits.
    """

    def __init__(self, canvas):
        # Turtle uses a Pen to actually draw on the canvas
        self.pen = Pen(canvas)

    # Getter for current position of the turtle (delegated to Pen)
    @property
    def current_position(self):
        return self.pen.current_pos

    # Move the turtle forward (upwards) by 20 units,
    # but only if it will not go out of the canvas boundary
    def forward(self):
        if self.current_position.y > 15:  # boundary check
            self.pen.line_to(
                self.current_position.x, self.current_position.y - 20
            )  # draw a line to new point

    # Move the turtle backward (downwards) by 20 units,
    # but only if it stays inside the canvas boundary
    def backward(self):
        if self.current_position.y < 395:  # boundary check
            self.pen.line_to(self.current_position.x, self.current_position.y + 20)

    # Move the turtle left (x decreases) by 20 units,
    # only if it does not cross the left boundary
    def left(self):
        if self.current_position.x > 5:  # boundary check
            self.pen.line_to(self.current_position.x - 20, self.current_position.y)

    # Move the turtle right (x increases) by 20 units,
    # only if it does not cross the right boundary
    def right(self):
        if self.current_position.x < 385:  # boundary check
            self.pen.line_to(self.current_position.x + 20, self.current_position.y)
