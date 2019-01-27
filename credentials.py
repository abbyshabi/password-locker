import pyperclip
import random
import string

class Credentials:
    ''' The credentials class would hold all the information of the user
    '''
    credential_list = []
    def __init__(self,user_account,account_password):
         self.user_account = user_account
         self.account_password = account_password

    def save_credential(self):
        '''save_credential method saves credential objects into credential list
        '''
        Credentials.credential_list.append(self)

    def delete_credential(self):

        '''
        delete_credential method deletes a saved account from the credential_list
        '''

        Credentials.credential_list.remove(self)

    @classmethod
    def find_by_name(cls,user_account):
        '''
        '''
        for credential in cls.credential_list:
            if credential.user_account == user_account:
                return credential

    @classmethod
    def display_credential(cls):
        """
        Method which displays all credentials list
        """
        return cls.credential_list

    def generate_password(stringLength=8,char= string.ascii_letters+string.digits):
      '''
      '''

      gen_pass = ''.join(random.choice(char) for i in range(stringLength))
      return gen_pass

    @classmethod
    def credential_exists(cls,name):
        """
        This method would check if a certain credential exists
        """
        for credential in cls.credential_list:
            if credential.user_account == name:
                return True
            return False

