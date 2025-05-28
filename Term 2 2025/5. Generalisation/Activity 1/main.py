from school_system import *

person = Person(['Bill', 'Bill'], '04/07/1998', 'Male', 'Bill@bill.com')

teacher = Teacher(['Peter', 'John'], '05/08/1979', 'Male', 'john.peter@bill.com', 'English', 478)

student = Student(['John', 'Smith'], '2/08/2008', 'Male', 'smith.john@bill.com', 'Red house', 'F', 1367)

parent = Parent(['Smith', 'Smith'], '04/04/1994', 'Male', 'smith@smith.com', student, 'Smith')

print(f'Person:\n{person.get_name()}\n{person.get_dob()}\n{person.get_gender()}\n{person.get_email()}')

print(f'\nTeacher:\n{teacher.get_name()}\n{teacher.get_dob()}\n{teacher.get_gender()}\n{teacher.get_email()}\n{teacher.get_faculty()}\n{teacher.get_teacher_id()}')

print(f'\nStudent:\n{student.get_name()}\n{student.get_dob()}\n{student.get_gender()}\n{student.get_email()}\n{student.get_house()}\n{student.get_core_class()}\n{student.get_student_id()}')

print(f'\nParent:\n{parent.get_name()}\n{parent.get_dob()}\n{parent.get_gender()}\n{parent.get_email()}\n{parent.get_job()}\n{parent.get_child().get_name()}')