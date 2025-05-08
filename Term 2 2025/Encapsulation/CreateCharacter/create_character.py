class CreateCharacter:
    def __init__(self, name, classtype, level):
        self._name = name
        self._classtype = classtype
        self._level = level

    
    def get_name(self):
        return self._name
    
    def get_classtype(self):
        return self._classtype
    
    def get_level(self):
        return self._level
    

    def set_name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name

    def set_classtype(self, new_classtype):
        if isinstance(new_classtype, str):
            self._classtype = new_classtype

    def set_level(self, new_level):
        if isinstance(new_level, int):
            self._level = new_level