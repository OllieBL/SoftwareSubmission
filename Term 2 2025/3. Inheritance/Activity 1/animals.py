class Animal:
    def __init__(self, name):
        self._name = name

    def get_sound(self):
        return ''
    

class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name)
        self._sound = sound
    
    def get_sound(self):
        print(f'{self._name}   {self._sound}')

class Cat(Animal):
    def __init__(self, name, sound):
        super().__init__(name)
        self._sound = sound
    
    def get_sound(self):
        print(f'{self._name}   {self._sound}')