class Subject:
    def __init__(self, name, year, class_code, num_students):
        self._name = name
        self._year = year
        self._class_code = class_code
        self._num_students = num_students
    
def displaySubjects(subjects):
    for i in subjects:
        print(f'{i._name}   {i._year}   {i._class_code} {i._num_students}')