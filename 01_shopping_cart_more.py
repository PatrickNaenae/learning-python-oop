from abc import ABC,  abstractmethod

class Product(ABC):  # Abstract class - Abstraction
    def __init__(self, product_id, name, price, category):
        self.__product_id = product_id  # Encapsulation: Private attribute
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} - {self.price} USD"

    
    def get_product_id(self):
        return self.__product_id  # Abstraction: Public getter method for private attribute

    @abstractmethod  # Abstract method - Abstraction
    def calculate_discounted_price(self):  # Polymorphism
        pass


class ElectronicsProduct(Product):  # Inheritance
    def __init__(self, product_id, name, price, category, warranty_period):
        super().__init__(product_id, name, price, category)
        self.warranty_period = warranty_period

    def __str__(self):
        return f"{self.name} - {self.price} USD (Warranty: {self.warranty_period} months)"

    def calculate_discounted_price(self):  # Polymorphism
        discount_percentage = 10
        discounted_price = self.price - (self.price * discount_percentage / 100)
        return discounted_price


class FashionProduct(Product):  # Inheritance
    def __init__(self, product_id, name, price, category, size):
        super().__init__(product_id, name, price, category)
        self.size = size

    def __str__(self):
        return f"{self.name} - {self.price} USD (Size: {self.size})"

    def calculate_discounted_price(self):  # Polymorphism
        discount_percentage = 20
        discounted_price = self.price - (self.price * discount_percentage / 100)
        return discounted_price


# Example usage: (Unchanged)
electronics_product = ElectronicsProduct(101, "Smartphone", 500, "Electronics", warranty_period=12)
fashion_product = FashionProduct(201, "T-shirt", 30, "Fashion", size="M")

print(electronics_product)
print(fashion_product)

# Polymorphism in action:
products = [electronics_product, fashion_product]


print("\nDiscounted Prices:")
for product in products:
    print(f"{product.name}: {product.calculate_discounted_price()} USD")


# Encapsulation: The Product class has a private attribute __product_id, 
# which is encapsulated and hidden from direct access outside the class.

# Abstraction: The Product class is abstract due to the presence of the @abstractmethod decorator for the calculate_discounted_price method. 
# It defines a common interface for all products but leaves the implementation details to its subclasses.

# Inheritance: The ElectronicsProduct and FashionProduct classes inherit from the abstract class Product, 
# inheriting its attributes and methods.

# Polymorphism: Both ElectronicsProduct and FashionProduct classes override the calculate_discounted_price method to provide 
# specific behavior for calculating discounted prices based on their product categories. This demonstrates polymorphism by allowing 
# different products to have their own implementation of the same method.