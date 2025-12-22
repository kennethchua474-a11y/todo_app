import tkinter as tk
from tkinter import messagebox

from todo_app.core import TodoList


class TodoApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Todo App")

        self.todo = TodoList()

        # Listbox
        self.listbox = tk.Listbox(root, width=40, height=10)
        self.listbox.pack(pady=10)

        # Entry
        self.entry = tk.Entry(root, width=40)
        self.entry.pack()

        # Button Frame
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        add_btn = tk.Button(btn_frame, text="Add", command=self.add_item)
        add_btn.grid(row=0, column=0, padx=5)

        delete_btn = tk.Button(btn_frame, text="Delete", command=self.delete_item)
        delete_btn.grid(row=0, column=1, padx=5)

        save_btn = tk.Button(btn_frame, text="Save", command=self.save_items)
        save_btn.grid(row=0, column=2, padx=5)

    def refresh_listbox(self) -> None:
        self.listbox.delete(0, tk.END)
        for item in self.todo.items:
            self.listbox.insert(tk.END, item)

    def add_item(self) -> None:
        text = self.entry.get()
        self.todo.add_item(text)
        self.entry.delete(0, tk.END)
        self.refresh_listbox()

    def delete_item(self) -> None:
        selection = self.listbox.curselection()  # type: ignore[no-untyped-call]
        if not selection:
            messagebox.showwarning("Warning", "No item selected")
            return

        self.todo.delete_item(selection[0])
        self.refresh_listbox()

    def save_items(self) -> None:
        self.todo.save("todo_items.txt")
        messagebox.showinfo("Saved", "Todo list saved!")


def run() -> None:
    root = tk.Tk()
    TodoApp(root)
    root.mainloop()


if __name__ == "__main__":
    run()
