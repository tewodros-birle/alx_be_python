# Get user input for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task using match-case for priority
match priority:
    case "high" | "medium" | "low":
        # Handle time-bound status
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
        else:
            print("Invalid input for time-bound status. Please enter 'yes' or 'no'.")
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")
