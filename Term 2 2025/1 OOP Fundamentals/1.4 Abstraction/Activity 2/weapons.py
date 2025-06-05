from abc import ABC, abstractmethod

class Weapon(ABC):
    def __init__(self, name, category, damage):
        self.name = name
        self.category = category
        self.damage = damage

    @abstractmethod
    def get_stats(self):
        pass

    @abstractmethod
    def set_stats(self):
        pass

class Sword(Weapon):
    def __init__(self, name, category, damage, melee_type):
        super().__init__(name, category, damage)
        self.melee_type = melee_type

    def get_stats(self):
        print(f'name: {self.name}\ncategory: {self.category}\ndamage: {self.damage}\nmelee type: {self.melee_type}\n')
    
    def set_stats(self, name, category, damage, melee_type):
        self.name = name
        self.category = category
        self.damage = damage
        self.melee_type = melee_type

class Bow(Weapon):
    def __init__(self, name, category, damage, range_type):
        super().__init__(name, category, damage)
        self.range_type = range_type

    def get_stats(self):
        print(f'name: {self.name}\ncategory: {self.category}\ndamage: {self.damage}\nrange type: {self.range_type}\n')

    def set_stats(self, name, category, damage, range_type):
        self.name = name
        self.category = category
        self.damage = damage
        self.range_type = range_type