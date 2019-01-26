import pyperclip

class User:
    '''
    class that generates new instances of users
    '''
    user_list = []
    def __init__(self,first_name,user_name,password):
        '''__init__ methods helps us define properties for out objects
        '''
       
        self.first_name = first_name
        self.user_name = user_name
        self.password = password
    
    def save_user(self):
        '''save_contact method saves contact objects into contact list
        '''
        User.user_list.append(self)
    
    def delete_user(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        User.user_list.remove(self)
  