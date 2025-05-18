import weapons


weapon = weapons.Weapon('cool weapon', 'weapon', 5)

sword = weapons.Sword('cool sword', 'sword', 4, 'slashing')

bow = weapons.Bow('cool bow', 'bow', 3, 'piercing')

longbow = weapons.Longbow('cool longbow', 'longbow', 4, 'piercing', 150)

shortbow = weapons.Shortbow('cool shortbow', 'shortbow', 2, 'piercing', 80)

weapon.get_stats()

sword.get_stats()

bow.get_stats()

longbow.get_stats()

shortbow.get_stats()