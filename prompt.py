import database


def prompt_add_student():
    studentID = input("Student ID: ")
    first_name = input("First Name: ")
    middle_name = input("Middle Name: ")
    last_name = input("Last Name: ")
    database.add_student(studentID, first_name, middle_name, last_name)


def prompt_add_teacher():
    teacherID = input("Teacher ID: ")
    first_name = input("First Name: ")
    middle_name = input("Middle Name: ")
    last_name = input("Last Name: ")
    database.add_teacher(teacherID, first_name, middle_name, last_name)


def prompt_add_subject():
    subjectID = input("Subject ID: ")
    subject = input("Subject Name: ")
    unit = input("Number of Unit: ")
    database.add_subject(subjectID, subject, unit)


def prompt_add_class():
    classID = input("Class ID: ")
    teacherID = input("Teacher ID: ")
    subjectID = input("Subject ID: ")
    database.add_class(classID, teacherID, subjectID)


def prompt_view_student():
    classID = input("Class ID :")
    studentList = database.view_student(classID)
    display_student(studentList)


def prompt_view_teacher():
    classID = input("Class ID:")
    teacherList= database.view_teacher(classID)
    display_teacher(teacherList)


def prompt_view_subject():
    subject = database.view_subject()
    display_subject(subject)


def prompt_view_class():
    classList = database.view_class()
    display_class(classList)


def prompt_view_student_class():
    studentID = input("Student ID :")
    studentClass = database.view_student_class(studentID)
    display_student_class(studentClass)


def prompt_view_teachers_class():
    teachersID = input("Teacher's ID:")
    teacherList = database.view_teacher_class(teachersID)
    display_teacher_class(teacherList)


def prompt_remove_student():
    name = input("Student Name:")
    database.remove_student(name)


def prompt_remove_teacher():
    name = input("Teacher Name:")
    database.remove_teacher(name)


def prompt_remove_subject():
    subjectID = input("Subject ID:")
    database.remove_subject(subjectID)


def prompt_remove_class():
    classID = input("Class ID:")
    database.remove_class(classID)


def display_student(studentList):
    for student in studentList:
        print(f"{student[0]}, {student[1]}, {student[2]}, {student[3]}")
    print("---- \n")


def display_student_class(studentClass):
    for student in studentClass:
        print(f"{student[0]}")
    print("---- \n")


def display_teacher(teacherList):
    for teacher in teacherList:
        print(f"{teacher[0]}, {teacher[1]}, {teacher[2]}, {teacher[3]}")
    print("---- \n")


def display_teacher_class(teacherClass):
    for teacher in teacherClass:
        print(f"{teacher[0]}")
    print("---- \n")


def display_subject(subjectList):
    for subject in subjectList:
        print(f"{subject[0]}, {subject[1]}, {subject[2]}")
    print("---- \n")


def display_class(classList):
    for class_ in classList:
        print(f"{class_[0]}, {class_[1]}, {class_[2]}")
    print("---- \n")

