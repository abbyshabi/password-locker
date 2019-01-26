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
        self.new_credential = Credentials('Twitter','fog123')

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.user_account,"Twitter")
        self.assertEqual(self.new_credential.account_password,"fog123")  

    def test_save_credential(self):
        '''
        test_save_contact test case to test if  credentials object are saved into
         the credential list
        '''
        self.new_credential.save_credential() 
        self.assertEqual(len(Credentials.credential_list),1)  
    
    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
            self.new_credential.save_credential()
            test_credential = Credentials("user","user123") 
            test_credential.save_credential()
            self.assertEqual(len(Credentials.credential_list),2)

    def tearDown(self):
        """
        The tear down method cleans up credential list after each test has been run
        """
        Credentials.credential_list = []
    
    def test_delete_credential(self):
            '''
            This to test if we can remove an account from our credential list
            '''
            self.new_credential.save_credential()
            test_credential = Credentials("user","test123") 
            test_credential.save_credential()

            self.new_credential.delete_credential()
            self.assertEqual(len(Credentials.credential_list),1)
    
    def test_find_contact_by_name(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credentials("Twitter","dog123") # new contact
        test_credential.save_credential()

        found_credential = Credentials.find_by_name("Twitter")

        self.assertEqual(found_credential.user_account,test_credential.user_account)

if __name__ ==  '__main__':
    unittest.main() 
