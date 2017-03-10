#!usr/bin/env python3

from account import Account
from customer import Customer
from accounts.savings import Savings
from accounts.checkings import Checkings
from accounts.retirement import Retirement

def print_menu():
    print("A: Create customer")
    print("B: View all customers")
    print("C: View customer data by userID")
    print("D: Access customer accounts by userID")
    print("E: Access customer accounts by list")
    print("F: View all bank accounts")
    print("Q: Quit the program")

def create_customer():
    firstName = input("Please enter your first name: ")
    lastName = input("Pleaase enter your last name: ")

    Customer(firstName, lastName)

#TODO: Check for empty dictionaries
def view_all_customers():
    for customer in Customer.customerLookup:
        print(Customer.customerLookup[customer])

#TODO: Add default option for key not found (Also empty dictionary)
def option_c():
    userID = input("Please enter the user's ID number: ")

    #TODO: Will include all accounts later
    print(Customer.customerLookup[int(userID)])

def option_d():
    print("Option D")

def option_e():
    print("Option E")

def main():
    quit = False

    while(quit == False):
        print_menu()

        while True:
            switch = input("\nSelect a menu option: ")

            if switch.upper() == "A":
                create_customer()
            elif switch.upper() == "B":
                view_all_customers()
            elif switch.upper() == "C":
                option_c()
            elif switch.upper() == "D":
                option_d()
            elif switch.upper() == "E":
                option_e()
            elif switch.upper() == "F":
                option_f()
            elif switch.upper() == "Q":
                quit = True
                break
            else:
                print("Please choose a valid menu option!")


if __name__ == '__main__':
    main()
