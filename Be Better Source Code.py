# ==========================================
# BE BETTER - Smart Student Planner
# Team Members: David Oladapo, Emmanuella Austin-Gabriel
# Features: Goal Tracker (not included here), Homework Tracker, Budget Tracker
# ==========================================

import random   # used for motivational messages
import os       # used to check for files

# ---------- Global user/profile variables ----------
userName = ""
userMajor = ""
userYearofGraduation = ""

PROFILE_FILENAME = "user_profile.txt"   # consistent filename


# ---------- User profile functions ----------
def loadUserProfile():
    """Try to load the saved user profile. Return True if loaded, False if not found."""
    global userName, userMajor, userYearofGraduation
    try:
        f = open(PROFILE_FILENAME, "r")
    except FileNotFoundError:
        return False

    lines = f.readlines()
    f.close()

    if len(lines) >= 3:
        userName = lines[0].strip()
        userMajor = lines[1].strip()
        userYearofGraduation = lines[2].strip()
        return True

    return False


def saveUserProfile():
    """Save the current user profile to file."""
    global userName, userMajor, userYearofGraduation
    f = open(PROFILE_FILENAME, "w")
    f.write(userName + "\n")
    f.write(userMajor + "\n")
    f.write(userYearofGraduation + "\n")
    f.close()


def setupNewUser():
    """Ask the user to enter profile information and save it."""
    global userName, userMajor, userYearofGraduation
    print("\nWelcome new User, Let's set up your account.")
    userName = input("Enter your name: ").strip()
    userMajor = input("Enter your major: ").strip()
    userYearofGraduation = input("Enter your year of graduation: ").strip()
    saveUserProfile()
    print("\nProfile saved. Welcome, " + userName + "!\n")


# ---------- START MENU (as requested) ----------
def start_menu():
    """Start menu: welcome the user, try to reload session or set up a new profile."""
    print("========================================")
    print("     Welcome to Be Better!")
    print("  A Smart Planner for Student Success")
    print("========================================\n")

    loaded = loadUserProfile()
    if loaded:
        print("Reloading your last session for " + userName + "...\n")
        # If you want, you can print loaded profile info here
        print("Name: " + userName)
        print("Major: " + userMajor)
        print("Graduation Year: " + userYearofGraduation + "\n")
    else:
        print("Welcome new User, Let's set up your account.\n")
        setupNewUser()


# ---------- HOMEWORK TRACKER ----------
homework_list = []  # each item: {"title","course","due","completed"}


def homework_tracker():
    print("\n--- Homework Tracker ---")
    print("a. Create Assignment")
    print("b. Task Completed!")
    print("c. See all Assignments")

    choice = input("Choose an option (a/b/c): ").strip().lower()

    if choice == "a":
        create_assignment()
    elif choice == "b":
        mark_assignment_completed()
    elif choice == "c":
        see_all_assignments()
    else:
        print("Invalid choice.")


def create_assignment():
    print("\n-- Create Assignment --")
    title = input("Enter assignment name: ").strip()
    course = input("Enter course name (e.g., CS100): ").strip()
    due = input("Enter due date (e.g., 2025-12-01 or 'Monday'): ").strip()

    if title == "" or course == "" or due == "":
        print("Assignment name, course, and due date cannot be empty.")
        return

    assignment = {
        "title": title,
        "course": course,
        "due": due,
        "completed": False
    }

    homework_list.append(assignment)
    print("Assignment created!")


def mark_assignment_completed():
    if len(homework_list) == 0:
        print("You don't have any assignments yet.")
        return

    print("\n-- Mark Assignment Completed --")
    index = 0
    while index < len(homework_list):
        hw = homework_list[index]
        status_text = "Done" if hw["completed"] else "Pending"
        print(str(index + 1) + ". " + hw["title"] +
              " | Course: " + hw["course"] +
              " | Due: " + hw["due"] +
              " | Status: " + status_text)
        index = index + 1

    choice = input("Which assignment is completed? (number): ").strip()
    if not choice.isdigit():
        print("Invalid input.")
        return

    selection = int(choice) - 1
    if selection < 0 or selection >= len(homework_list):
        print("Invalid choice.")
        return

    homework_list[selection]["completed"] = True

    messages = [
        "You did it! Task conquered!",
        "Great job, keep going!",
        "Another assignment off the list!",
        "Nice work, you're staying on top of it!"
    ]
    mot = random.choice(messages)
    print("Yay! Assignment completed!")
    print(mot)


