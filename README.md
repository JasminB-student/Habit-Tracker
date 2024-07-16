# Habit Tracker

A simple habit tracking application implemented in Python. This application allows you to create, manage, and analyze daily and weekly habits, helping you build good habits and break bad ones.

## Features

   -   Create and track daily and weekly habits
   -  Mark habits as completed
   -  Track habit streaks
   -  List habits and analyze their performance
   -  Coommand Line Interface (CLI) for easy interaction

## Requirements

  -  Python 3.7 or later

## Installation

### Step 1: Clone the Repository

First, clone the repository from GitHub:
```
git clone https://github.com/yourusername/habit-tracker.git
cd habit-tracker
```

### Step 2: Create a Virtual Environment (Optional but Recommended)

It is recommended to create a virtual environment to manage dependencies:
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the necessary dependencies using pip:
```
pip install -r requirements.txt
```

### Step 4: Run the Application

You can now run the CLI tool to start using the habit tracker:
```
python interface.py
```

## Usage Guide

The application is controlled via a command-line interface (CLI). Below are the available commands and their usage:

### Create a New Habit

To create a new habit, use the `create` command followed by the habit name and periodicity (`daily` or `weekly`): 
```
create <habit_name> <periodicity>
```

Example:
```
create "Brush Teeth" daily
create "Grocery Shopping" weekly
```

### Complete a Habit Task

To mark a habit as completed for the current period, use the `complete` command followed by the habit name: 
```
complete <habit_name>
```

Example:
```
complete "Brush Teeth"
```

### List All Habits

To list all currently tracked habits, use the `list` command: 
```
list
```

### List Habits by Periodicity

To list all habits with a specific periodicity (`daily` or `weekly`), use the `list` command followed by the periodicity: 
```
list <periodicity>
```

Example:
```
list daily
list weekly
```

### Show the Longest Streak of All Habits

To show the longest run streak of all habits, use the `streak` command: 
```
streak
```

### Show the Longest Streak for a Specific Habit

To show the longest run streak for a specific habit, use the `streak` command followed by the habit name: 
```
streak <habit_name>
```

Example:
```
streak "Brush Teeth"
```

### Exit the Application

To exit the program, use the `exit` command: 
```
exit
```

### Example Workflow

Here is an example workflow demonstrating how to use the application:

1. Create Habits:
```
create "Brush Teeth" daily
create "Workout" daily
create "Grocery Shopping" weekly
```
2. Complete Tasks:
```
complete "Brush Teeth"
complete "Workout"
```
3. List Habits:
```
list
```
4. List Daily Habits:
```
list daily
```
5. Check Streaks:
```
streak
streak "Brush Teeth"
```
6. Exit:
```
exit
```

## Testing

Unit tests are provided to ensure the validity of the habit tracking components. To run the tests, use the following command: 
```
python -m unittest discover
```

This command will discover and run all the unit tests in the project.

## Conclusion

This habit tracking application helps you build and maintain good habits by providing a simple yet effective way to track and analyze your daily and weekly tasks. With the provided CLI, you can easily create, complete, and analyze your habits, ensuring you stay on top of your personal goals.
