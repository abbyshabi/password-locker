import unittest # Importing the unittest module
from user import User # Importing the contact class
import pyperclip

class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the class behaviours.

   '''

    def setUp(self):
        '''
        Set up method to run before each test cases tp check if the class initialized properly
        '''
        self.new_user = User("Oluwadamilola","Shabi","flower12")
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Oluwadamilola")
        self.assertEqual(self.new_user.user_name,"Shabi")
        self.assertEqual(self.new_user.password,"flower12")
     
    def test_save_user(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.new_user.save_user() 
        self.assertEqual(len(User.user_list),1)  

    def test_save_multiple_user(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
            self.new_user.save_user()
            test_user = User("user","user","users") 
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)
            
if __name__ ==  '__main__':
    unittest.main()        

