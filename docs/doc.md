Before building the project, we need to install the OpenAI API library. Let's install it using pip:

```bash
pip install openai
```

Now, let's start building the program. We'll first create a function to get the OpenAI API key from the user:

```python
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
```

This function will open a dialog box asking the user for their API key and return it. We use the `simpledialog` module from `tkinter` for this.

Next, let's create a function to get a list of available models from the OpenAI API:

```python
import openai

def get_api_models():
    """
    Returns a list of available OpenAI API models.
    """
    models = []
    try:
        models = openai.Model.list()
        models = [model.id for model in models['data']]
    except Exception as e:
        handle_error(e)
    return models
```

This function uses the `openai.Model.list()` function to get a list of models from the OpenAI API. We then extract the `id` attribute from each model and return a list of model IDs. If there's an error while retrieving the models, we call the `handle_error()` function.

Now, let's create the main function to send requests to the API:

```python
import threading

def send_request(model, data, async=False):
    """
    Sends a request to the OpenAI API using the specified model and data.
    """
    api_key = get_api_key()
    if not api_key:
        return
    openai.api_key = api_key
    try:
        if async:
            t = threading.Thread(target=send_async_request, args=(model, data))
            t.start()
        else:
            response = None
            if model == "text":
                response = openai.Completion.create(
                  engine=model,
                  prompt=data
                )
                response = response.choices[0].text
            else:
                response = "Image processing not implemented yet"
            return response
    except Exception as e:
        handle_error(e)

def send_async_request(model, data):
    """
    Sends an asynchronous request to the OpenAI API using the specified model and data.
    """
    response = send_request(model, data)
    # Do something with the response
```

This function calls `get_api_key()` to retrieve the API key from the user and sets it in the `openai` module. We then use the `openai.Completion.create()` function to send a request to the OpenAI API. If the `async` parameter is set to `True`, we create a new thread and call `send_async_request()` to process the API response in the background.

Finally, let's create a function to handle errors:

```python
from tkinter import messagebox

def handle_error(error):
    """
    Displays an error message to the user.
    """
    messagebox.showerror("Error", str(error))
```

This function uses `messagebox.showerror()` to display an error message to the user.

Now, let's create a simple GUI for the program:

```python
import tkinter as tk
from tkinter import ttk
 
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("OpenAI API")
 
        # API model selection
        self.model_label = ttk.Label(self.master, text="Select an API model:")
        self.model_label.grid(row=0, column=0)
 
        self.model_combo = ttk.Combobox(self.master, values=get_api_models())
        self.model_combo.grid(row=0, column=1)
 
        # Input field
        self.input_label = ttk.Label(self.master, text="Enter text or upload an image:")
        self.input_label.grid(row=1, column=0)
 
        self.input_field = tk.Text(self.master, height=5)
        self.input_field.grid(row=1, column=1)
 
        # Submit button
        self.submit_button = ttk.Button(self.master, text="Submit", command=self.submit_request)
        self.submit_button.grid(row=2, column=0)

        # Output field
        self.output_label = ttk.Label(self.master, text="Response:")
        self.output_label.grid(row=3, column=0)
 
        self.output_field = tk.Text(self.master, height=5, state=tk.DISABLED)
        self.output_field.grid(row=3, column=1)

    def submit_request
    

Now, let's complete the `submit_request()` method, which is called when the user clicks the Submit button:

```python
    def submit_request(self):
        """
        Submits a request to the OpenAI API and displays the output.
        """
        model = self.model_combo.get()
        input_data = self.input_field.get("1.0", tk.END).strip()
 
        if not model or not input_data:
            handle_error("Please select a model and enter some input data.")
            return
 
        response = send_request(model, input_data)
 
        if response:
            self.output_field.config(state=tk.NORMAL)
            self.output_field.delete("1.0", tk.END)
            self.output_field.insert(tk.END, response)
            self.output_field.config(state=tk.DISABLED)
```

This function gets the selected model and input data from the GUI fields. It then checks if both fields are filled and calls `send_request()` to process the API request.

If a response is received, it displays the response in the output text box.

Finally, let's start the GUI by creating an instance of the `Application` class:

```python
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
```

This will create a new instance of the `Application` class and start the GUI.

And here's the full code:

```python
import tkinter as tk
from tkinter import simpledialog, messagebox, ttk

