
SCHOOL_NAME = "Career devs"

STUDENTS = ["Kat", "Nick", "Bill", "Keith", "Jazlynn", "coralona", "John", "Manny"]

# Welcome message + student list  listed out
print("HELLO CAREER DEVS!!!!! ")
print("\nWelcome to the " + SCHOOL_NAME + " student check-in\n")
for student_name in STUDENTS:
     print("-- " + student_name)
print("\n")


# user input section (buggy code)
def checker():
    accept = input("Do you attend " + SCHOOL_NAME + "?\n(yes/no): ").strip()
    if accept[0] == "y":
        name = input("What is your name?\nName: ").strip()
        for student_name in STUDENTS:
            if name.casefold() == student_name.casefold():
                print("Thank you " + student_name + ", you are now checked in.")
                exit()
        print("You're not a current student ")
        exit()
    if accept[0] == "n":
        print("This service is not for you. Exiting program...")
        exit()
    if accept[0] != "y" or "n":
        print("Please enter a valid response")
        checker()

checker()
exit()
