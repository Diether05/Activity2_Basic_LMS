import database


def prompt_add_student():
    studentID = input("Student ID: ")
    first_name = input("First Name: ")
    middle_name = input("Middle Name: ")
    last_name = input("Last Name: ")
    print("\n" + first_name + " was successfully added!!!\n")
    database.add_student(studentID, first_name, middle_name, last_name)


def prompt_add_teacher():
    teacherID = input("Teacher ID: ")
    first_name = input("First Name: ")
    middle_name = input("Middle Name: ")
    last_name = input("Last Name: ")
    print("\n" + first_name + " was successfully added!!!\n")
    database.add_teacher(teacherID, first_name, middle_name, last_name)


def prompt_add_subject():
    subjectID = input("Subject ID: ")
    subject = input("Subject Name: ")
    unit = input("Number of Unit: ")
    print("\n" + subject + " was successfully added!!!\n")
    database.add_subject(subjectID, subject, unit)


def prompt_add_class():
    classID = input("Class ID: ")
    teacherID = input("Teacher ID: ")
    subjectID = input("Subject ID: ")
    print("\n" + classID + " was successfully added!!!\n")
    database.add_class(classID, teacherID, subjectID)


def prompt_view_student():
    classID = input("Class ID :")
    studentList = database.view_student(classID)
    print("\n------Viewing Student List------")
    display_student(studentList)


def prompt_view_teacher():
    classID = input("Class ID:")
    teacherList= database.view_teacher(classID)
    print("\n------Viewing Teacher List------")
    display_teacher(teacherList)


def prompt_view_subject():
    subject = database.view_subject()
    print("\n------Viewing Subject List------")
    display_subject(subject)


def prompt_view_class():
    classList = database.view_class()
    print("\n------Viewing Class List------")
    display_class(classList)


def prompt_view_student_class():
    studentID = input("Student ID :")
    studentClass = database.view_student_class(studentID)
    print("\n------Viewing Student Class------")
    display_student_class(studentClass)


def prompt_view_teachers_class():
    teachersID = input("Teacher's ID:")
    teacherList = database.view_teacher_class(teachersID)
    print("\n------Viewing Teacher's Class------")
    display_teacher_class(teacherList)


def prompt_remove_student():
    name = input("Student Name:")
    print(name + " was successfully removed from the list")
    database.remove_student(name)


def prompt_remove_teacher():
    name = input("Teacher Name:")
    print(name + " was successfully removed from the list")
    database.remove_teacher(name)


def prompt_remove_subject():
    subjectID = input("Subject ID:")
    print(subjectID + " was successfully removed from the list")
    database.remove_subject(subjectID)


def prompt_remove_class():
    classID = input("Class ID:")
    print(classID + " was successfully removed from the list")
    database.remove_class(classID)

def prompt_view_student_subject():
    studentSub = database.view_student_subject()
    print("\n------Viewing Student's Subject------")
    display_student_subject(studentSub)

def prompt_view_teacher_subject():
    teacherSub = database.view_teacher_subject()
    print("\n------Viewing Teacher's Subject------")
    display_teacher_subject(teacherSub)

def display_student(studentList):
    for student in studentList:
        print(f"{student[0]}, {student[1]}, {student[2]}, {student[3]}")
    print("--------------- \n")


def display_student_class(studentClass):
    for student in studentClass:
        print(f"{student[0]}")
    print("--------------- \n")


def display_teacher(teacherList):
    for teacher in teacherList:
        print(f"{teacher[0]}, {teacher[1]}, {teacher[2]}, {teacher[3]}")
    print("--------------- \n")


def display_teacher_class(teacherClass):
    for teacher in teacherClass:
        print(f"{teacher[0]}")
    print("--------------- \n")


def display_subject(subjectList):
    for subject in subjectList:
        print(f"{subject[0]}, {subject[1]}, {subject[2]}")
    print("--------------- \n")


def display_class(classList):
    for class_ in classList:
        print(f"{class_[0]}, {class_[1]}, {class_[2]}")
    print("--------------- \n")

def display_student_subject(studentSub):
    for studentSub_ in studentSub:
        print(f"{studentSub_[0]}, {studentSub_[1]}, {studentSub_[2]}")
    print("--------------- \n")

def display_teacher_subject(teacherSub):
    for teacherSub_ in teacherSub:
        print(f"{teacherSub_[0]}, {teacherSub_[1]}, {teacherSub_[2]}")
    print("--------------- \n")