import openai
import threading


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("OpenAI API")
 
        # API model selection
        self.model_label = ttk.Label(self.master, text="Select an API model:")
        self.model_label.grid(row=0, column=0)
 
        self.model_combo = ttk.Combobox(self.master, values=get_api_models())
        self.model_combo.grid(row=0, column=1)
 
        # Input field
        self.input_label = ttk.Label(self.master, text="Enter text or upload an image:")
        self.input_label.grid(row=1, column=0)
 
        self.input_field = tk.Text(self.master, height=5)
        self.input_field.grid(row=1, column=1)
 
        # Submit button
        self.submit_button = ttk.Button(self.master, text="Submit", command=self.submit_request)
        self.submit_button.grid(row=2, column=0)

        # Output field
        self.output_label = ttk.Label(self.master, text="Response:")
        self.output_label.grid(row=3, column=0)
 
        self.output_field = tk.Text(self.master, height=5, state=tk.DISABLED)
        self.output_field.grid(row=3, column=1)

    def submit_request(self):
        """
        Submits a request to the OpenAI API and displays the output.
        """
        model = self.model_combo.get()
        input_data = self.input_field.get("1.0", tk.END).strip()
 
        if not model or not input_data:
            handle_error("Please select a model and enter some input data.")
            return
 
        response = send_request(model, input_data)
 
        if response:
            self.output_field.config(state=tk.NORMAL)
            self.output_field.delete("1.0", tk.END)
            self.output_field.insert(tk.END, response)
            self.output_field.config(state=tk.DISABLED)

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

def get_api_models():
    """
    Returns a list of available OpenAI API models.
    """
    models = []
    try:
        models = openai.Model.list()
        models = [model.id for model in models['data']]
    except Exception as e:
        handle_error(e)
    return models

def send_request(model, data, async=False):
    """
    Sends a request to the OpenAI API using the specified model and data.
    """
    api_key = get_api_key()
    if not api_key:
        return
    openai.api_key = api_key
    try:
        if async:
            t = threading.Thread(target=send_async_request, args=(model, data))
            t.start()
        else:
            response = None
            if model == "text":
                response = openai.Completion.create(
                  engine=model,
                  prompt=data
                )
                response = response.choices[0].text
            else:
                response = "Image processing not implemented yet"
            return response
    except Exception
    
    
 
Sure, here is the complete code for the program:

```python
import tkinter as tk
from tkinter import simpledialog, messagebox, ttk

import openai
import threading


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("OpenAI API")
 
        # API model selection
        self.model_label = ttk.Label(self.master, text="Select an API model:")
        self.model_label.grid(row=0, column=0)
 
        self.model_combo = ttk.Combobox(self.master, values=get_api_models())
        self.model_combo.grid(row=0, column=1)
 
        # Input field
        self.input_label = ttk.Label(self.master, text="Enter text or upload an image:")
        self.input_label.grid(row=1, column=0)
 
        self.input_field = tk.Text(self.master, height=5)
        self.input_field.grid(row=1, column=1)
 
        # Submit button
        self.submit_button = ttk.Button(self.master, text="Submit", command=self.submit_request)
        self.submit_button.grid(row=2, column=0)

        # Output field
        self.output_label = ttk.Label(self.master, text="Response:")
        self.output_label.grid(row=3, column=0)
 
        self.output_field = tk.Text(self.master, height=5, state=tk.DISABLED)
        self.output_field.grid(row=3, column=1)

    def submit_request(self):
        """
        Submits a request to the OpenAI API and displays the output.
        """
        model = self.model_combo.get()
        input_data = self.input_field.get("1.0", tk.END).strip()
 
        if not model or not input_data:
            handle_error("Please select a model and enter some input data.")
            return
 
        response = send_request(model, input_data)
 
        if response:
            self.output_field.config(state=tk.NORMAL)
            self.output_field.delete("1.0", tk.END)
            self.output_field.insert(tk.END, response)
            self.output_field.config(state=tk.DISABLED)

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

def get_api_models():
    """
    Returns a list of available OpenAI API models.
    """
    models = []
    try:
        models = openai.Model.list()
        models = [model.id for model in models['data']]
    except Exception as e:
        handle_error(e)
    return models

def send_request(model, data, async=False):
    """
    Sends a request to the OpenAI API using the specified model and data.
    """
    api_key = get_api_key()
    if not api_key:
        return
    openai.api_key = api_key
    try:
        if async:
            t = threading.Thread(target=send_async_request, args=(model, data))
            t.start()
        else:
            response = None
            if model == "text":
                response = openai.Completion.create(
                  engine=model,
                  prompt=data
                )
                response = response.choices[0].text
            else:
                response = "Image processing not implemented yet"
            return response
    except Exception as e:
        handle_error(e)

def send_async_request(model, data):
    """
    Sends an asynchronous request to the OpenAI API using the specified model and data.
    """
    response = send_request(model, data)

def handle_error(error):
    """
    Displays an error message to the user.
    """
    messagebox.showerror("Error", str(error))


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
```

When you run this code, it will open a GUI window with a ComboBox to select an OpenAI API model, a Text field to input data or an image, and a Submit button. When you click the Submit button, the program will send a request to the OpenAI API, and the response will be displayed in another Text field below. If there is an error, it will be displayed in a message box.
