class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        self.is_borrowed = True
        print(f"'{self.title}' has been marked as borrowed.")

    def mark_as_returned(self):
        self.is_borrowed = False
        print(f"'{self.title}' has been marked as returned.")

    def __str__(self):
        return f"{self.title} by {self.author}"


class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is currently borrowed by someone else.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned '{book.title}'.")
        else:
            print(f"{self.name} has not borrowed '{book.title}'.")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f"- {book}")
        else:
            print(f"{self.name} has not borrowed any books.")


def main():
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

    member = LibraryMember("Alice", "M001")

    books = [book1, book2, book3]

    while True:
        print("\nLibrary Menu:")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. List borrowed books")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            print("\nAvailable books:")
            for idx, book in enumerate(books):
                if not book.is_borrowed:
                    print(f"{idx + 1}. {book}")
            selected = int(input("Enter the number of the book to borrow: ")) - 1
            if 0 <= selected < len(books):
                member.borrow_book(books[selected])
            else:
                print("Invalid selection.")

        elif choice == '2':
            if member.borrowed_books:
                print("\nYour borrowed books:")
                for idx, book in enumerate(member.borrowed_books):
                    print(f"{idx + 1}. {book}")
                selected = int(input("Enter the number of the book to return: ")) - 1
                if 0 <= selected < len(member.borrowed_books):
                    member.return_book(member.borrowed_books[selected])
                else:
                    print("Invalid selection.")
            else:
                print("You haven't borrowed any book")

        elif choice == '3':
            member.list_borrowed_books()

        elif choice == '4':
            print("Okay")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
