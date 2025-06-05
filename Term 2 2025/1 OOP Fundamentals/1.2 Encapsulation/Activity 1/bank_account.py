class BankAccount:
    def __init__(self, account_number, balance, owner_name):
        self._account_number = account_number
        self._balance = balance
        self._owner_name = owner_name


    def get_account_number(self):
        return self._account_number
    
    def get_balance(self):
        return self._balance
    
    def get_owner_name(self):
        return self._owner_name
    

    def set_account_number(self, new_account_number):
        if isinstance(new_account_number, int):
            if len(str(new_account_number)) == 6:
                self._account_number = new_account_number
    
    def set_balance(self, new_balance):
        if isinstance(new_balance, float):
            self._balance = new_balance

    def set_owner_name(self, new_owner_name):
        if isinstance(new_owner_name, str):
            self._owner_name = new_owner_name