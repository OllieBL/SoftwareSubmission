import subjects

def addSubject():
    name = input('name: ')
    year = input('year: ')
    class_code = input('class code: ')
    num_students = input('number of students: ')

    subject = subjects.Subject(name, year, class_code, num_students)
    
    return subject

subject_list = []

while True:
    user_choice = int(input('1. Add subject \n 2. View subject \n 3. Display all subjects \n\n Pick a number'))
    if user_choice == 1:
        subject_list.append(addSubject())
    elif user_choice == 2:
        for i in range(len(subject_list)):
            print(f'{i}. {subject_list[i]._name}')
        user_choice = int(input('\n Pick a subject: '))
        user_class = subject_list[user_choice]
        print(f'{user_class._name}  {user_class._year}  {user_class._class_code}    {user_class._num_students}')
    elif user_choice == 3:
        subjects.displaySubjects(subject_list)