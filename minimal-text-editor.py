import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Minimalist Text Editor")
        self.master.geometry("600x400")

        self.text = tk.Text(self.master, undo=True)
        self.text.pack(expand=True, fill=tk.BOTH)

        menubar = tk.Menu(self.master)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New (Ctrl+N)", command=self.new_file)
        filemenu.add_command(label="Open (Ctrl+O)", command=self.open_file)
        filemenu.add_command(label="Save (Ctrl+S)", command=self.save_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit (Ctrl+Q)", command=self.master.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        self.text.bind('<Control-n>', self.new_file)
        self.text.bind('<Control-N>', self.new_file)
        self.text.bind('<Control-o>', self.open_file)
        self.text.bind('<Control-O>', self.open_file)
        self.text.bind('<Control-s>', self.save_file)
        self.text.bind('<Control-S>', self.save_file)
        self.text.bind('<Control-q>', self.master.quit)
        self.text.bind('<Control-Q>', self.master.quit)

        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Cut (Ctrl+X)", command=self.cut)
        editmenu.add_command(label="Copy (Ctrl+C)", command=self.copy)
        editmenu.add_command(label="Paste (Ctrl+V)", command=self.paste)
        editmenu.add_separator()
        editmenu.add_command(label="Select All (Ctrl+A)", command=self.select_all)
        editmenu.add_command(label="Undo (Ctrl+Z)", command=self.paste)
        editmenu.add_command(label="Redo (Ctrl+Y)", command=self.paste)
        menubar.add_cascade(label="Edit", menu=editmenu)

        self.text.bind('<Control-x>', self.cut)
        self.text.bind('<Control-X>', self.cut)
        self.text.bind('<Control-c>', self.copy)
        self.text.bind('<Control-C>', self.copy)
        self.text.bind('<Control-v>', self.paste)
        self.text.bind('<Control-V>', self.paste)
        self.text.bind('<Control-a>', self.select_all)
        self.text.bind('<Control-A>', self.select_all)

        self.master.config(menu=menubar)

    def new_file(self, event):
        self.text.delete('1.0', tk.END)

    def open_file(self, event):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'r') as f:
                file_content = f.read()
            self.text.delete('1.0', tk.END)
            self.text.insert(tk.END, file_content)

    def save_file(self, event):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'w') as f:
                f.write(self.text.get('1.0', tk.END))

    def cut(self, event):
        self.text.event_generate("<<Cut>>")

    def copy(self, event):
        self.text.event_generate("<<Copy>>")

    def paste(self, event):
        self.text.event_generate("<<Paste>>")

    def select_all(self, event):
        self.text.tag_add('sel', '1.0', 'end')
        return "break"

if __name__ == "__main__":
    root = tk.Tk()
    text_editor = TextEditor(root)
    root.mainloop()