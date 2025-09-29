import tkinter as tk

class TkPanel(tk.Canvas):
    """
    A custom Tkinter Canvas widget that allows drawing and clearing lines.
    
    Features:
    - Inherits from tk.Canvas.
    - Provides a "Clear" button at the top-right corner to clear all drawings.
    - Keeps track of drawn lines for reference.
    
    Attributes
    ----------
    lines : list
        A list storing all line objects that have been drawn on the canvas.
    my_button : tk.Button
        A button widget to clear the canvas when clicked.
    """

    def __init__(self, master=None, h=400, w=400):
        """
        Initialize the TkPanel (custom canvas).
        
        Parameters
        ----------
        master : tk.Widget, optional
            The parent widget (e.g., a Tk window or frame). Default is None.
        h : int, optional
            Height of the canvas. Default is 400.
        w : int, optional
            Width of the canvas. Default is 400.
        """
        # Initialize a Tkinter Canvas with the given height and width
        super().__init__(master, height=h, width=w)
        
        # Create a "Clear" button on the master widget (not inside the canvas)
        self.my_button = tk.Button(
            master,
            bg="brown",
            font=("Arial", 10, "bold"),
            fg="white",
            text="Clear",
            command=self.clear_window,  # Button action clears the canvas
        )
        
        # Position the button at the top-right of the parent container
        self.my_button.pack(side="top", anchor="ne")
        
        # Store drawn line objects (so we can track them logically)
        self.lines = []
        
    def add_line(self, line):
        """
        Add a new line object to the canvas and draw it.
        
        Parameters
        ----------
        line : object
            A line object with start_point and end_point attributes,
            where each point has `x` and `y` coordinates.
        """
        self.lines.append(line)   # Keep record of the line
        self.draw(line)           # Draw it visually on the canvas

    def draw(self, line):
        """
        Draw a line on the canvas using Tkinter's create_line method.
        
        Parameters
        ----------
        line : object
            A line object with start_point and end_point attributes.
        """
        self.create_line(
            line.start_point.x, line.start_point.y,   # Starting point
            line.end_point.x, line.end_point.y        # Ending point
        )

    def clear_window(self):
        """
        Clear all drawings from the canvas and reset stored lines.
        """
        self.delete("all")  # Remove everything from the canvas
        self.lines = []     # Reset the internal list of drawn lines
