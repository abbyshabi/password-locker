import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    The user test class will be used to test all the instances of the user class
    '''
    def setUp(self):
     ''' The Setup methoid will run before each test case is conducted
     '''

     def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Oluwadamilola")
        self.assertEqual(self.new_user.user_name,"Shabi")
        self.assertEqual(self.new_user.password,"flower12")

