# You can implement user interface functions here.
#import social_network
import hashlib

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
    return input("Please Choose a number: " + "\n")

def editAccount():
    print("What would you like to edit?" + "\n")
    print("1. Username")
    print("2. Password")
    print("3. Age")
    print("4. Gender")
    print("5. Friends list")
    print("6. <- Go back ")
    return input("Please Choose a number: " + "\n")

def editUsername():
        #implement function that creates account here; create instance
        username = input("Enter username: ")
        
        # if x > 4: pwd == len(str) x=str(pwd) print("Account created!") else: print("Password not long enough")
        with open("credentials.txt", "w") as f:
            f.write(username + "\n")
        f.close()
        print("Username Changed!")
        "\n"
    


def  editPassword():
        pwd = input("Enter password (must be more than 4 characters): ")
        conf_pwd = input("Confirm password: ")
        
        # if x > 4: pwd == len(str) x=str(pwd) print("Account created!") else: print("Password not long enough")
        
        if conf_pwd == pwd:
            enc = conf_pwd.encode()
            hash1 = hashlib.md5(enc).hexdigest()

        with open("credentials.txt", "w") as f:
            f.write(hash1)
        f.close()
        print("Password Changed!")
        "\n"

def editAge():
        age = input("Enter age: ")
        
        with open("credentials.txt", "w") as f:
            f.write(age + "\n")
        f.close()
        print("Age Changed!")
        "\n"

def editGender():
        gender = input("What is your gender?: ")

        with open("credentials.txt", "w") as f:
            f.write(gender + "\n")
        f.close()
        print("Gender Changed!")
        "\n"

def editFriendslist():
     block = input("Who would you like to block?: ")
     "\n"

def addFriend():
    print("Who would you like to add?: ")
    "\n"
    # user = input("Enter username: ")

def friendslist(self):
    print(self.friends)
    "\n"

def viewMessages():
    print("What message would you like to view?")
    "\n"