#!/usr/bin/env python3.6
from user import User
from credentials import Credentials

def create_user(fname, uname, password):
    '''
    This is a function to create a new user
    '''
    new_user = User(fname , uname, password)
    return new_user

def save_user(user):
    '''
    This function saves a new user
    '''
    user.save_user()

#def check_user(user):
    '''
   This function verifies a user before giving access 
    '''
 #   checking_user= User.check_user(user_name,password)

def del_user(user):
    '''
    This function deletes a user 
    '''
    user.delete_user()

def create_new_credential(user_account, account_password):
    ''' 
    This function allows a user create a new credential account
    '''
    new_credential = Credentials(user_account , account_password)
    return new_credential

def save_new_credentials(credential):
    ''' 
    This is a function to save new credentials created 
    '''
    credential.save_credentials()

def delete_credentials(credential):
    '''
    This is a function to delete credentials by the user 
    '''
    return Credentials.delete_credential(credential)

def verify_user(user_name,password):
	'''
	Function that checks if the username already exists in the system
	'''
	checking_user = Credential.check_user(user_name,password)
	return checking_user
 
#def find_credentials(name):
 #   '''

 #   '''
   # return Credentials.find_by_name(user_account)

#def check_existing_credentials(name):
#    '''
 #   '''
 #   return Credentials.find_by_name(name)

def display_credentials():
    '''
    Function to display credentials of an account
    '''
    return Credentials.display_credential()

def main():
      print("")
      print("")
    
      print("                                           WELCOME TO THE .....|| ")  
      print("                                                               ||  ")
      print("                                                               ||  ")
      print("                                                               vv ")
      print("'                                                                           /$$       /$$                        /$$                        /$$")
      print("'                                                                          | $$      | $$                       | $$                       | $$")
      print("'    /$$$$$$  /$$$$$$  /$$$$$$$/$$$$$$$/$$  /$$  /$$ /$$$$$$  /$$$$$$  /$$$$$$$      | $$       /$$$$$$  /$$$$$$| $$   /$$ /$$$$$$  /$$$$$$| $$")
      print("'   /$$__  $$|____  $$/$$_____/$$_____| $$ | $$ | $$/$$__  $$/$$__  $$/$$__  $$      | $$      /$$__  $$/$$_____| $$  /$$//$$__  $$/$$__  $| $$")
      print("'  | $$  \ $$ /$$$$$$|  $$$$$|  $$$$$$| $$ | $$ | $| $$  \ $| $$  \__| $$  | $$      | $$     | $$  \ $| $$     | $$$$$$/| $$$$$$$| $$  \__|__/")
      print("'  | $$  | $$/$$__  $$\____  $\____  $| $$ | $$ | $| $$  | $| $$     | $$  | $$      | $$     | $$  | $| $$     | $$_  $$| $$_____| $$         ")
      print("'  | $$$$$$$|  $$$$$$$/$$$$$$$/$$$$$$$|  $$$$$/$$$$|  $$$$$$| $$     |  $$$$$$$      | $$$$$$$|  $$$$$$|  $$$$$$| $$ \  $|  $$$$$$| $$      /$$")
      print("'  | $$____/ \_______|_______|_______/ \_____/\___/ \______/|__/      \_______/      |________/\______/ \_______|__/  \__/\_______|__/     |__/")
      print("'  | $$                                                                                                                                        ")
      print("'  | $$                                                                                                                                        ")
      print("'  |__/                                                                                                                                        ")

      print(" ")

      print(" please what is your name?")
      first_name = input()

      print(f" Hello {first_name} what would you like to do today?")
      print (" ")

      while True:  
          print("Please use the following short codes :\n cc - to create a new account  ,\n  da - to diplay existing account ,\n fa - to find an existing account name , \n ex to exit password locker")
          short_code = input().lower()

     
          if short_code == "cc":
        
               print ("-"*15)
               print (" ")
               print ("To create a new user account: ")
               first_name = input("Please enter your first name:-  ")
               user_name = input("Please enter your preferred username :-  ")
               password = str(input ("Please enter your desired password:- "))

               save_user(create_user(first_name,user_name,password))
               print("")
               print(f"New account has been created for : {first_name} \n with username :{user_name} \n using password: {password}")

               
               

          elif short_code == "ex":
               print("Bye....we hope you again visit soon")
               break

               
            

if __name__ == '__main__':

    main()               