import re
import tkinter as tk
from tkinter import filedialog, messagebox


root = tk.Tk()
root.title("Email Extractor")
root.geometry("700x200")
root.configure(bg="lightblue") 
root.resizable(False, False)

def extract_emails_from_file(input_file_path, output_file_path):
    try:
        
        with open(input_file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_pattern, content)

       
        unique_emails = sorted(set(emails))

        
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            for email in unique_emails:
                output_file.write(email + '\n')

        messagebox.showinfo("Success", f"{len(unique_emails)} emails saved to:\n{output_file_path}")

    except FileNotFoundError:
        messagebox.showerror("Error", f"File not found: {input_file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{str(e)}")

def browse_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, file_path)

def browse_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt")])
    output_entry.delete(0, tk.END)
    output_entry.insert(0, file_path)

def run_extraction():
    input_file = input_entry.get()
    output_file = output_entry.get()
    if not input_file or not output_file:
        messagebox.showwarning("Missing Info", "Please select both input and output files.")
        return
    extract_emails_from_file(input_file, output_file)



# Input File
tk.Label(root, text="Input .txt File:").pack(pady=(10, 0))
input_frame = tk.Frame(root)
input_frame.pack(padx=10)
input_entry = tk.Entry(input_frame, width=50)
input_entry.pack(side=tk.LEFT)
tk.Button(input_frame, text="Browse", command=browse_input_file).pack(side=tk.LEFT, padx=5)

# Output File
tk.Label(root, text="Output File (to save emails):").pack(pady=(10, 0))
output_frame = tk.Frame(root)
output_frame.pack(padx=10)
output_entry = tk.Entry(output_frame, width=50)
output_entry.pack(side=tk.LEFT)
tk.Button(output_frame, text="Browse", command=browse_output_file).pack(side=tk.LEFT, padx=5)

# Extract Button
tk.Button(root, text="Extract Emails", command=run_extraction, bg="#4CAF50", fg="white").pack(pady=20)


root.mainloop()
