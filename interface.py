import sys
from tracker import HabitTracker

def main():
    """Main function to handle user commands."""
    tracker = HabitTracker()

    def print_help():
        """Print the help message with available commands."""
        print("""
        Available commands:
        1. create <habit_name> <periodicity> - Create a new habit (periodicity: daily or weekly)
        2. complete <habit_name> - Mark a habit as completed for the current period
        3. list - List all currently tracked habits
        4. list <periodicity> - List all habits with the specified periodicity (daily or weekly)
        5. streak - Show the longest run streak of all habits
        6. streak <habit_name> - Show the longest run streak for the specified habit
        7. exit - Exit the program
        """)

    while True:
        command = input("Enter command (type 'help' for options): ").strip().split()
        if not command:
            continue
        action = command[0].lower()

        if action == 'help':
            print_help()
        elif action == 'create' and len(command) == 3:
            habit_name, periodicity = command[1], command[2]
            tracker.create_habit(habit_name, periodicity)
        elif action == 'complete' and len(command) == 2:
            habit_name = command[1]
            tracker.complete_habit(habit_name)
        elif action == 'list':
            if len(command) == 1:
                print("All habits:", tracker.list_habits())
            elif len(command) == 2:
                periodicity = command[1]
                print(f"Habits with periodicity '{periodicity}':", tracker.habits_by_periodicity(periodicity))
        elif action == 'streak':
            if len(command) == 1:
                print("Longest streak of all habits:", tracker.longest_streak())
            elif len(command) == 2:
                habit_name = command[1]
                print(f"Longest streak for habit '{habit_name}':", tracker.longest_streak_for_habit(habit_name))
        elif action == 'exit':
            print("Exiting program.")
            break
        else:
            print("Invalid command. Type 'help' for options.")

if __name__ == '__main__':
    main()
