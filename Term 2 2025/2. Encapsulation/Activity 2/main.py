import create_character

# Create the two characters
character0 = create_character.CreateCharacter('Dave', 'Wizard', 12) 
character1 = create_character.CreateCharacter('Tom', 'Barbarian', 7)

# Print the name saved in the class
print(f'character0 name: {character0.get_name()}')
print(f'character1 name: {character1.get_name()}')

# Print the classtype saved in the class
print(f'character0 classtype: {character0.get_classtype()}')
print(f'character1 classtype: {character1.get_classtype()}')

# Print the level saved in the class
print(f'character0 level: {character0.get_level()}')
print(f'character1 level: {character1.get_level()}')


# Set the name to a new name
character0.set_name('Bill')
character1.set_name('John')

# Set the classtype to a new classtype
character0.set_classtype('Fighter')
character1.set_classtype('Sorcerer')

# Set the level to a new level
character0.set_level(20)
character1.set_level(15)

# Print the name saved in the class
print(f'character0 name: {character0.get_name()}')
print(f'character1 name: {character1.get_name()}')

# Print the classtype saved in the class
print(f'character0 classtype: {character0.get_classtype()}')
print(f'character1 classtype: {character1.get_classtype()}')

# Print the level saved in the class
print(f'character0 level: {character0.get_level()}')
print(f'character1 level: {character1.get_level()}')