class Course:
    def __init__(self, course_id, title, instructor, price):
        self.course_id = course_id
        self.title = title
        self.instructor = instructor
        self.price = price
        self.students = []

    def __str__(self):
        return f"{self.title} (Course ID: {self.course_id}) by {self.instructor}"

    def enroll_student(self, student):
        if student not in self.students:
            self.students.append(student)
            print(f"{student} enrolled in {self.title}.")
        else:
            print(f"{student} is already enrolled in {self.title}.")

    def get_students(self):
        return self.students

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def __str__(self):
        return self.name


class Instructor(User):
    def __init__(self, user_id, name, expertise):
        super().__init__(user_id, name)
        self.expertise = expertise

    def __str__(self):
        return f"Instructor: {self.name} (Expertise: {self.expertise})"


class Student(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.courses_enrolled = []

    def __str__(self):
        return f"Student: {self.name}"

    def enroll_course(self, course):
        if course not in self.courses_enrolled:
            course.enroll_student(self)
            self.courses_enrolled.append(course)
        else:
            print(f"{self.name} is already enrolled in {course.title}.")


# Example usage:
instructor1 = Instructor(101, "John Doe", "Python Programming")
instructor2 = Instructor(102, "Jane Smith", "Web Development")

course1 = Course(201, "Python Basics", instructor1, 100)
course2 = Course(202, "Web Development Fundamentals", instructor2, 120)

student1 = Student(301, "Alice")
student2 = Student(302, "Bob")

print(instructor1)
print(course1)
print(student1)

student1.enroll_course(course1)  # Alice enrolled in Python Basics.
student2.enroll_course(course1)  # Bob enrolled in Python Basics.
student1.enroll_course(course2)  # Alice enrolled in Web Development Fundamentals.
student1.enroll_course(course2)  # Alice is already enrolled in Web Development Fundamentals.


# Get the students enrolled in each course
for course in [course1, course2]:
    students = course.get_students()
    print(f"Students enrolled in {course.title}: {[student.name for student in students]}")