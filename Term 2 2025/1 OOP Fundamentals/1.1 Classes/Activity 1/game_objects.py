class Player:
    def __init__(self, name, race, cls, atk, health):
        self.name = name      # Store the player's name
        self.race = race      # Store the player's race (e.g., human, elf, etc.)
        self.cls = cls        # Store the player's class (e.g., warrior, mage, etc.)
        self.atk = atk        # Store the player's attack power
        self.health = health  # Store the player's health points

class Weapon:
    def __init__(self, name, category, dmg):
        self.name = name            # Store weapon name
        self.category = category    # Store weapon category
        self.dmg = dmg              # Store weapon damage

class Enemy:
    def __init__(self, name, race, dmg, hp):
        self.name = name    # Store enemy name
        self.race = race    # Store enemy race
        self.dmg = dmg      # Store enemy damage
        self.hp = hp        # Store enemy health