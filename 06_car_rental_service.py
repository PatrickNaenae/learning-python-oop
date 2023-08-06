from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class CarType(ABC):
    def __init__(self, name, base_price_per_day):
        self._name = name  # Encapsulation: Protected attribute for name
        self._base_price_per_day = base_price_per_day  # Encapsulation: Protected attribute for base_price_per_day

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def base_price_per_day(self):
        return self._base_price_per_day

    @base_price_per_day.setter
    def base_price_per_day(self, new_base_price):
        self._base_price_per_day = new_base_price

    @abstractmethod
    def calculate_total_cost(self, rental_duration):
        pass

class EconomyCar(CarType):
    def __init__(self):
        super().__init__("Economy Car", base_price_per_day=50)

    def calculate_total_cost(self, rental_duration):  # Polymorphism
        return self.base_price_per_day * rental_duration

class LuxuryCar(CarType):
    def __init__(self):
        super().__init__("Luxury Car", base_price_per_day=150)

    def calculate_total_cost(self, rental_duration):  # Polymorphism
        return self.base_price_per_day * rental_duration

class CarRentalService:
    def __init__(self):
        self.cars = {}
        self.rentals = {}

    def add_car(self, car_id, car_type):
        self.cars[car_id] = car_type

    def remove_car(self, car_id):
        if car_id in self.cars:
            del self.cars[car_id]

    def rent_car(self, car_id, rental_duration):
        if car_id not in self.cars:
            raise ValueError("Car does not exist.")

        car_type = self.cars[car_id]
        total_cost = car_type.calculate_total_cost(rental_duration)

        rental_id = len(self.rentals) + 1
        rental = Rental(rental_id, car_id, rental_duration, total_cost)

        self.rentals[rental_id] = rental
        return rental

class Rental:
    def __init__(self, rental_id, car_id, rental_duration, total_cost):
        self.rental_id = rental_id
        self.car_id = car_id
        self.rental_duration = rental_duration
        self.total_cost = total_cost

    def __str__(self):
        return f"Rental {self.rental_id} for Car {self.car_id} with {self.rental_duration} days rental duration"

# Example usage:
car_rental_service = CarRentalService()

economy_car = EconomyCar()
luxury_car = LuxuryCar()

car_rental_service.add_car("C101", economy_car)
car_rental_service.add_car("C102", luxury_car)

rental_duration = 5

rental_1 = car_rental_service.rent_car("C101", rental_duration)
rental_2 = car_rental_service.rent_car("C102", rental_duration)

print(rental_1)  # Output: Rental 1 for Car C101 with 5 days rental duration
print(rental_2)  # Output: Rental 2 for Car C102 with 5 days rental duration


# Encapsulation:
# Explanation: Encapsulation is the principle of bundling data (attributes) and methods that operate on the data (behavior) within a single 
# unit, i.e., a class. In the Car Rental Service, we achieve encapsulation by using the @property decorator and setters 
# (@name.setter and @base_price_per_day.setter) to encapsulate attributes name and base_price_per_day as protected attributes in 
# the CarType class. The protected attributes cannot be accessed directly from outside the class and can be modified using the provided 
# setters, which allows controlled access and modification. This promotes data privacy and abstraction of the internal implementation 
# details from external users.

# Abstraction:
# Explanation: Abstraction is the process of defining a high-level interface for a class while hiding the underlying implementation details. 
# In the Car Rental Service, we achieve abstraction through the use of an abstract class CarType with an abstract method 
# calculate_total_cost. The CarType class serves as a template for different car types, and the calculate_total_cost method provides a 
# high-level interface for calculating the total cost of a car rental. However, the specific implementation of calculate_total_cost is 
# deferred to its concrete subclasses (EconomyCar and LuxuryCar). By defining an abstract method in the CarType class, 
# we create an abstraction that enforces the presence of calculate_total_cost in its subclasses, ensuring that all car types have a consistent 
# interface to calculate the rental cost but allow customization of the calculation for different car types.

# Inheritance:
# Explanation: Inheritance is the mechanism in OOP that allows a class (subclass) to inherit properties and behaviors from another class
#  (superclass). In the Car Rental Service, we achieve inheritance by creating the subclasses EconomyCar and LuxuryCar that inherit 
# from the CarType class. The subclasses inherit the attributes (name and base_price_per_day) and methods 
# (including the abstract method calculate_total_cost) from the CarType class. This promotes code reuse and allows creating different 
# types of car types with specialized behavior without duplicating code.

# Polymorphism:
# Explanation: Polymorphism is the ability of objects of different classes to be treated as objects of a common superclass and respond 
# to the same method calls. In the Car Rental Service, we achieve polymorphism by having both the EconomyCar and LuxuryCar 
# classes override the calculate_total_cost method to provide specific behavior for calculating the total cost of a car rental based on the 
# rental duration. Despite having different implementations of calculate_total_cost, we can treat objects of both classes as objects of the 
# common superclass CarType. This allows us to use a single interface (calculate_total_cost) to calculate the rental cost, regardless of the 
# specific car type, promoting code flexibility and simplifying client code that interacts with different car types.