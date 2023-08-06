from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.__name = name  # Encapsulation: Private attribute for name
        self.__price = price  # Encapsulation: Private attribute for price
        self.__stock = stock  # Encapsulation: Private attribute for stock

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = new_price

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, new_stock):
        self.__stock = new_stock

    def update_stock(self, quantity):
        self.__stock += quantity

    @abstractmethod  # Abstraction: Abstract method for calculating total price
    def calculate_total_price(self, quantity):
        pass

class SimpleProduct(Product):
    def __init__(self, product_id, name, price, stock):
        super().__init__(product_id, name, price, stock)

    def calculate_total_price(self, quantity):  # Polymorphism
        return self.price * quantity

class DiscountedProduct(Product):
    def __init__(self, product_id, name, price, stock, discount_rate):
        super().__init__(product_id, name, price, stock)
        self.discount_rate = discount_rate

    def calculate_total_price(self, quantity):  # Polymorphism
        discounted_price = self.price * (1 - self.discount_rate)
        return discounted_price * quantity

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id not in self.products:
            self.products[product.product_id] = product

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]

    def get_product_by_id(self, product_id):
        return self.products.get(product_id)

    def list_products(self):
        return list(self.products.values())

class Transaction:
    def __init__(self, transaction_id, products):
        self.transaction_id = transaction_id
        self.products = products

    def __str__(self):
        return f"Transaction {self.transaction_id}"

    def calculate_total_cost(self):
        total_cost = 0
        for product, quantity in self.products.items():
            total_cost += product.calculate_total_price(quantity)
        return total_cost

# Example usage:
inventory = Inventory()

product_1 = SimpleProduct(101, "Phone", 500, 10)
product_2 = DiscountedProduct(201, "Laptop", 1000, 5, discount_rate=0.1)

inventory.add_product(product_1)
inventory.add_product(product_2)

transaction_1 = Transaction(1, {product_1: 2, product_2: 1})
total_cost = transaction_1.calculate_total_cost()

print(f"{transaction_1} Total Cost: ${total_cost}")

# Update product_1 attributes using setters
product_1.name = "Smartphone"
product_1.price = 550
product_1.stock = 15
product_1.update_stock(5)

# Retrieve and print updated product attributes from the inventory
updated_product_1 = inventory.get_product_by_id(101)
print(f"Updated Product 1 Name: {updated_product_1.name}")   # Output: Smartphone
print(f"Updated Product 1 Price: {updated_product_1.price}") # Output: 550
print(f"Updated Product 1 Stock: {updated_product_1.stock}") # Output: 20

# Explanation of OOP principles:
# 1. Encapsulation: Attributes like name, price, and stock are encapsulated as private attributes (using double underscore) and 
# accessed using property getters and setters. This prevents direct access and allows controlled modification.
# 2. Abstraction: The Product class is an abstract class with an abstract method calculate_total_price(). 
# It defines a common interface for all products but leaves the implementation to its subclasses.
# 3. Inheritance: SimpleProduct and DiscountedProduct classes inherit from the Product class, inheriting its attributes and methods. 
# This promotes code reuse and allows creating different types of products with specialized behavior.
# 4. Polymorphism: Both SimpleProduct and DiscountedProduct classes override the calculate_total_price method to provide specific 
# behavior for different types of products. This demonstrates polymorphism by allowing different product types to have their own 
# implementation of the same method with different behaviors.
