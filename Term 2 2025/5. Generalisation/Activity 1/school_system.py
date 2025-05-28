class Person:
    def __init__(self, name, dob, gender, email):
        self._name = name
        self._dob = dob
        self._gender = gender
        self._email = email


    def get_name(self):
        return self._name
    
    def get_dob(self):
        return self._dob
    
    def get_gender(self):
        return self._gender
    
    def get_email(self):
        return self._email
    
    def get_job(self):
        return self._job
    
class Teacher(Person):
    def __init__(self, name, dob, gender, email, faculty, teacher_id):
        super().__init__(name, dob, gender, email)
        self._faculty = faculty
        self._teacher_id = teacher_id

    def get_name(self):
        return super().get_name()
    
    def get_dob(self):
        return super().get_dob()
    
    def get_gender(self):
        return super().get_gender()
    
    def get_email(self):
        return super().get_email()
    
    def get_faculty(self):
        return self._faculty
    
    def get_teacher_id(self):
        return self._teacher_id
    
class Student(Person):
    def __init__(self, name, dob, gender, email, house, core_class, student_id):
        super().__init__(name, dob, gender, email)
        self._house = house
        self._core_class = core_class
        self._student_id = student_id

    def get_name(self):
        return super().get_name()
    
    def get_dob(self):
        return super().get_dob()
    
    def get_gender(self):
        return super().get_gender()
    
    def get_email(self):
        return super().get_email()
    
    def get_house(self):
        return self._house
    
    def get_core_class(self):
        return self._core_class
    
    def get_student_id(self):
        return self._student_id
    
class Parent(Person):
    def __init__(self, name, dob, gender, email, child, job):
        super().__init__(name, dob, gender, email)
        self._child = child
        self._job = job

    def get_name(self):
        return super().get_name()
    
    def get_dob(self):
        return super().get_dob()
    
    def get_gender(self):
        return super().get_gender()
    
    def get_email(self):
        return super().get_email()
    
    def get_child(self):
        return self._child
    
    def get_job(self):
        return self._job