#!usr/bin/env python3

from account import Account
from customer import Customer
from accounts.savings import Savings
from accounts.checkings import Checkings
from accounts.retirement import Retirement

def print_menu():
    print("A: Create customer")
    print("B: View all customers")
    print("C: Access customer by userID")
    print("D: Access customer accounts by list")
    print("E: View all bank accounts")
    print("Q: Quit the program")

def option_a():
    firstName = input("Please enter your first name: ")
    lastName = input("Pleaase enter your last name: ")

    Customer(firstName, lastName)

def option_b():
    print(Customer.customerLookup)

def option_c():
    print("Option C")

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
                option_a()
            elif switch.upper() == "B":
                option_b()
            elif switch.upper() == "C":
                option_c()
            elif switch.upper() == "D":
                option_d()
            elif switch.upper() == "E":
                option_e()
            elif switch.upper() == "Q":
                quit = True
                break
            else:
                print("Please choose a valid menu option!")


if __name__ == '__main__':
    main()
