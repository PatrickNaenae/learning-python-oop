from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, emp_id, name):
        self._emp_id = emp_id  # Encapsulation: Protected attribute for employee ID
        self._name = name  # Encapsulation: Protected attribute for employee name

    @property
    def emp_id(self):
        return self._emp_id

    @emp_id.setter
    def emp_id(self, new_emp_id):
        self._emp_id = new_emp_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @abstractmethod
    def calculate_salary(self):
        pass

class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    @property
    def hourly_rate(self):
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, new_hourly_rate):
        self._hourly_rate = new_hourly_rate

    @property
    def hours_worked(self):
        return self._hours_worked

    @hours_worked.setter
    def hours_worked(self, new_hours_worked):
        self._hours_worked = new_hours_worked

    def calculate_salary(self):  # Polymorphism
        return self.hourly_rate * self.hours_worked

class SalariedEmployee(Employee):
    def __init__(self, emp_id, name, annual_salary):
        super().__init__(emp_id, name)
        self.annual_salary = annual_salary

    @property
    def annual_salary(self):
        return self._annual_salary

    @annual_salary.setter
    def annual_salary(self, new_annual_salary):
        self._annual_salary = new_annual_salary

    def calculate_salary(self):  # Polymorphism
        return self.annual_salary

class PayrollSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self, employee):
        self.employees[employee.emp_id] = employee

    def remove_employee(self, emp_id):
        if emp_id in self.employees:
            del self.employees[emp_id]

    def calculate_payroll(self):
        payroll_data = {}
        for emp_id, employee in self.employees.items():
            payroll_data[emp_id] = employee.calculate_salary()
        return payroll_data

# Example usage:
payroll_system = PayrollSystem()

hourly_employee = HourlyEmployee(101, "John Doe", hourly_rate=20, hours_worked=160)
salaried_employee = SalariedEmployee(102, "Jane Smith", annual_salary=50000)

payroll_system.add_employee(hourly_employee)
payroll_system.add_employee(salaried_employee)

print(payroll_system.calculate_payroll())  # Output: {101: 3200, 102: 50000}


# Explanation of OOP principles in the Employee Payroll System:

# Encapsulation:
# Explanation: Encapsulation is the principle of bundling data (attributes) and methods that operate on the data (behavior) within a 
# single unit, i.e., a class. In the Employee Payroll System, we achieve encapsulation by using the @property decorator and setters 
# (@emp_id.setter, @name.setter, @hourly_rate.setter, @hours_worked.setter, and @annual_salary.setter) to encapsulate attributes 
# emp_id, name, hourly_rate, hours_worked, and annual_salary as protected attributes in the Employee, HourlyEmployee, and 
# SalariedEmployee classes. The protected attributes cannot be accessed directly from outside the classes and can be modified using 
# the provided setters, which allows controlled access and modification. This promotes data privacy and abstraction of the internal 
# implementation details from external users.

# Abstraction:
# Explanation: Abstraction is the process of defining a high-level interface for a class while hiding the underlying implementation details. 
# In the Employee Payroll System, we achieve abstraction through the Employee class, which serves as an abstract class with the 
# abstract method calculate_salary(). The Employee class provides a high-level interface for employee information (emp_id, name) 
# and the calculation of salary (calculate_salary()), without specifying how the salary is calculated. 
# The subclasses (HourlyEmployee and SalariedEmployee) implement their specific behavior for calculating the salary. 
# This promotes abstraction by providing a clear separation between the high-level interface and the underlying implementation, 
# and it ensures that every concrete employee type must implement the calculate_salary() method.

# Inheritance:
# Explanation: Inheritance is the mechanism in OOP that allows a class (subclass) to inherit properties and behaviors from another class 
# (superclass). In the Employee Payroll System, we achieve inheritance by creating the subclasses HourlyEmployee and SalariedEmployee,
#  which inherit from the Employee class. The subclasses inherit the attributes (emp_id, name) and the abstract method calculate_salary() 
# from the Employee class. This promotes code reuse and allows creating different types of employees with specialized behavior without 
# duplicating code.

# Polymorphism:
# Explanation: Polymorphism is the ability of objects of different classes to be treated as objects of a common superclass and respond to 
# the same method calls. In the Employee Payroll System, we achieve polymorphism by having both the HourlyEmployee and 
# SalariedEmployee classes implement the calculate_salary() method to provide specific behavior for calculating the salary based on 
# the employee type (hourly or salaried). Despite having different implementations of calculate_salary(), we can treat objects of both 
# classes as objects of the common superclass Employee. This allows us to use a single interface (calculate_salary()) to calculate the salary,
#  regardless of the specific employee type, promoting code flexibility and simplifying client code that interacts with different employee 
# types.