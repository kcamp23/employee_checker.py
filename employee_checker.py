# Ignore the whitespace of the user inputs
# Ignore capitalization of characters in the user’s input
# allow all inputs that start with ‘y’ to be a vaild ‘yes’
# allow a user to re-enter if they dont enter yes or no


COMPANY_NAME = "Tech Inc."

EMPLOYEES = ["Alice", "Bob", "Cameron", "Dan", "Ellen", "Frank", "Grace", "Harry"]

# Welcome message + employee names listed out
print("\nWelcome to the " + COMPANY_NAME + " employee check-in\n")
print("We at " + COMPANY_NAME + " are very proud of our employees: ")
for emp_name in EMPLOYEES:
    print("-- " + emp_name)
print("\n")


# user input section (buggy code)
def checker():
    accept = input("Do you work for " + COMPANY_NAME + "?\n(yes/no): ").strip()
    if accept[0] == "y":
        name = input("What is your name?\nName: ").strip()
        for emp_name in EMPLOYEES:
            if name.casefold() == emp_name.casefold():
                print("Thank you " + emp_name + ", you are now checked in.")
                exit()
        print("You're not an employee")
        exit()
    if accept[0] == "n":
        print("This service is not for you. Exiting program...")
        exit()
    if accept[0] != "y" or "n":
        print("Please enter a valid response")
        checker()


checker()
exit()
