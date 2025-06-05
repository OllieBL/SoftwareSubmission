class Weapon:
    def __init__(self, name, category, damage):
        self._name = name
        self._category = category
        self._damage = damage

    def get_stats(self):
        print(f'Name: {self._name}\nCategory: {self._category}\nDamage: {self._damage}')

class Sword(Weapon):
    def __init__(self, name, category, damage, damage_category):
        super().__init__(name, category, damage)
        self._damage_category = damage_category

    def get_stats(self):
        print(f'Name: {self._name}\nCategory: {self._category}\nDamage: {self._damage}\nDamage Category: {self._damage_category}\nCrit Damage: {self._damage * 3}')

class Bow(Weapon):
    def __init__(self, name, category, damage, damage_category):
        super().__init__(name, category, damage)
        self._damage_category = damage_category

    def get_stats(self):
        print(f'Name: {self._name}\nCategory: {self._category}\nDamage: {self._damage}\nDamage Category: {self._damage_category}\nCrit Damage: {self._damage * 2}')

class Longbow(Bow):
    def __init__(self, name, category, damage, damage_category, bow_range):
        super().__init__(name, category, damage, damage_category)
        self._bow_range = bow_range

    def get_stats(self):
        print(f'Name: {self._name}\nCategory: {self._category}\nDamage: {self._damage}\nDamage Category: {self._damage_category}\nCrit Damage: {self._damage * 2}\nBow Range: {self._bow_range}')

class Shortbow(Bow):
    def __init__(self, name, category, damage, damage_category, bow_range):
        super().__init__(name, category, damage, damage_category)
        self._bow_range = bow_range

    def get_stats(self):
        print(f'Name: {self._name}\nCategory: {self._category}\nDamage: {self._damage}\nDamage Category: {self._damage_category}\nCrit Damage: {self._damage * 2}\nBow Range: {self._bow_range}')