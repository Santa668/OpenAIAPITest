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
