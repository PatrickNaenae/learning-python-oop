class Car:
    def __init__(self, make, model):
        self.__make = make        # Private attribute
        self._model = model       # Protected attribute

    def start(self):
        print("Engine started.")

    def __accelerate(self):      # Private method
        print("Accelerating.")

    def _stop(self):             # Protected method
        print("Car stopped.")

    def drive(self):
        self.__accelerate()
        print("Driving.")
        self._stop()

car = Car("Toyota", "Camry")

# Accessing public methods and attributes
car.start()
car.drive()

# Accessing private and protected attributes (Not recommended!)
print(car._Car__make)    # Output: Toyota (Accessing private attribute using mangled name)
print(car._model)        # Output: Camry (Accessing protected attribute)

# Accessing private and protected methods (Not recommended!)
car._Car__accelerate()   # Output: Accelerating. (Accessing private method using mangled name)
car._stop()              # Output: Car stopped. (Accessing protected method)



class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age >= 0:
            self.__age = new_age
        else:
            raise ValueError("Age cannot be negative.")

person = Person("Alice", 30)

# Accessing attributes using properties
print(person.name)    # Output: Alice
print(person.age)     # Output: 30

# Updating the age attribute using the setter property
person.age = 31
print(person.age)     # Output: 31

# Trying to set a negative age will raise an exception
person.age = -1       # Raises ValueError: Age cannot be negative.










