#Daily Task Reminder
print("\n Welcome to DailyTask Reminder!")
print("Plan your day effectively with personalized task reminders.\n")

# Get user input with input validation
while True:
    task = input("Enter your priority task: ").strip()
    if task:
        break
    print("Task cannot be empty. Please enter a valid task.")

while True:
    priority = input("Priority(high/medium/low): ").lower().strip()
    if priority in ["high", "medium", "low"]:
        break
    print("Invalid priority. Please enter high, medium, or low.")

while True:
    time_bound = input("Is this time-bound? (yes/no): ").lower().strip()
    if time_bound in ["yes", "no"]:
        break
    print("Invalid response. Please enter yes or no.")

#customized reminder
print("\n" + "="*50)
if time_bound == "yes":
    print(f"  '{task}' is a {priority} priority task that requires immediate attention today!")
    print(f"  This task is time-sensitive! Complete it before your deadline.")
else:
    print(f"  '{task}' is a {priority} priority task.")
    print(f"  Consider completing it when you have free time.")

# Completion message
print("="*50)
