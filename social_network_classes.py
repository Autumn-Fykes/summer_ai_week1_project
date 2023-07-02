import hashlib

# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
              def __init__(self, id, username, age, gender, friends, inbox, list_of_people):
                self.id = id
                self.name = username
                self.year = age
                self.gender = gender
                self.friends = []
                self.inbox = []
                self.list_of_people = []

    user2 = SocialNetwork(27, "Autumn", 17, "female", [12, 1980, 7])
        # with open('credentials.txt') as file: self.list_of_people = [line.strip() for line in file 
        # this instance variable is initialized to an empty list when social network is created, 
                         # you can save objects of people on the network in this list
    
    ## For more challenge try this
    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass

    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        pass

    def  create_account(self):
        #implement function that creates account here; create instance
        username = input("Enter username: ")
        pwd = input("Enter password (must be more than 4 characters): ")
        conf_pwd = input("Confirm password: ")
        
        # if x > 4: pwd == len(str) x=str(pwd) print("Account created!") else: print("Password not long enough")
        
        if conf_pwd == pwd:
            enc = conf_pwd.encode()
            hash1 = hashlib.md5(enc).hexdigest()

        with open("credentials.txt", "w") as f:
            f.write(username + "\n")
            f.write(hash1)
        f.close()
        print("Account created!")



class Person(object):
    def __init__(self, id, username, age, gender, friends, inbox):
        self.id = id
        self.name = username
        self.year = age
        self.gender = gender
        self.friends = []
        self.inbox = []

user1 = Person(27, "Autumn", 17, "female", [12, 1980]) 

print(user1)

def is_friend(id1, id2):
    # if (id1 in People.friends) & (id2 in People.friends):
        # return True

    def add_friend(self):
        #implement adding friend. Hint add to self.friendlist; create remove from friendlist; add person object
        pass

    def send_message(self):
        #implement sending message to friend here; also create a block; add friend name and message
        pass
