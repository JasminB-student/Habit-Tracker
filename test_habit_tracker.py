import unittest
from habit import Habit
from tracker import HabitTracker

class TestHabit(unittest.TestCase):
    def test_create_habit(self):
        """Test creating a new habit."""
        habit = Habit("Test Habit", "daily")
        self.assertEqual(habit.name, "Test Habit")
        self.assertEqual(habit.periodicity, "daily")

    def test_complete_task(self):
        """Test marking a task as completed."""
        habit = Habit("Test Habit", "daily")
        habit.complete_task()
        self.assertEqual(len(habit.completed_tasks), 1)

    def test_get_streak(self):
        """Test calculating the current streak of consecutive task completions."""
        habit = Habit("Test Habit", "daily")
        habit.complete_task()
        self.assertEqual(habit.get_streak(), 1)
        habit.complete_task()
        self.assertEqual(habit.get_streak(), 2)

class TestHabitTracker(unittest.TestCase):
    def setUp(self):
        """Set up a habit tracker instance for testing."""
        self.tracker = HabitTracker(filename='test_habits.json')

    def tearDown(self):
        """Clean up the test habits file."""
        import os
        os.remove('test_habits.json')

    def test_create_and_list_habits(self):
        """Test creating and listing habits."""
        self.tracker.create_habit("Test Habit 1", "daily")
        self.tracker.create_habit("Test Habit 2", "weekly")
        self.assertEqual(len(self.tracker.list_habits()), 2)

    def test_complete_habit(self):
        """Test marking a habit as completed."""
        self.tracker.create_habit("Test Habit", "daily")
        self.tracker.complete_habit("Test Habit")
        habit = self.tracker.habits["Test Habit"]
        self.assertEqual(len(habit.completed_tasks), 1)

    def test_longest_streak(self):
        """Test calculating the longest streak of all habits."""
        self.tracker.create_habit("Test Habit", "daily")
        self.tracker.complete_habit("Test Habit")
        self.assertEqual(self.tracker.longest_streak(), 1)

if __name__ == '__main__':
    unittest.main()
