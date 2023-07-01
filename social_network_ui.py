# You can implement user interface functions here.
import social_network_classes

def mainMenu():
    print("")
    print("1. Create Account")
    print("2. Manage my account")
    print("3. Quit")
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    print("")
    print("1. Edit my details")
    print("2. Add a friend")
    print("3. View all my friends")
    print("4. View all my messages")
    print("5. <- Go back ")
    return input("Please Choose a number: ")

def editAccount():
    print("What would you like to edit?" + "\n")
    print("1. Username")
    print("2. Password")
    print("3. Age")
    print("4. Gender")
    print("5. Friends list")
    print("5. <- Go back ")
    return input("Please Choose a number: ")

def addFriend():
    print("Who would you like to add?: ")
    # user = input("Enter username: ")

def friendslist(self):
    print(self.friends)

def viewMessages():
    print("What message would you like to view?")