from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_id, name, price):
        self._product_id = product_id
        self._name = name
        self._price = price

    @property
    def product_id(self):
        return self._product_id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @abstractmethod
    def calculate_total(self, quantity):
        pass

class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def update_quantity(self, new_quantity):
        if new_quantity > 0:
            self.quantity = new_quantity

    def calculate_subtotal(self):
        return self.product.calculate_total(self.quantity)

class ConcreteProduct(Product):
    def calculate_total(self, quantity):
        return self.price * quantity

class ShoppingCart:
    def __init__(self):
        self._items = {}

    def add_item(self, product, quantity):
        if product.product_id in self._items:
            self._items[product.product_id].update_quantity(quantity)
        else:
            self._items[product.product_id] = CartItem(product, quantity)

    def remove_item(self, product_id):
        if product_id in self._items:
            del self._items[product_id]

    def update_item_quantity(self, product_id, quantity):
        if product_id in self._items:
            self._items[product_id].update_quantity(quantity)

    def calculate_total(self):
        total = 0
        for item in self._items.values():
            total += item.calculate_subtotal()
        return total

    def display_cart(self):
        if not self._items:
            print("Your cart is empty.")
        else:
            print("Cart Contents:")
            for item in self._items.values():
                print(f"{item.product.name} - Quantity: {item.quantity} - Subtotal: ${item.calculate_subtotal()}")

# Example usage:
product_1 = ConcreteProduct(101, "Laptop", 1000)
product_2 = ConcreteProduct(102, "Headphones", 50)
product_3 = ConcreteProduct(103, "Keyboard", 30)

cart = ShoppingCart()

cart.add_item(product_1, 2)
cart.add_item(product_2, 1)
cart.add_item(product_3, 3)

cart.update_item_quantity(102, 2)
cart.remove_item(103)

cart.display_cart()
print(f"Total Price: ${cart.calculate_total()}")  # Output: Total Price: $2100



# Encapsulation:
# Explanation: Encapsulation is the principle of bundling data (attributes) and methods that operate on the data (behavior) within a single
#  unit, i.e., a class. In the E-commerce Shopping Cart example, we achieve encapsulation by using access control modifiers (_ prefix) to 
# mark attributes as protected or private, and using getters and setters to control access to these attributes. The Product class encapsulates 
# the product's ID, name, and price as protected attributes, while the ShoppingCart class encapsulates the cart's items as a private attribute. 
# By encapsulating the data, we ensure that it is only accessible and modifiable through controlled methods, promoting data privacy, 
# and abstraction of the internal implementation details from external users.

# Abstraction:
# Explanation: Abstraction is the process of defining a high-level interface for a class while hiding the underlying implementation details. 
# In the E-commerce Shopping Cart example, we achieve abstraction by creating the abstract class Product using the ABC module. 
# The Product class defines an abstract method calculate_total(), which serves as a template for calculating the total price of a product. 
# The abstract method does not provide an implementation in the abstract class, leaving it to its concrete subclasses (e.g., ConcreteProduct)
#  to implement it. This enforces that every concrete product class must implement its own way of calculating the total price. 
# By providing a clear interface without specifying implementation details, abstraction allows us to work with products without 
# concerning ourselves with how each product's total is calculated, promoting code flexibility, and ease of extension.

# Inheritance:
# Explanation: Inheritance is the mechanism in OOP that allows a class (subclass) to inherit properties and behaviors from another class 
# (superclass). In the E-commerce Shopping Cart example, we achieve inheritance by creating the concrete class ConcreteProduct, 
# which inherits from the abstract class Product. The ConcreteProduct class inherits the attributes (product_id, name, price) and the 
# abstract method calculate_total() from the Product class. By reusing the common attributes and methods from the Product class, 
# we avoid code duplication and create specialized products (e.g., Laptop, Headphones) that have their own specific implementation of 
# calculating the total price. This promotes code reuse, modularity, and maintainability.

# Polymorphism:
# Explanation: Polymorphism is the ability of objects of different classes to be treated as objects of a common superclass and respond to 
# the same method calls. In the E-commerce Shopping Cart example, we achieve polymorphism by creating instances of both the Product 
# and ConcreteProduct classes. Despite having different implementations of calculate_total() in each concrete product class, we can treat 
# objects of ConcreteProduct as objects of the common superclass Product. This allows us to use a single interface (calculate_total()) to 
# calculate the total price, regardless of the specific product type. For example, when adding items to the cart, the ShoppingCart class 
# doesn't need to know the specific type of product; it only needs to interact with the common methods provided by the superclass 
# (Product). This promotes code flexibility and simplifies client code that interacts with different product types, making the system more 
# adaptable to future changes and expansions.