import datetime

class Activity:
    def __init__(self, activity_type, start_time, duration, calories_burned=0):
        self.activity_type = activity_type
        self.start_time = start_time
        self.duration = duration
        self.calories_burned = calories_burned

    def __str__(self):
        return f"{self.activity_type} - {self.start_time} (Duration: {self.duration} min, Calories Burned: {self.calories_burned} cal)"

    def calculate_calories_burned(self, weight, intensity):
        # A simple formula to calculate calories burned based on weight and activity intensity
        # This formula is just for demonstration purposes and not accurate in a real fitness tracker
        self.calories_burned = int(self.duration * weight * intensity)


class FitnessTracker:
    def __init__(self, user_name, weight):
        self.user_name = user_name
        self.weight = weight
        self.activities = []

    def add_activity(self, activity):
        self.activities.append(activity)

    def total_calories_burned(self):
        total_calories = sum(activity.calories_burned for activity in self.activities)
        return total_calories


# Example usage:
user_name = "John"
weight_kg = 75

tracker = FitnessTracker(user_name, weight_kg)

# Track a running activity
start_time_run = datetime.datetime(2023, 8, 10, 9, 0)
running_activity = Activity("Running", start_time_run, duration=30)
running_activity.calculate_calories_burned(weight_kg, intensity=8)
tracker.add_activity(running_activity)

# Track a cycling activity
start_time_cycle = datetime.datetime(2023, 8, 10, 17, 0)
cycling_activity = Activity("Cycling", start_time_cycle, duration=45)
cycling_activity.calculate_calories_burned(weight_kg, intensity=5)
tracker.add_activity(cycling_activity)

# Display activities and total calories burned
for activity in tracker.activities:
    print(activity)

print(f"Total Calories Burned: {tracker.total_calories_burned()} cal")
