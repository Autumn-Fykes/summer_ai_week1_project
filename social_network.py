#Various import Statements can go here
from  social_network_classes import SocialNetwork
import social_network_ui



#Create instance of main social network object
ai_social_network = SocialNetwork()

#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            ai_social_network.create_account()

        elif choice == "2":
            inner_menu_choice = social_network_ui.manageAccountMenu()
            #inner menu
            if inner_menu_choice == "1":
                inner_menu_choice = social_network_ui.editAccount()
                if inner_menu_choice == "1":
                    inner_menu_choice == social_network_ui.editUsername()
                elif inner_menu_choice == "2":
                    inner_menu_choice = social_network_ui.editPassword()
                elif inner_menu_choice == "3":
                    inner_menu_choice = social_network_ui.editAge()
                elif inner_menu_choice == "4":
                    inner_menu_choice = social_network_ui.editGender()
                elif inner_menu_choice == "5":
                    inner_menu_choice = social_network_ui.editFriendslist()
                elif inner_menu_choice == "6":
                    inner_menu_choice = social_network_ui.editAccount()

            elif inner_menu_choice == "2":
                inner_menu_choice = social_network_ui.addFriend()
            
            elif inner_menu_choice == "3":
                inner_menu_choice == social_network_ui.friendslist()
            
            elif inner_menu_choice == "4":
                inner_menu_choice == social_network_ui.viewMessages()

            while True:
                if inner_menu_choice == "5":
                    break
                else:
                    inner_menu_choice = social_network_ui.manageAccountMenu()

        elif choice == "3":
            print("Thank you for visiting. Goodbye")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()



        
