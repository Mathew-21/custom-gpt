import tkinter as tk
from tkinter import scrolledtext
import subprocess

# Function to run the Mistral model with a prompt
def run_mistral():
    prompt = input_text.get("1.0", "end-1c")  # Get input from the text box
    result_output.delete('1.0', tk.END)  # Clear previous output
    
    try:
        # Run the command to query the Mistral model through Ollama
        result = subprocess.run(
            ["ollama", "run", "mistral", prompt],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8', errors='ignore', shell=True
        )
        output = result.stdout
    except Exception as e:
        output = f"Error running model: {e}"

    result_output.insert(tk.END, output)  # Display output
# Initialize the main window
app = tk.Tk()
app.title("Mistral Model UI")
app.geometry('600x400')

# Add a label and text box for input
tk.Label(app, text="Enter your prompt:").pack(pady=10)
input_text = tk.Text(app, height=5, width=70)
input_text.pack(pady=10)

# Add a button to trigger the model
run_button = tk.Button(app, text="Run Mistral", command=run_mistral)
run_button.pack(pady=10)

# Add a scrollable text area to display the output
result_output = scrolledtext.ScrolledText(app, height=10, width=70)
result_output.pack(pady=10)

# Start the main event loop
app.mainloop()
