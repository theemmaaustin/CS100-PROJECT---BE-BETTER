# ________________________________________________________________________________
# BE BETTER - This is a Smart Student Planner
# Team Members: David Oladapo, Emmanuella Austin-Gabriel
# Features: Goal Tracker, Homework Tracker, Budget Tracker
# ___________________________________________________________________________________

import random   # this is used for randomizing motivational messages for the homework feature

#Global user/profile variables 
userName = ""
userMajor = ""
userYearofGraduation = ""

profileFilename = "userProfile.txt"  


#This is our user profile functions
def loadUserProfile():
    global userName, userMajor, userYearofGraduation
    profileUserFile = open("userProfile.txt", "r")
    lines = profileUserFile.readlines()
    profileUserFile.close()

    if len(lines) >= 3:
        userName = lines[0].strip()
        userMajor = lines[1].strip()
        userYearofGraduation = lines[2].strip()

def saveUserProfile():
    '''This is for us to save the current user profile to file'''
    global userName, userMajor, userYearofGraduation
    f = open(PROFILE_FILENAME, "w")
    f.write(userName + "\n")
    f.write(userMajor + "\n")
    f.write(userYearofGraduation + "\n")
    f.close()


def setupNewUser():
    '''This is used to ask the user to enter profile information and save it'''
    global userName, userMajor, userYearofGraduation
    print("\nWelcome new User, Let's set up your account.")
    userName = input("Enter your name: ").strip()
    userMajor = input("Enter your major: ").strip()
    userYearofGraduation = input("Enter your year of graduation: ").strip()
    saveUserProfile()
    print("\nProfile saved. Welcome, " + userName + "!\n")


# This is the start menu for our overall code
def start_menu():
    '''Start menu: welcome the user, then try to reload session for a returning user or set up if it is a new profile'''
    print("_________________________________")
    print("  Welcome to Be Better! ")
    print("  A Smart Planner for Students  ")
    print("_______________________________________\n")

    profileLoaded = loadUserProfile()
    if profileLloaded:
        print("Reloading your last session for " + userName + "..." + "\n")
        print("Name: " + userName)
        print("Major: " + userMajor)
        print("Graduation Year: " + userYearofGraduation + "\n")
    else:
        print("Hey new user we are so excited you're here, let's set up your account.\n")
        setupNewUser()


# Second feature of our code; Homework Tracker
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
        if hw["completed"]:
            status_text = "Done"
        else: status_text = "pending"
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
        if hw["completed"]:
            status_text = "Done"
        else:
            status_text = "pending"
        line = "- " + hw["title"]
        line += " | Course: " + hw["course"]
        line += " | Due: " + hw["due"]
        line += " | Status: " + status_text
        print(line)

    count = len(homework_list)
    binary_count = bin(count)
    print("\nYou currently have " + str(count) + " assignment(s).")
    print("In binary, that is: " + binary_count)


#last feature; Budget Tracker
income = 0.0
expensesList = []
currentFile = ""


def loadBudgetData():
    # this first line is written to load the income and expense that were saved for this user
    global income, expensesList, currentFile

    income = 0.0
    expensesList = []

    f = open(currentFile, "r")
    lines = f.readlines()
    f.close()

    if len(lines) == 0:
        return

    incomeLine = lines[0].strip()
    if incomeLine != "":
        income = float(incomeLine)

    #the file is used to store expenses using this format in our code: name|amount (example: Games|33)
    for line in lines[1:]:
        line = line.strip()
        if line != "":
            parts = line.split("|")
            if len(parts) == 2:
                name = parts[0]
                amountText = parts[1]
                amount = float(amountText)
                expensesList.append({"name": name, "amount": amount})


'''def saveBudgetData():
    # this saves the user's income and expenses into their file
    global income, expensesList, currentFile

    f = open(currentFile, "w")
    f.write(str(income) + "\n")

    for expense in expensesList:
        line = expense["name"] + "|" + str(expense["amount"]) + "\n"
        f.write(line)'''

    f.close()


