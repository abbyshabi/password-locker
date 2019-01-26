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
 
#def find_credentials(name):
    '''

    '''
   # return Credentials.find_by_name(user_account)

#def check_existing_credentials(name):
    '''
    '''
 #   return Credentials.find_by_name(name)

def display_credentials():
    '''
    Function to display credentials of an account
    '''
    return Credentials.display_credential()

    def main():
      print("This is the Password Locker! Hello and welcome ")  