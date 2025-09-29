import tkinter as tk
from canvas.Canvas import TkPanel
from Turtle.turtle import Turtle


class App:
    """
    Main application class for running a simple Turtle Graphics program
    using Tkinter.
    
    Features:
      - Creates a window with a drawing canvas (TkPanel).
      - Initializes a Turtle that can move and draw.
      - Supports keyboard controls:
          * Arrow Up    → move forward
          * Arrow Down  → move backward
          * Arrow Left  → move left
          * Arrow Right → move right
      - Runs an event loop to keep the app interactive.
    """

    def __init__(self, title="Default", height=400, width=400):
        # Create main Tkinter window
        self.window = tk.Tk()

        # Create a TkPanel (canvas) where Turtle will draw
        self.canvas = TkPanel(self.window, height, width)
        self.canvas.pack()  # place the canvas in the window

        # Set the window title
        self.window.title(title)

        # Placeholder for Turtle instance (initialized in run)
        self.turtle = None

        # Bind key press events to control turtle with arrow keys
        self.window.bind("<Key>", self.key_press)

    def key_press(self, event):
        """
        Handle key press events for turtle movement.
        Maps arrow keys to turtle movement methods.
        """
        key = event.keysym  # identify which key was pressed
        if key == "Up":
            self.turtle.forward()
        elif key == "Down":
            self.turtle.backward()
        elif key == "Left":
            self.turtle.left()
        elif key == "Right":
            self.turtle.right()

    def run(self):
        """
        Start the application:
        - Create a Turtle bound to the canvas.
        - Enter the Tkinter event loop to keep the app running.
        """
        turtle = Turtle(self.canvas)  # create turtle object
        self.turtle = turtle          # store it for movement
        self.window.mainloop()        # start Tkinter event loop
