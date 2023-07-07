import tkinter as tk
from tkinter import messagebox

class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = []

    def add_book(self, book):
        self.books.append(book)
        messagebox.showinfo("Book Added", "Book added successfully.")

    def display_books(self):
        if not self.books:
            messagebox.showinfo("No Books", "No books available.")
        else:
            book_list = "\n\n".join(str(book) for book in self.books)
            messagebox.showinfo("Available Books", book_list)

    def borrow_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                self.borrowed_books.append(book)
                messagebox.showinfo("Book Borrowed", "Book borrowed successfully.")
                break
        else:
            messagebox.showinfo("Book Not Found", "Book not found.")

    def return_book(self, book_id):
        for book in self.borrowed_books:
            if book.book_id == book_id:
                self.borrowed_books.remove(book)
                self.books.append(book)
                messagebox.showinfo("Book Returned", "Book returned successfully.")
                break
        else:
            messagebox.showinfo("Book Not Found", "Book not found.")

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book ID: {self.book_id}\nTitle: {self.title}\nAuthor: {self.author}"

def add_book(library, book_id_entry, title_entry, author_entry):
    book_id = book_id_entry.get()
    title = title_entry.get()
    author = author_entry.get()
    book = Book(book_id, title, author)
    library.add_book(book)

    # Clear the entry fields
    book_id_entry.delete(0, tk.END)
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)

def display_books(library):
    library.display_books()

def borrow_book(library, book_id_entry):
    book_id = book_id_entry.get()
    library.borrow_book(book_id)

    # Clear the entry field
    book_id_entry.delete(0, tk.END)

def return_book(library, book_id_entry):
    book_id = book_id_entry.get()
    library.return_book(book_id)

    # Clear the entry field
    book_id_entry.delete(0, tk.END)

def main():
    library = Library()

    # Create the main window
    root = tk.Tk()
    root.title("Library Management System")

    # Add Book Section
    add_frame = tk.Frame(root)
    add_frame.pack(pady=10)

    add_label = tk.Label(add_frame, text="Add Book")
    add_label.pack()

    book_id_label = tk.Label(add_frame, text="Book ID:")
    book_id_label.pack()

    book_id_entry = tk.Entry(add_frame)
    book_id_entry.pack()

    title_label = tk.Label(add_frame, text="Title:")
    title_label.pack()

    title_entry = tk.Entry(add_frame)
    title_entry.pack()

    author_label = tk.Label(add_frame, text="Author:")
    author_label.pack()

    author_entry = tk.Entry(add_frame)
    author_entry.pack()

    add_button = tk.Button(add_frame, text="Add Book",
                           command=lambda: add_book(library, book_id_entry, title_entry, author_entry))
    add_button.pack(pady=10)

    # Display Books Section
    display_frame = tk.Frame(root)
    display_frame.pack(pady=10)

    display_label = tk.Label(display_frame, text="Display Available Books")
    display_label.pack()

    display_button = tk.Button(display_frame, text="Display Books",
                               command=lambda: display_books(library))
    display_button.pack()

    # Borrow Book Section
    borrow_frame = tk.Frame(root)
    borrow_frame.pack(pady=10)

    borrow_label = tk.Label(borrow_frame, text="Borrow Book")
    borrow_label.pack()

    borrow_id_label = tk.Label(borrow_frame, text="Book ID:")
    borrow_id_label.pack()

    borrow_id_entry = tk.Entry(borrow_frame)
    borrow_id_entry.pack()

    borrow_button = tk.Button(borrow_frame, text="Borrow Book",
                              command=lambda: borrow_book(library, borrow_id_entry))
    borrow_button.pack(pady=10)

    # Return Book Section
    return_frame = tk.Frame(root)
    return_frame.pack(pady=10)

    return_label = tk.Label(return_frame, text="Return Book")
    return_label.pack()

    return_id_label = tk.Label(return_frame, text="Book ID:")
    return_id_label.pack()

    return_id_entry = tk.Entry(return_frame)
    return_id_entry.pack()

    return_button = tk.Button(return_frame, text="Return Book",
                              command=lambda: return_book(library, return_id_entry))
    return_button.pack(pady=10)

    # Quit Button
    def quit_app():
        root.destroy()
        messagebox.showinfo("Thank You", "Thank you for using the Library Management System.")

    quit_button = tk.Button(root, text="Quit", command=quit_app)
    quit_button.pack(pady=10)

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()
