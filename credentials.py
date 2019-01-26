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
def find_by_name(cls, user_account):
        """Method that takes in a name and returns a credential that matches that particular name
        Args:
            name: account_name that has a password
        Returns:
            The account_name and it's corresponding PassWord
        """

        for credential in cls.credential_list:
            if credential.user_account == user_account:
                return credential