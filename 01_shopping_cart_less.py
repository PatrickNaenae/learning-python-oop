class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id  #instance attributes
        self.name = name  #instance attributes
        self.price = price   #instance attributes

    def __str__(self):
        return f"{self.name} - {self.price}"

class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id  #instance attributes
        self.name = name  #instance attributes

    def __str__(self):
        return f"{self.name}"

class ShoppingCart:
    def __init__(self, customer):
        self.customer = customer  #instance attributes
        self.items = []  #instance attributes

    def __str__(self):
        return f"{self.items}"

    def add_to_cart(self, product, quantity=1):  #instance methods
        self.items.append({"product": product, "quantity": quantity})

    def remove_from_cart(self, product):  #instance methods
        self.items = [item for item in self.items if item["product"] != product]

    def total_amount(self):  #instance methods
        total = 0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total

product1 = Product(1, "Laptop", 1000)
product2 = Product(2, "Phone", 500)
product3 = Product(3, "Tablet", 300)

# Create customers
customer1 = Customer(101, "John")
customer2 = Customer(102, "Alice")

# Create shopping carts for customers
cart1 = ShoppingCart(customer1)
cart2 = ShoppingCart(customer2)

# Add items to the shopping carts
cart1.add_to_cart(product1, 2)
cart1.add_to_cart(product2)
cart2.add_to_cart(product2)
cart2.add_to_cart(product3, 3)

# Calculate total for each shopping cart
for item in cart1.items:
    print(item['product'].name, item['product'].price)
print(f"{customer1.name}'s cart total: ${cart1.total_amount()}")
print(f"{customer2.name}'s cart total: ${cart2.total_amount()}")