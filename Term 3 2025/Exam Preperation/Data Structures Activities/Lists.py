shoppingList = ['milk', 'bread', 'eggs']

while True:
    option = input('would you like to add an item, remove, or view list: ')
    if int(option) == 0:
        shoppingList.append(input('what item: '))
    if int(option) == 1:
        shoppingList.remove(input('what item: '))
    if int(option) == 2:
        print(shoppingList)