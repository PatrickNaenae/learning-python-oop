class Book:
    def __init__(self, book_id, title, author, available_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available_copies = available_copies

    def __str__(self):
        return f"{self.title} by {self.author}"

    def borrow(self):
        if self.available_copies  > 0:
            self.available_copies -= 1
            return True
        else:
            return False

    def return_book(self):
        self.available_copies += 1


class LibraryMember:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

    def __str__(self):
        return self.name

class Library:
    def __init__(self ):
        self.books = []
        self.members = []

    def add_books(self, book):
        self.books.append(book)

    def add_members(self, member):
        self.members.append(member)

    def borrow_book(self, member, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.borrow():
                    print(f"{member.name} borrowed {book.title}.")
                else:
                    print(f"Sorry, {book.title} is currently unavailable.")

    def return_book(self, member, book_id):
        for book in self.books:
            if book.book_id == book_id:
                book.return_book()
                print(f"{member.name} returned {book.title}.")


# Example usage:
book1 = Book(101, "The Alchemist", "Paulo Coelho", 1)
book2 = Book(102, "To Kill a Mockingbird", "Harper Lee", 2)

member1 = LibraryMember(201, "John")
member2 = LibraryMember(202, "Peter")

library = Library()
library.add_books(book1)
library.add_books(book2)
library.add_members(member1)
library.add_members(member2)

library.borrow_book(member1, 101)  # John borrowed The Alchemist.
library.borrow_book(member2, 101)  # Sorry, The Alchemist is currently unavailable..
library.borrow_book(member2, 102)  # Peter  borrowed To Kill a Mockingbird.

library.return_book(member2, 102)  # peter returned To Kill a Mockingbird.

for book in library.books:
    print(book)

for member in library.members:
    print(member)