from tkinter import messagebox

def handle_error(error):
    """
    Displays an error message to the user.
    """
    messagebox.showerror("Error", str(error))
