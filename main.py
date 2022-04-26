# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
# Ignore the whitespace of the user inputs
# Ignore capitalization of characters in the user’s input
# allow all inputs that start with ‘y’ to be a vaild ‘yes’
# allow a user to re-enter if they dont enter yes or no




COMPANY_NAME = "Tech Inc."

EMPLOYEES = ["Alice", "Bob", "Cameron", "Dan", "Ellen", "Frank", "Grace", "Harry"]

# Welcome message + employee names listed out
print("\nWelcome to the "+COMPANY_NAME+" employee check-in\n")
print("We at " + COMPANY_NAME + " are very proud of our employees: ")
for emp_name in EMPLOYEES:
    print("-- "+emp_name)
print("\n")

# user input section (buggy code)
accept = input("Do you work for " + COMPANY_NAME + "?\n(yes/no): ")
if accept.casefold().strip() == "yes":
    name = input("What is your name?\nName: ").strip()
    for emp_name in EMPLOYEES:
       if name.casefold() == emp_name.casefold():
            print("Thank you " + emp_name + ", you are now checked in.")
            if name.casefold() != emp_name.casefold():
                print("You're not an employee")

else:
    print("This service is not for you. Exiting program...")
    exit()
