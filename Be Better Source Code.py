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
    global userName, userMajor, userYearofGraduation, profileUserFile 
    f = open(profileFilename, "r")
    lines = f.readlines()
    f.close()

    if len(lines) >= 3:
        userName = lines[0].strip()
        userMajor = lines[1].strip()
        userYearofGraduation = lines[2].strip()

def saveUserProfile():
    global userName, userMajor, userYearofGraduation
    f = open(profileFilename, "w")
    f.write(userName + "\n")
    f.write(userMajor + "\n")
    f.write(userYearofGraduation + "\n")
    f.close()


def setupNewUser():
    #This is used to ask the user to enter profile information and then save it
    global userName, userMajor, userYearofGraduation
    print("\nWelcome new User, Let's set up your account.")
    userName = input("Enter your name: ").strip()
    userMajor = input("Enter your major: ").strip()
    userYearofGraduation = input("Enter your year of graduation: ").strip()
    saveUserProfile()
    print("\nProfile saved. Welcome, " + userName + "!\n")


# This is the start menu for our overall code
def startMenu():
    #Start menu: welcome the user, then try to reload session for a returning user or set up if it is a new profile
    print("_________________________________")
    print("  Welcome to Be Better! ")
    print("  A Smart Planner for Students  ")
    print("_________________________________\n")

    print("Have you used Be Better on this computer before?")
    userAnswer = input("Enter yes or no: "). lower()

    if userAnswer == "yes":
        loadUserProfile()
        print("Reloading your last session for " + userName + "..." + "\n")
        print("Name: " + userName)
        print("Major: " + userMajor)
        print("Graduation Year: " + userYearofGraduation + "\n")
    else:
        print("Hey new user we are so excited you're here, let's set up your account.\n")
        setupNewUser()


# Second feature of our code; Homework Tracker
homeworkList = []  # each item: {"title","course","due","completed"}


def homeworkTracker():
    print("\n--- Homework Tracker ---")
    print("a. Create Assignment")
    print("b. Task Completed!")
    print("c. See all Assignments")

    choice = input("Choose an option (a/b/c): ").strip().lower()

    if choice == "a":
        createAssignment()
    elif choice == "b":
        markAssignmentCompleted()
    elif choice == "c":
        seeAllAssignments()
    else:
        print("Invalid choice.")


def createAssignment():
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

    homeworkList.append(assignment)
    print("Assignment created")


def markAssignmentCompleted():
    if len(homeworkList) == 0:
        print("You don't have any assignments yet.")
        return

    print("\n-- Mark Assignment Completed --")
    index = 0
    while index < len(homeworkList):
        hw = homeworkList[index]
        if hw["completed"]:
            statusText = "Done"
        else: statusText = "pending"
        print(str(index + 1) + ". " + hw["title"] +
              " | Course: " + hw["course"] +
              " | Due: " + hw["due"] +
              " | Status: " + statusText)
        index = index + 1

    choice = input("Which assignment is completed? (number): ").strip()
    valid = True
    i = 0 
    while i < len(choice):
        if choice[i] not in "0123456789":
            valid = False
        i = i + 1

    if valid == False:
        print("Invalid input")
        return
        
    selection = int(choice) - 1
    if selection < 0 or selection >= len(homeworkList):
        print("Invalid choice.")
        return

    homeworkList[selection]["completed"] = True

    messages = [
        "You did it! Task conquered!",
        "Great job, keep going!",
        "Another assignment off the list!",
        "Nice work, you're staying on top of it!"
    ]
    mot = random.choice(messages)
    print("Yay!!! Assignment completed")
    print(mot)


def seeAllAssignments():
    if len(homeworkList) == 0:
        print("No homework yet. Add an assignment to get started.")
        return

    print("\n-- All Assignments --")
    for hw in homeworkList:
        if hw["completed"]:
            statusText = "Done"
        else:
            statusText = "pending"
        line = "- " + hw["title"]
        line += " | Course: " + hw["course"]
        line += " | Due: " + hw["due"]
        line += " | Status: " + statusText
        print(line)

    count = len(homeworkList)
    binaryCount = bin(count)
    print("\nYou currently have " + str(count) + " assignment(s).")
    print("In binary, that is : " + binaryCount)

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


def saveBudgetData():
    # this saves the user's income and expenses into their file
    global income, expensesList, currentFile

    f = open(currentFile, "w")
    f.write(str(income) + "\n")

    for expense in expensesList:
        line = expense["name"] + "|" + str(expense["amount"]) + "\n"
        f.write(line)

    f.close()


def showSummary():
    # this shows the income, the list of all the expenses, the total spent and the remaining money/what is left
    global income, expensesList

    print("\n_-_-_- ACCOUNT SUMMARY _-_-_-")
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

    print("\n-_-_- Add a New Expense -_-_-")
    name = input("Enter expense name: ")
    userAmount = input("Enter expense amount: ")

    amount = float(userAmount)

    expensesList.append({"name": name, "amount": amount})
    saveBudgetData()
    print("Success, Expense added.\n")


def budgetTracker():
    # this is the main part for the budget tracker function
    global income, expensesList, currentFile

    print("\n-_-_- BUDGET TRACKER -_-_-")
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

        print("\n-_-_- Budget Setup -_-_-")
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

#this is used to get the user;s choice and display the menu for the program
def mainMenu():
    print("\nWhat features are you feeling today?")
    print("1. Homework Tracker")
    print("2. Budget Tracker")
    print("3. Exit")

    userChoice = input("Please enter your choice (1-3): ").strip()
    return userChoice


def main():
    #this is so that the start menu would be displayed first
    startMenu()

#this is the loop created to go through the main menu when the user makes their choice
    while True:
        userChoice = mainMenu()

        if userChoice == "1":
            homeworkTracker()
        elif userChoice == "2":
            budgetTracker()
        elif userChoice == "3":
            print("Goodbye, we hope you use Be Better another time")
            break
        else:
            print("Oopsie, Invalid option. Please try again.")


if __name__ == "__main__":
    main()




