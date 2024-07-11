import json
from datetime import datetime, timedelta

class Habit:
    """Class representing a habit with task specifications and periodicity."""
    def __init__(self, name, periodicity):
        """
        Initialize a new habit.
        
        :param name: Name of the habit
        :param periodicity: Periodicity of the habit ('daily' or 'weekly')
        """
        self.name = name
        self.periodicity = periodicity
        self.created_at = datetime.now()
        self.completed_tasks = []

    def complete_task(self):
        """Mark the task as completed for the current period."""
        self.completed_tasks.append(datetime.now())

    def get_streak(self):
        """
        Calculate the current streak of consecutive periods the task has been completed.
        
        :return: The current streak count
        """
        if not self.completed_tasks:
            return 0
        
        streak = 1
        sorted_tasks = sorted(self.completed_tasks, reverse=True)
        period_delta = timedelta(days=1) if self.periodicity == 'daily' else timedelta(weeks=1)

        for i in range(1, len(sorted_tasks)):
            if sorted_tasks[i-1] - sorted_tasks[i] > period_delta:
                break
            streak += 1

        return streak

    def to_dict(self):
        """Convert the habit to a dictionary for JSON serialization."""
        return {
            'name': self.name,
            'periodicity': self.periodicity,
            'created_at': self.created_at.isoformat(),
            'completed_tasks': [dt.isoformat() for dt in self.completed_tasks]
        }

    @classmethod
    def from_dict(cls, data):
        """Create a habit instance from a dictionary."""
        habit = cls(data['name'], data['periodicity'])
        habit.created_at = datetime.fromisoformat(data['created_at'])
        habit.completed_tasks = [datetime.fromisoformat(dt) for dt in data['completed_tasks']]
        return habit

