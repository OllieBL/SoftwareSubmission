from game_objects import Player, Weapon, Enemy # MUST have this in the program
import random #For random damage and health


def playerSelection(player_list, weapon_list):
    tester = False
    while tester == False:
        try:
            for i in range(len(player_list)):
                print(f'{i}. {player_list[i].name}    {player_list[i].race}   {player_list[i].cls}    {player_list[i].atk}    {player_list[i].health} /n {weapon_list[i].name}   {weapon_list[i]}')
            user_input = input('pick a player')
            player_choice = player_list[user_input]
            tester = True
        except:
            print('please try again')
        
        return player_choice
# Create an instance of Player
player_character = Player('Gimli', 'Dwarf', 'Fighter', 3, 180)

# TODO: Create an instance of Weapon with random damage between 12 and 15
random_weapon = Weapon('Axe', 'Axe', random.randrange(12, 15))
# TODO: Create an instance of Enemy with random damage between 15 and 18, and random health between 80 and 140
random_enemy = Enemy('Goblin', 'Goblin', random.randrange(15, 18), random.randrange(80, 140))

# Print the player character details
print(f"Player Name: {player_character.name}")
print(f"Player Race: {player_character.race}")
print(f"Player Class: {player_character.cls}")
print(f"Player Attack: {player_character.atk}")
print(f"Player Health: {player_character.health}")


print(f'Weapon Name: {random_weapon.name}')
print(f'Weapon Category: {random_weapon.category}')
print(f'Weapon Damage: {random_weapon.dmg}')


print(f'Enemy Name: {random_enemy.name}')
print(f'Enemy Race: {random_enemy.race}')
print(f'Enemy Damage: {random_enemy.dmg}')
print(f'Enemy Health: {random_enemy.hp}')

player_list = [
    Player('Bill', 'Human', 'Wizard', 5, 100),
    Player('Fred', 'Dwarf', 'Fighter', 3, 180),
    Player('Tom', 'Orc', 'Barbarian', 2, 250),
    Player('Greg', 'Elf', 'Rogue', 3, 150)
]
weapon_list = [
    Weapon('Sword', 'Sword', 2),
    Weapon('Axe', 'Axe', 3),
    Weapon('Staff', 'Staff', 1),
    Weapon('Bow', 'Bow', 3)
]

playerSelection(player_list, weapon_list)