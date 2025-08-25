phone_book = {}

while True:
    userChoice = int(input('Add contact, look up, or delete contact: '))
    if userChoice == 0:
        contactName = input('contact name: ')
        contactNumber = input('contact number: ')

        phone_book[contactName] = contactNumber
    elif userChoice == 1:
        contactName = input('contact name: ')
        print(phone_book[contactName])
    elif userChoice == 2:
        contactName = input('contact name: ')
        del phone_book[contactName]