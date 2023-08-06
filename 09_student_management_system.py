from abc import ABC, abstractmethod

class Student(ABC):
    def __init__(self, student_id, name):
        self._student_id = student_id  # Encapsulation: Protected attribute for student ID
        self._name = name  # Encapsulation: Protected attribute for student name

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, new_student_id):
        self._student_id = new_student_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @abstractmethod
    def calculate_grade(self):
        pass

class RegularStudent(Student):
    def __init__(self, student_id, name, marks):
        super().__init__(student_id, name)
        self.marks = marks

    def calculate_grade(self):  # Polymorphism
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 80:
            return 'B'
        elif self.marks >= 70:
            return 'C'
        elif self.marks >= 60:
            return 'D'
        else:
            return 'F'

class SportsStudent(Student):
    def __init__(self, student_id, name, sport):
        super().__init__(student_id, name)
        self.sport = sport

    def calculate_grade(self):  # Polymorphism
        return 'Pass'  # Sports students are evaluated based on participation, not grades

class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.student_id] = student

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]

    def get_student_grade(self, student_id):
        if student_id in self.students:
            pupil = self.students[student_id]
            return pupil.calculate_grade()
        return None

# Example usage:
regular_student = RegularStudent(101, "John Doe", 85)
sports_student = SportsStudent(102, "Jane Smith", "Basketball")

sms = StudentManagementSystem()

sms.add_student(regular_student)
sms.add_student(sports_student)

print(sms.get_student_grade(101))  # Output: B
print(sms.get_student_grade(102))  # Output: Pass


# Encapsulation:
# Explanation: Encapsulation is the principle of bundling data (attributes) and methods that operate on the data (behavior) within a 
# single unit, i.e., a class. In the Student Management System, we achieve encapsulation by using access control modifiers (_ prefix) 
# to mark attributes as protected and using getters and setters to control access to these attributes. The Student class encapsulates the 
# student's ID and name as protected attributes, while the subclasses (RegularStudent and SportsStudent) encapsulate their specific 
# attributes (marks and sport) as protected attributes. This promotes data privacy, and external users can only access or modify these 
# attributes through controlled methods.

# Inheritance:
# Explanation: Inheritance is the mechanism in OOP that allows a class (subclass) to inherit properties and behaviors from another class 
# (superclass). In the Student Management System, we achieve inheritance by creating the subclasses RegularStudent and SportsStudent, 
# which inherit from the abstract class Student. The subclasses inherit the attributes (student_id, name) and the abstract method 
# calculate_grade() from the Student class. This promotes code reuse and allows creating different types of students with specialized 
# behavior without duplicating code.

# Abstraction:
# Explanation: Abstraction is the process of defining a high-level interface for a class while hiding the underlying implementation details. 
# In the Student Management System, we achieve abstraction by creating the abstract class Student using the ABC module. The Student 
# class defines an abstract method calculate_grade(), which serves as a template for calculating a student's grade. The abstract method 
# does not provide an implementation in the abstract class, leaving it to its concrete subclasses (RegularStudent and SportsStudent) to 
# implement it. This enforces that every concrete student class must implement its own way of calculating the grade. By providing a clear 
# interface without specifying implementation details, abstraction allows us to work with students without concerning ourselves with how 
# each student's grade is calculated, promoting code flexibility, and ease of extension.

# Polymorphism:
# Explanation: Polymorphism is the ability of objects of different classes to be treated as objects of a common superclass and respond to 
# the same method calls. In the Student Management System, we achieve polymorphism by having both the RegularStudent and 
# SportsStudent classes implement the calculate_grade() method to provide specific behavior for calculating the student's grade. 
# Despite having different implementations of calculate_grade(), we can treat objects of both classes as objects of the common superclass 
# Student. This allows us to use a single interface (calculate_grade()) to calculate the grade, regardless of the specific student type, 
# promoting code flexibility and simplifying client code that interacts with different student types.