username = input('username: ')

if len(username) <= 8 and username.isalpha() == True:
    print('username accepted')
else: 
    print('username rejected')