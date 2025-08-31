from app.app import App


def main():
    # Create an instance of App (your Tkinter GUI application)
    app = App()

    # Run the application (starts the Tkinter main event loop)
    app.run()


# This ensures that the code below only runs when main.py is executed directly,
# and not when it is imported as a module in another file.
if __name__ == "__main__":
    main()