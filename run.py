#!/usr/bin/env python3.6
from user import User
from credentials import Credentials

def create_user(name, username, password):
    '''
    This is a function to create a new user
    '''
    new_user = User(name , username, password)
    return new_user

def save_user(user):
    '''
    This function saves a new user
    '''
    user.save_user()

def del_user(user):
    '''
    This function deletes a user 
    '''
    user.delete_user()

def find_credentials(name):
    '''

    '''


def display_credentials():
    '''
    Function to display credentials of an account
    '''