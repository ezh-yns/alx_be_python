task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

reminder = ""

# if time_bound == "yes":
#     reminder = f"Reminder: '{task}' is a  "
# else:
#     reminder = f"Note: '{task}' is a  "

match priority:
    case "high":
        reminder += "high priority task"
    case "medium":
        reminder += "medium priority task"
    case "low":
        reminder += "low priority task"
    case _:
        reminder = "The priority level is not recognized."

if time_bound == "yes":
    reminder += " That requires immediate attention today!"
    print(f"Reminder: {reminder}")
else :
    reminder += ". Consider compliting it when you have free time!"
    print(f"Note: {reminder}")
