from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, item_id, title, num_copies):
        self._item_id = item_id  # Encapsulation: Protected attribute for item ID
        self._title = title  # Encapsulation: Protected attribute for item title
        self._num_copies = num_copies  # Encapsulation: Protected attribute for number of copies

    @property
    def item_id(self):
        return self._item_id

    @property
    def title(self):
        return self._title

    @property
    def num_copies(self):
        return self._num_copies

    @num_copies.setter
    def num_copies(self, new_num_copies):
        self._num_copies = new_num_copies

    @abstractmethod
    def display_info(self):
        pass

class Book(LibraryItem):
    def __init__(self, item_id, title, num_copies, author):
        super().__init__(item_id, title, num_copies)
        self.author = author

    def display_info(self):
        print(f"Book ID: {self.item_id}, Title: {self.title}, Author: {self.author}, Copies Available: {self.num_copies}")

class Magazine(LibraryItem):
    def __init__(self, item_id, title, num_copies, issue_number):
        super().__init__(item_id, title, num_copies)
        self.issue_number = issue_number

    def display_info(self):
        print(f"Magazine ID: {self.item_id}, Title: {self.title}, Issue Number: {self.issue_number}, Copies Available: {self.num_copies}")

class Library:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.item_id] = item

    def remove_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]

    def checkout_item(self, item_id):
        if item_id in self.items and self.items[item_id].num_copies > 0:
            self.items[item_id].num_copies -= 1
            return True
        return False

    def return_item(self, item_id):
        if item_id in self.items:
            self.items[item_id].num_copies += 1
            return True
        return False

    def display_library_items(self):
        if not self.items:
            print("No items in the library.")
        else:
            print("Library Items:")
            for item in self.items.values():
                item.display_info()

# Example usage:
book_1 = Book(101, "Introduction to Python", 5, "John Doe")
book_2 = Book(102, "Data Science Handbook", 3, "Jane Smith")
magazine_1 = Magazine(201, "Tech Today", 10, "Issue #45")

library = Library()

library.add_item(book_1)
library.add_item(book_2)
library.add_item(magazine_1)

library.checkout_item(101)
library.checkout_item(201)
library.return_item(101)

library.display_library_items()


# Encapsulation:
# Explanation: Encapsulation is the principle of bundling data (attributes) and methods that operate on the data (behavior) within a single 
# unit, i.e., a class. In the Library Management System, we achieve encapsulation by using access control modifiers (_ prefix) to mark 
# attributes as protected and using getters and setters to control access to these attributes. The LibraryItem class encapsulates the item's ID,
#  title, and number of copies as protected attributes, while the subclasses (Book and Magazine) encapsulate their specific attributes 
# (author and issue_number) as protected attributes. This promotes data privacy, and external users can only access or modify these 
# attributes through controlled methods.

# Inheritance:
# Explanation: Inheritance is the mechanism in OOP that allows a class (subclass) to inherit properties and behaviors from another class 
# (superclass). In the Library Management System, we achieve inheritance by creating the subclasses Book and Magazine, which inherit 
# from the abstract class LibraryItem. The subclasses inherit the attributes (item_id, title, num_copies) and the abstract method 
# display_info() from the LibraryItem class. This promotes code reuse and allows creating different types of library items with specialized 
# behavior without duplicating code.

# Abstraction:
# Explanation: Abstraction is the process of defining a high-level interface for a class while hiding the underlying implementation details. 
# In the Library Management System, we achieve abstraction by creating the abstract class LibraryItem using the ABC module. The 
# LibraryItem class defines an abstract method display_info(), which serves as a template for displaying information about a library item. 
# The abstract method does not provide an implementation in the abstract class, leaving it to its concrete subclasses (Book and Magazine) 
# to implement it. This enforces that every concrete library item class must implement its own way of displaying information. 
# By providing a clear interface without specifying implementation details, abstraction allows us to work with library items without 
# concerning ourselves with how each item's information is displayed, promoting code flexibility, and ease of extension.

# Polymorphism:
# Explanation: Polymorphism is the ability of objects of different classes to be treated as objects of a common superclass and respond to 
# the same method calls. In the Library Management System, we achieve polymorphism by having both the Book and Magazine classes 
# implement the display_info() method to provide specific behavior for displaying information about a library item. Despite having 
# different implementations of display_info(), we can treat objects of both classes as objects of the common superclass LibraryItem. 
# This allows us to use a single interface (display_info()) to display information, regardless of the specific type of library item, promoting 
# code flexibility and simplifying client code that interacts with different library item types.