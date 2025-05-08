import bank_account

def withdraw(balance, withdraw):
    if balance >= float(withdraw):
        post_withdraw_balance = balance - float(withdraw)
        return post_withdraw_balance
    
def deposit(balance, deposit):
    post_deposit_balance = balance + float(deposit)
    return post_deposit_balance

def accountManagement():
    name = input('name: \n')
    number = input('number with 6 digits: \n')
    bankAccount = bank_account.BankAccount(number, 0.0, name)
    exit = False
    while exit != True:
        choice = input('withdraw or deposit: \n')
        if choice == 'withdraw':
            withdrawAmount = input('how much to withdraw: \n')
            bankAccount.set_balance = withdraw(bankAccount.get_balance(), withdrawAmount)
        if choice == 'deposit':
            depositAmount = input('how much to deposit: \n')
            bankAccount.set_balance = deposit(bankAccount.get_balance(), depositAmount)
        exit = input('exit: \n')


bankAccount = bank_account.BankAccount(12345, 27.0, 'FRED')

print(bankAccount.get_account_number())

print(bankAccount.get_balance())

print(bankAccount.get_owner_name())

bankAccount.set_account_number(54321)
print(bankAccount.get_account_number())

bankAccount.set_balance(28.0)
print(bankAccount.get_balance())

bankAccount.set_owner_name('CHRIS')
print(bankAccount.get_owner_name())

bankAccount2 = bank_account.BankAccount(654321, 2700000000.0, 'Frederick')

print(bankAccount2.get_account_number())

print(bankAccount2.get_balance())

print(bankAccount2.get_owner_name())

bankAccount2.set_account_number(654321)
print(bankAccount2.get_account_number())

bankAccount2.set_balance(2800000000.0)
print(bankAccount2.get_balance())

bankAccount2.set_owner_name('Christopher')
print(bankAccount2.get_owner_name())



accountManagement()