def showSummary():
    # this shows the income, the list of all the expenses, the total spent and the remaining money/what is left
    global income, expensesList

    print("\n=== ACCOUNT SUMMARY ===")
    print("Income: " + str(income))

    totalExpenses = 0.0

    if len(expensesList) == 0:
        print("No expenses yet.")
    else:
        print("\nExpenses:")
        for expense in expensesList:
            print("- " + expense["name"] + ": " + str(expense["amount"]))
            totalExpenses = totalExpenses + expense["amount"]

    remaining = income - totalExpenses

    print("\nTotal Expenses: " + str(totalExpenses))
    print("Remaining Money: " + str(remaining))
    print("")


def addExpense():
    # this is for asking a user for one expense and then saving it
    global expensesList

    print("\n--- Add a New Expense ---")
    name = input("Enter expense name: ")
    userAmount = input("Enter expense amount: ")

    amount = float(userAmount)

    expensesList.append({"name": name, "amount": amount})
    saveBudgetData()
    print("Success, Expense added.\n")


def budgetTracker():
    # this is the main part for the budget tracker function
    global income, expensesList, currentFile

    print("\n=== BUDGET TRACKER ===")
    print("Are you:")
    print("1. A new user")
    print("2. A returning user")
    userType = input("Choose an option (1/2): ")

    username = input("Enter your name (with no spaces please): ")
    currentFile = username + "_budget.txt"

    # When it is a new user the following will happen
    if userType == "1":
        print("\nDo you currently have:")
        print("1. Income only")
        print("2. Savings only")
        print("3. Both income and savings")
        print("4. None (start at 0)")
        moneyChoice = input("Choose an option (1/2/3/4): ")

        print("\n--- Budget Setup ---")
        if moneyChoice == "1" or moneyChoice == "3":
            newUserinc = input("Enter your income: ")
            income = float(newUserinc)
        else:
            income = 0.0

        saveBudgetData()

        print("\nNow let's add your expenses.")
        while True:
            addExpense()
            moreAddition = input(" Do you want to add another expense? (yes/no): ").lower()
            if moreAddition != "yes":
                break

        showSummary()

    # If the user is a reoccurring user then the following will run
    elif userType == "2":
        # if the option '2' is selected then a file should already exist for that particular user
        loadBudgetData()

        print("\nWelcome back, " + username + "!")
        print("a. View summary")
        print("b. Add a new expense")
        print("c. Back to main menu")
        option = input("Choose (a/b/c): ").lower()

        if option == "a":
            showSummary()
        elif option == "b":
            addExpense()
            see = input("Do you want to view summary now? (yes/no): ").lower()
            if see == "yes":
                showSummary()
        elif option == "c":
            print("Returning to main menu...\n")
        else:
            print("Sorry. This is an Invalid option.\n")

    else:
        print("Sorry. This is an Invalid choice.\n")


def showMainMenu():
    # this prints the main menu and gets the user's choice
    print("\nWhat features are you feeling today?")
    print("1. Goal Tracker")
    print("2. Homework Tracker")
    print("3. Budget Tracker")
    print("4. GPA Calculator")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")
    return choice


def main():
    # this is the main function that runs the whole Be Better planner
    global userName, userMajor, userYearOfGraduation, Goals_List

    print("Welcome to Be Better!")

    print("Have you used Be Better on this computer before?")
    answer = input("Enter yes or no: ").lower()

    if answer == "yes":
        print("Reloading your last session...")
        loadUserProfile()
        # Goals_List is already a list, homework_list and expensesList
        # are handled in their own sections
    else:
        print("Welcome new user, let's set up your account.")
        userName = input("Enter your name: ")
        userMajor = input("Enter your major: ")
        userYearOfGraduation = input("Enter your year of graduation: ")

        Goals_List = []   # empty goals list for now
        saveUserProfile()


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



