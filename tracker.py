import json
from habit import Habit

class HabitTracker:
    """Class to manage habits, including creating, completing, and storing them."""
    
    def __init__(self, filename='habits.json'):
        """
        Initialize the habit tracker.
        
        :param filename: File to store the habits
        """
        self.filename = filename
        self.habits = self.load_habits()
        if not self.habits:
            self.add_predefined_habits()
            
   def add_predefined_habits(self):
        """Add predefined habits to the tracker."""
        predefined_habits = [
            {"name": "Brush Teeth", "periodicity": "daily"},
            {"name": "Workout", "periodicity": "daily"},
            {"name": "Read Book", "periodicity": "daily"},
            {"name": "Grocery Shopping", "periodicity": "weekly"},
            {"name": "Laundry", "periodicity": "weekly"}
        ]

        # Add predefined habits with some example tracking data
        for habit_data in predefined_habits:
            habit = Habit(habit_data["name"], habit_data["periodicity"])
            now = datetime.now()
            if habit_data["periodicity"] == "daily":
                habit.completed_tasks = [now - timedelta(days=i) for i in range(28)]
            elif habit_data["periodicity"] == "weekly":
                habit.completed_tasks = [now - timedelta(weeks=i) for i in range(4)]
            self.habits[habit_data["name"]] = habit
        
        self.save_habits()

    def create_habit(self, name, periodicity):
        """
        Create a new habit.
        
        :param name: Name of the habit
        :param periodicity: Periodicity of the habit ('daily' or 'weekly')
        """
        self.habits[name] = Habit(name, periodicity)
        self.save_habits()

    def complete_habit(self, name):
        """
        Mark a habit as completed.
        
        :param name: Name of the habit
        """
        if name in self.habits:
            self.habits[name].complete_task()
            self.save_habits()
        else:
            print(f"Habit '{name}' does not exist.")

    def save_habits(self):
        """Save the habits to a file."""
        with open(self.filename, 'w') as file:
            json.dump({name: habit.to_dict() for name, habit in self.habits.items()}, file)

    def load_habits(self):
        """Load the habits from a file."""
        try:
            with open(self.filename, 'r') as file:
                return {name: Habit.from_dict(data) for name, data in json.load(file).items()}
        except FileNotFoundError:
            return {}

    def list_habits(self):
        """Return a list of all currently tracked habits."""
        return list(self.habits.keys())

    def habits_by_periodicity(self, periodicity):
        """
        Return a list of habits with the specified periodicity.
        
        :param periodicity: The periodicity to filter habits ('daily' or 'weekly')
        :return: List of habit names
        """
        return [name for name, habit in self.habits.items() if habit.periodicity == periodicity]

    def longest_streak(self):
        """
        Return the longest streak of all defined habits.
        
        :return: Longest streak count
        """
        return max((habit.get_streak() for habit in self.habits.values()), default=0)

    def longest_streak_for_habit(self, name):
        """
        Return the longest streak for a given habit.
        
        :param name: Name of the habit
        :return: Longest streak count for the specified habit
        """
        return self.habits[name].get_streak() if name in self.habits else 0

    def longest_streak_per_periodicity(self, periodicity):
        """
        Return the longest streak of habits with the specified periodicity.
        
        :param periodicity: The periodicity to filter habits ('daily' or 'weekly')
        :return: Longest streak count for the specified periodicity
        """
        return max((habit.get_streak() for habit in self.habits.values() if habit.periodicity == periodicity), default=0)