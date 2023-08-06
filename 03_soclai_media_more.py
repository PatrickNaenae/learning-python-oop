from abc import ABC, abstractmethod

class User(ABC):  # Inherit ABC class to make User an abstract class - Abstraction
    def __init__(self, user_id, username, email, password):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.__password = password  # Encapsulation: Private attribute

    @property  # Abstraction: Property getter for password attribute
    def password(self):
        return "********"  # Encapsulation: Property getter returns a masked password

    @abstractmethod  # Abstraction: Abstract method for creating a post
    def create_post(self, content):
        pass

    @abstractmethod  # Abstraction: Abstract method for creating a comment
    def create_comment(self, post, text):
        pass

    def __str__(self):
        return f"{self.username} (User ID: {self.user_id})"


class Post:
    def __init__(self, post_id, author, content):
        self.post_id = post_id
        self.author = author
        self.content = content

    def __str__(self):
        return f"Post {self.post_id} by {self.author}: {self.content}"


class Comment:
    def __init__(self, comment_id, author, text):
        self.comment_id = comment_id
        self.author = author
        self.text = text

    def __str__(self):
        return f"Comment {self.comment_id} by {self.author}: {self.text}"


class RegularUser(User):
    def __init__(self, user_id, username, email, password):
        super().__init__(user_id, username, email, password)

    def create_post(self, content):  # Polymorphism
        return Post(post_id=1, author=self.username, content=content)

    def create_comment(self, post, text):  # Polymorphism
        return Comment(comment_id=1, author=self.username, text=text)


class AdminUser(User):
    def __init__(self, user_id, username, email, password):
        super().__init__(user_id, username, email, password)

    def create_post(self, content):  # Polymorphism
        return Post(post_id=1, author=self.username.upper(), content=content)

    def create_comment(self, post, text):  # Polymorphism
        return Comment(comment_id=1, author=self.username.upper(), text=text)


# Example usage: (Unchanged)
regular_user = RegularUser(101, "john_doe", "john@example.com", "password123")
admin_user = AdminUser(201, "admin123", "admin@example.com", "adminpass")

# Creating posts and comments
post_1 = regular_user.create_post("Hello, everyone! This is my first post.")
comment_1 = regular_user.create_comment(post_1, "Nice post!")

post_2 = admin_user.create_post("Greetings from the admin!")
comment_2 = admin_user.create_comment(post_2, "Admin power!")

# Displaying posts and comments
print(post_1)
print(comment_1)

print(post_2)
print(comment_2)


# Encapsulation: The User class has a private attribute __password, which is encapsulated and hidden from direct access outside the class. 
# The @property decorator allows access to the password attribute through a getter method, providing a controlled way to retrieve the password.

# Abstraction: The User class is an abstract class with abstract methods create_post and create_comment. 
# It defines a common interface for all users but leaves the implementation details to its subclasses.

# Inheritance: The RegularUser and AdminUser classes inherit from the User class, inheriting its attributes and methods.

# Polymorphism: Both RegularUser and AdminUser classes override the create_post and create_comment methods to provide specific 
# behavior for regular users and admin users, respectively. This demonstrates polymorphism by allowing different user types to have 
# their own implementation of the same methods with different behaviors.