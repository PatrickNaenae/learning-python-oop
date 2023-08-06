import datetime

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def __str__(self):
        return self.name


class Task:
    def __init__(self, task_id, title, description, assignee, due_date=None):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.assignee = assignee
        self.due_date = due_date
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.title} - {status}"

    def mark_as_completed(self):
        self.completed = True

    def update_due_date(self, due_date):
        self.due_date = due_date


class TaskTracker:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def find_task_by_id(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def find_tasks_by_user(self, user):
        user_tasks = []
        for task in self.tasks:
            if task.assignee == user:
                user_tasks.append(task)
        return user_tasks

    def __str__(self):
        return "\n".join(str(task) for task in self.tasks)


# Example usage:
user1 = User(1, "John")
user2 = User(2, "Alice")

task1 = Task(101, "Implement Login", "Create a login system for the website", user1)
task1.update_due_date(datetime.date(2023, 8, 10))

task2 = Task(102, "Design UI", "Design the user interface for the app", user2)
task2.update_due_date(datetime.date(2023, 8, 15))

task3 = Task(103, "Write Documentation", "Write documentation for the project", user1)
task3.update_due_date(datetime.date(2023, 8, 20))

tracker = TaskTracker()
tracker.add_task(task1)
tracker.add_task(task2)
tracker.add_task(task3)

print(tracker.find_task_by_id(102))
user_tasks = tracker.find_tasks_by_user(user1)
for task in user_tasks:
    print(task)


