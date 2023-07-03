class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def display_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("Available Books:")
            for book in self.books:
                print(book)
                print("--------------------")

    def borrow_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                self.borrowed_books.append(book)
                print("Book borrowed successfully.")
                break
        else:
            print("Book not found.")

    def return_book(self, book_id):
        for book in self.borrowed_books:
            if book.book_id == book_id:
                self.borrowed_books.remove(book)
                self.books.append(book)
                print("Book returned successfully.")
                break
        else:
            print("Book not found.")

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book ID: {self.book_id}\nTitle: {self.title}\nAuthor: {self.author}"

def main():
    library = Library()

    while True:
        print("\n1. Add Book")
        print("2. Display Available Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            while True:
                book_id = input("Enter the Book ID: ")
                title = input("Enter the Title: ")
                author = input("Enter the Author: ")
                book = Book(book_id, title, author)
                library.add_book(book)

                add_more = input("Do you want to add more books? (yes/no): ")
                if add_more.lower() == "no":
                    break
                elif add_more.lower() != "yes":
                    print("Invalid choice. Adding more books stopped.")
                    break

        elif choice == "2":
            library.display_books()
        elif choice == "3":
            book_id = input("Enter the Book ID to borrow: ")
            library.borrow_book(book_id)
        elif choice == "4":
            book_id = input("Enter the Book ID to return: ")
            library.return_book(book_id)
        elif choice == "5":
            print("Thank you for using the Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