def see_all_assignments():
    if len(homework_list) == 0:
        print("No homework yet. Add an assignment to get started.")
        return

    print("\n-- All Assignments --")
    for hw in homework_list:
        status_text = "Done" if hw["completed"] else "Pending"
        line = "- " + hw["title"]
        line += " | Course: " + hw["course"]
        line += " | Due: " + hw["due"]
        line += " | Status: " + status_text
        print(line)

    count = len(homework_list)
    binary_count = bin(count)
    print("\nYou currently have " + str(count) + " assignment(s).")
    print("In binary, that is: " + binary_count)


# ---------- BUDGET TRACKER ----------
income = 0.0
expenses_list = []
current_file = ""


def load_budget_data():
    global income, expenses_list, current_file
    income = 0.0
    expenses_list = []

    # if file doesn't exist, just return
    if not os.path.exists(current_file):
        return

    f = open(current_file, "r")
    lines = f.readlines()
    f.close()

    if len(lines) == 0:
        return

    income_line = lines[0].strip()
    if income_line != "":
        try:
            income = float(income_line)
        except ValueError:
            income = 0.0

    for line in lines[1:]:
        line = line.strip()
        if line != "":
            parts = line.split("|")
            if len(parts) == 2:
                name = parts[0]
                try:
                    amount = float(parts[1])
                except ValueError:
                    amount = 0.0
                expenses_list.append({"name": name, "amount": amount})


def save_budget_data():
    global income, expenses_list, current_file
    f = open(current_file, "w")
    f.write(str(income) + "\n")
    for expense in expenses_list:
        line = expense["name"] + "|" + str(expense["amount"]) + "\n"
        f.write(line)
    f.close()


def show_summary():
    global income, expenses_list
    print("\n=== ACCOUNT SUMMARY ===")
    print("Income: " + str(income))

    total_expenses = 0.0
    if len(expenses_list) == 0:
        print("No expenses yet.")
    else:
        print("\nExpenses:")
        for expense in expenses_list:
            print("- " + expense["name"] + ": " + str(expense["amount"]))
            total_expenses = total_expenses + expense["amount"]

    remaining = income - total_expenses
    print("\nTotal Expenses: " + str(total_expenses))
    print("Remaining Money: " + str(remaining))
    print("")


def add_expense():
    global expenses_list
    print("\n--- Add a New Expense ---")
    name = input("Enter expense name: ").strip()
    amt = input("Enter expense amount: ").strip()
    try:
        amount = float(amt)
    except ValueError:
        print("Invalid amount. Expense not added.")
        return

    expenses_list.append({"name": name, "amount": amount})
    save_budget_data()
    print("Expense added.\n")


def budget_tracker():
    global income, expenses_list, current_file
    print("\n=== BUDGET TRACKER ===")
    print("Are you:")
    print("1. A new user")
    print("2. A returning user")
    user_type = input("Choose an option (1/2): ").strip()

    username = input("Enter your name (no spaces): ").strip()
    current_file = username + "_budget.txt"

    if user_type == "1":
        print("\nDo you currently have:")
        print("1. Income only")
        print("2. Savings only")
        print("3. Both income and savings")
        print("4. None (start at 0)")
        money_choice = input("Choose an option (1/2/3/4): ").strip()

        print("\n--- Budget Setup ---")
        if money_choice == "1" or money_choice == "3":
            inc = input("Enter your income: ").strip()
            try:
                income = float(inc)
            except ValueError:
                income = 0.0
        else:
            income = 0.0

        save_budget_data()

        print("\nNow let's add your expenses.")
        while True:
            add_expense()
            more = input("Add another? (yes/no): ").lower()
            if more != "yes":
                break

        show_summary()

    elif user_type == "2":
        load_budget_data()
        print("\nWelcome back, " + username + "!")
        print("a. View summary")
        print("b. Add new expense")
        print("c. Back to main menu")
        option = input("Choose (a/b/c): ").lower()

        if option == "a":
            show_summary()
        elif option == "b":
            add_expense()
            see = input("View summary now? (yes/no): ").lower()
            if see == "yes":
                show_summary()
        elif option == "c":
            print("Returning to main menu...\n")
        else:
            print("Invalid option.\n")
    else:
        print("Invalid choice.\n")


# ---------- MAIN MENU ----------
def mainMenu():
    print("\nWhat features are you feeling today?")
    print("1. Homework Tracker")
    print("2. Budget Tracker")
    print("3. Exit")

    userChoice = input("Please enter your choice (1-3): ").strip()
    return userChoice


def main():
    # show the start menu first
    start_menu()

    # now loop the main menu
    while True:
        userChoice = mainMenu()

        if userChoice == "1":
            homework_tracker()
        elif userChoice == "2":
            budget_tracker()
        elif userChoice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
