from tkinter import simpledialog

def get_api_key():
    """
    Prompts the user for their OpenAI API key and returns it.
    """
    root = tk.Tk()
    root.withdraw()
    api_key = simpledialog.askstring(
        "API Key",
        "Enter your OpenAI API key:"
    )
    return api_key
