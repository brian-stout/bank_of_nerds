# This module contains all the functions which handle menu logic
# and user input

from bank import Bank
from customer import Customer

from accounts.savings import Savings
from accounts.checkings import Checkings
from accounts.retirement import Retirement

"""
    The main menu that shows when the program first starts
"""


def print_bank_menu():
    print("\nA: Create customer")
    print("B: View all customers")
    print("C: View customer data by userID")
    print("D: Access customer accounts by userID")
    print("Q: Quit the program")

"""
    This menu apppears when user selects an account in option D
"""


def print_account_menu(account):
    print("Account Name:" + account.accountName)
    print("Type: " + account.accountType)
    print("Account ID: " + str(account.actID))
    print("Balance: " + str(account.moneyInAccount) + "$")

    print("\nA: Deposit money to account")
    print("B: Withdraw money from account")
    print("Q: Main Menu\n")

"""
    This function handles the logic used to withdraw, deposit money after
        a user has selected a bank account from option D in the main menu
"""


def access_accounts(bank, customer, account):
    print_account_menu(account)

    while True:
        switch = input("Please select an option ")
        if switch.upper() == "A":
            while True:
                print("How much money would you like to deposit?", end=' ')
                print("(Q to back out)")
                amount = input("deposit: ")
                if amount.upper() == "Q":
                    break
                elif amount.isdigit():
                    account.deposit(int(amount))
                    break
                else:
                    print("Please enter a valid input")
            break
        elif switch.upper() == "B":
            while True:
                print("How much money would you like to withdraw?", end=' ')
                print("(Q to back out)")
                amount = input("withdrawal: ")
                if amount.upper() == "Q":
                    break
                elif amount.isdigit():
                    account.withdraw(int(amount), customer)
                    break
                else:
                    print("Please enter a valid input")
            break
        elif switch.upper() == "Q":
            break
        else:
            print("Please enter a valid input")

"""
    Function is called when the user select option A, and grabs user input
        to create a new customer object and add it to the bank
"""


def create_customer(bank):

    firstName = input("Please enter your first name: ")
    lastName = input("Pleaase enter your last name: ")
    while True:
        userAge = input("Please enter you age: ")
        if userAge.isdigit():
            break
        else:
            print("Not a valid age!")

    userAge = int(userAge)
    customer = Customer(firstName, lastName, userAge, bank.numberOfCustomerIDs)

    # By default the bank creates a checkings and savings account
    customer.accounts.append(create_account(bank, "Checkings", "Checkings Act"))
    customer.accounts.append(create_account(bank, "Savings", "Savings Act"))

    bank.add_customer(customer)

"""
    The create_account() function makes a new account based on a
        arbitrary name and the account type.

    By default it's called upon customer creation, but can also be used
        to create new accounts.
"""


def create_account(bank, actType, name):
    actID = bank.numberOfAccounts

    if actType == "Checkings":
        newAccount = Checkings(name, actID)
    elif actType == "Savings":
        newAccount = Savings(name, actID)
    elif actType == "Retirement":
        newAccount = Retirement(name, actID)

    bank.add_account(newAccount)

    return bank.accountLookup.get(actID)

"""
    The view_customer_data() function is called upon option C in the main menu.
        Based on an inputted user ID, it pulls up the First and
        Last name of a user
"""


def view_customer_data(bank):
    userID = input("Please enter the user's ID number: ")
    userID = int(userID)

    customer = bank.customer_lookup(userID)
    if customer:
        print(customer)
    else:
        print("UserID does not exist")

"""
    When the user selects the option to create a new account when he views
        a user's accounts based on the ID,  this menu guides the user
        through the account creation process.
"""


def create_account_menu(bank, customer):
    print("A. For a checkings account")
    print("B. For a savings account")
    print("C. For a retirement account")
    print("Q. Main Menu")

    while True:
        switch = input("Choose an options: ")

        if switch.upper() == "A":
            actType = "Checkings"
            break
        elif switch.upper() == "B":
            actType = "Savings"
            break
        elif switch.upper() == "C":
            actType = "Retirement"
            break
        elif switch.upper() == "Q":
            return None
        else:
            print("Please input a valid option!")

    name = input("Name your account: ")

    newAccount = create_account(bank, actType, name)
    customer.add_account(newAccount)

"""
    The access_user_accounts() function is ran when the user
        selects option D in the main menu.  It prompts the user
        to enter a UserID, then shows all the user's accounts.

    The user then has the option to enter the accounts, or create
        a new account.
"""


def access_user_accounts(bank):
    userID = input("Please enter the user's ID number: ")
    customer = bank.customer_lookup(int(userID))
    if customer is None:
        print("User ID does not exist")
        return None

    print("\nAll of the user's accounts")
    customer.print_accounts()

    print("\nInput a number to access an account")
    print("A. Create a new account")
    print("Q. Main menu")

    while True:
        switch = input("Choose an option: ")

        if switch.isdigit():
            try:
                userAccount = customer.accounts[int(switch) - 1]
            except IndexError:
                print("Not a valid option")
                continue
            access_accounts(bank, customer, userAccount)
            break

        elif switch.upper() == "A":
            create_account_menu(bank, customer)
            break
        elif switch.upper() == "Q":
            break
        else:
            print("Not a valid option")
