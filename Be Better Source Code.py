'''start of the code'''

#START OF THE CODE, THIS HASN'T BEEN CODED YET


#ARJUN'S CODE
#DAVID'S CODE
import random
# Each homework will be stored as a dictionary like:
# {"title": "Lab 3", "course": "CS100", "due": "2025-12-01", "completed": False}


def homework_tracker(homework_list):

    print("\n--- Homework Tracker ---")
    print("a. Create Assignment")
    print("b. Task Completed!")
    print("c. See all Assignments")

    choice = input("Choose an option (a/b/c): ").strip().lower()

    if choice == "a":
        create_assignment(homework_list)
    elif choice == "b":
        mark_assignment_completed(homework_list)
    elif choice == "c":
        see_all_assignments(homework_list)
    else:
        print("Invalid choice.")


def create_assignment(homework_list):
    """
    This will ask the user for assignment info and store it in a dictionary.
    Uses: strings, dictionaries, lists.
    """
    print("\n-- Create Assignment --")
    title = input("Enter assignment name: ").strip()
    course = input("Enter course name (e.g., CS100): ").strip()
    due = input("Enter due date (e.g., 2025-12-01 or 'Monday'): ").strip()





#EMMA'S CODE
income = 0.0
expenses_list = []
current_file = ""


def load_budget_data():
    global income, expenses_list, current_file

    income = 0.0
    expenses_list = []

    f = open(current_file, "r")
    lines = f.readlines()
    f.close()

    if len(lines) == 0:
        return

    income_line = lines[0].strip()
    if income_line != "":
        income = float(income_line)

    for line in lines[1:]:
        line = line.strip()
        if line != "":
            parts = line.split("|")
            if len(parts) == 2:
                name = parts[0]
                amount_text = parts[1]
                amount = float(amount_text)
                expenses_list.append({"name": name, "amount": amount})

def save_budget_data():

    global income, expenses_list, current_file

    f = open(current_file, "w")
    f.write(str(income) + "\n")

    for expense in expenses_list:
        line = expense["name"] + "|" + str(expense["amount"]) + "\n"
        f.write(line)

    f.close()

#GPA CALCULATOR
