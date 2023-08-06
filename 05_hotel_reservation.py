from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class RoomType(ABC):
    def __init__(self, name, base_price):
        self._name = name  # Encapsulation: Protected attribute for name
        self._base_price = base_price  # Encapsulation: Protected attribute for base_price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def base_price(self):
        return self._base_price

    @base_price.setter
    def base_price(self, new_base_price):
        self._base_price = new_base_price

    @abstractmethod
    def calculate_total_cost(self, check_in_date, check_out_date):
        pass

class StandardRoom(RoomType):
    def __init__(self):
        super().__init__("Standard Room", base_price=100)

    def calculate_total_cost(self, check_in_date, check_out_date):  # Polymorphism
        nights = (check_out_date - check_in_date).days
        return self.base_price * nights

class SuiteRoom(RoomType):
    def __init__(self):
        super().__init__("Suite Room", base_price=200)

    def calculate_total_cost(self, check_in_date, check_out_date):  # Polymorphism
        nights = (check_out_date - check_in_date).days
        return self.base_price * nights

class Hotel:
    def __init__(self):
        self.rooms = {}
        self.reservations = {}

    def add_room(self, room_number, room_type):
        self.rooms[room_number] = room_type

    def remove_room(self, room_number):
        if room_number in self.rooms:
            del self.rooms[room_number]

    def make_reservation(self, room_number, check_in_date, check_out_date):
        if room_number not in self.rooms:
            raise ValueError("Room does not exist.")

        room_type = self.rooms[room_number]
        total_cost = room_type.calculate_total_cost(check_in_date, check_out_date)

        reservation_id = len(self.reservations) + 1
        reservation = Reservation(reservation_id, room_number, check_in_date, check_out_date, total_cost)

        self.reservations[reservation_id] = reservation
        return reservation

class Reservation:
    def __init__(self, reservation_id, room_number, check_in_date, check_out_date, total_cost):
        self.reservation_id = reservation_id
        self.room_number = room_number
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.total_cost = total_cost

    def __str__(self):
        return f"Reservation {self.reservation_id} for Room {self.room_number} from {self.check_in_date.strftime('%Y-%m-%d')} to {self.check_out_date.strftime('%Y-%m-%d')}"

# Example usage:
hotel = Hotel()

standard_room = StandardRoom()
suite_room = SuiteRoom()

hotel.add_room("101", standard_room)
hotel.add_room("102", suite_room)

check_in_date = datetime(2023, 8, 1)
check_out_date = datetime(2023, 8, 5)

reservation_1 = hotel.make_reservation("101", check_in_date, check_out_date)
reservation_2 = hotel.make_reservation("102", check_in_date, check_out_date)

print(reservation_1)  # Output: Reservation 1 for Room 101 from 2023-08-01 to 2023-08-05
print(reservation_2)  # Output: Reservation 2 for Room 102 from 2023-08-01 to 2023-08-05


# Explanation of OOP principles in the Hotel Reservation System:

# Encapsulation: We use the @property decorator and setters (@name.setter and @base_price.setter) to encapsulate attributes name and 
# base_price as protected attributes in the RoomType class. The protected attributes cannot be accessed directly from outside the class 
# and can be modified using the provided setters, which allows controlled access and modification.

# Abstraction: The RoomType class is an abstract class with an abstract method calculate_total_cost. 
# It defines a common interface for different room types (e.g., standard and suite rooms), but the implementation 
# is left to its concrete subclasses (StandardRoom and SuiteRoom). This promotes abstraction by providing a high-level interface for 
# calculating the total cost of a reservation without specifying how it is done.

# Inheritance: The StandardRoom and SuiteRoom classes inherit from the RoomType class, inheriting its attributes and methods. 
# This promotes code reuse and allows creating different types of room types with specialized behavior. In this example, 
# both classes have their implementations of the calculate_total_cost method, which demonstrates inheritance and polymorphism.

# Polymorphism: Both the StandardRoom and SuiteRoom classes override the calculate_total_cost method to provide specific behavior 
# for calculating the total cost of reservations based on the number of nights. This demonstrates polymorphism by allowing different 
# room types to have their own implementation of the same method with different behaviors. 
# The RoomType class serves as the common interface for these different implementations.