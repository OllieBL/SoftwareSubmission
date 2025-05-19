from weapons import Sword, Bow

sword = Sword('ekskalyber', 'sword', 5, 'slashing')
bow = Bow('cool bow', 'reallylongbow', 20, 'piercing')

sword.get_stats()
bow.get_stats()

sword.set_stats('edge of annihilation', 'sword', 2, 'slashing')
bow.set_stats('uncool bow', 'extremelyshortbow', 1, 'explosive')

sword.get_stats()
bow.get_stats()