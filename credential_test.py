import unittest
from credentials import Credentials

class TestCredential(unittest.TestCase):
    '''
        The test credential class defines test cases for the credential class
    '''

    def setUp(self):
        """
        The setUp method will run before each test case
        """
        self.new_account = Credentials('Twitter','fog123')

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.account_name,"Twitter")
        self.assertEqual(self.new_account.password,"fog123")  

     def test_save_account(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.new_account.save_account() 
        self.assertEqual(len(account.account_list),1)    

