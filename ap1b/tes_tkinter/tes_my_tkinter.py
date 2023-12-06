import tkinter as tk

def on_button_click():
    label.config(text="Hello, " + entry.get())

# Create the main window
root = tk.Tk()
root.title("Tkinter Example")

# Create and pack a label
label = tk.Label(root, text="Enter your name:")
label.pack(pady=10)

# Create and pack an entry widget
entry = tk.Entry(root)
entry.pack(pady=10)

# Create and pack a button
button = tk.Button(root, text="Submit", command=on_button_click)
button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
