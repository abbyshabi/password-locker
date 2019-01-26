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
    