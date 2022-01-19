import sqlite3

CREATE_STUDENT_TABLE = """
CREATE TABLE IF NOT EXISTS student (
studentID VARCHAR(45) NOT NULL PRIMARY KEY,
first_name TEXT NOT NULL,
middle_name TEXT,
last_name TEXT NOT NULL
);
"""

CREATE_TEACHER_TABLE = """
CREATE TABLE IF NOT EXISTS teacher (
teacherID VARCHAR(45) NOT NULL PRIMARY KEY,
first_name TEXT NOT NULL,
middle_name TEXT,
last_name TEXT NOT NULL
);
"""

CREATE_SUBJECT_TABLE = """
CREATE TABLE IF NOT EXISTS subject (
subjectID VARCHAR(45) NOT NULL PRIMARY KEY,
subject TEXT NOT NULL,
unit INT NOT NULL
);
"""

CREATE_CLASS_TABLE = """
CREATE TABLE IF NOT EXISTS class (
classId VARCHAR(45) NOT NULL PRIMARY KEY,
teacherID VARCHAR(45) NOT NULL,
subjectID VARCHAR(45) NOT NULL,
FOREIGN KEY(teacherID) REFERENCES teacher(teacherID) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY(subjectID) REFERENCES subject(subjectID) ON DELETE CASCADE ON UPDATE CASCADE
);
"""

CREATE_SCHEDULE_TABLE = """
CREATE TABLE IF NOT EXISTS schedule (
id INTEGER NOT NULL,
studentID VARCHAR(45) NOT NULL,
classID	VARCHAR(45) NOT NULL,
FOREIGN KEY("studentID") REFERENCES "student"("studentID") ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY("classID") REFERENCES "class"("classID") ON DELETE CASCADE ON UPDATE CASCADE,
PRIMARY KEY("id" AUTOINCREMENT)
);"""

# student
ADD_STUDENT = "INSERT INTO student (studentID, first_name, middle_name, last_name) VALUES (?, ?, ?, ?);"
VIEW_STUDENT = """
SELECT student.*
FROM student 
INNER JOIN schedule 
ON student.studentID=schedule.studentID
WHERE schedule.classID = ?
"""
VIEW_STUDENT_CLASS = """
SELECT classID
FROM schedule 
WHERE studentID = ?
"""
REMOVE_STUDENT = "DELETE FROM student WHERE (first_name||middle_name||last_name) LIKE ?;"

# teacher
ADD_TEACHER = "INSERT INTO teacher (teacherID, first_name, middle_name, last_name) VALUES (?, ?, ?, ?);"
VIEW_TEACHER = """
SELECT teacher.*
FROM teacher 
"""
VIEW_TEACHER_CLASS = """
SELECT classID
FROM class 
WHERE teacherID = ?
"""
REMOVE_TEACHER = "DELETE FROM teacher WHERE (first_name||middle_name||last_name) LIKE ?;"

# class
ADD_CLASS = "INSERT INTO class (classID, teacherID, subjectID) VALUES (?, ?, ?);"
VIEW_CLASS = """
SELECT class.*
FROM class 
"""
REMOVE_CLASS = "DELETE FROM class WHERE classID = ? ;"

# subject
ADD_SUBJECT = "INSERT INTO subject (subjectID, subject, unit) VALUES (?, ?, ?);"
VIEW_SUBJECT = """
SELECT subject.*
FROM subject 
"""
REMOVE_SUBJECT = "DELETE FROM subject WHERE subjectID = ? ;"

SHOW_STUDENTS_SUBJECT = """
SELECT first_name || " " || middle_name || " " || last_name, subject, unit
FROM student s
INNER JOIN schedule sched
ON s.studentID = sched.studentID
INNER JOIN class cls
ON sched.classID = cls.classID
INNER JOIN subject sbt
ON cls.subjectID = sbt.subjectID
"""

SHOW_TEACHERS_SUBJECT = """
SELECT first_name || " " || middle_name || " " || last_name AS "Full Name", subject, unit
FROM teacher t
INNER JOIN class cls
ON t.teacherID = cls.teacherID
INNER JOIN subject sbt
ON cls.subjectID = sbt.subjectID
"""

connection = sqlite3.connect("database.db")


def create_tables():
    with connection:
        connection.execute(CREATE_STUDENT_TABLE)
        connection.execute(CREATE_TEACHER_TABLE)
        connection.execute(CREATE_SUBJECT_TABLE)
        connection.execute(CREATE_CLASS_TABLE)
        connection.execute(CREATE_SCHEDULE_TABLE)


def add_student(student_id, first_name, middle_name, last_name):
    with connection:
        connection.execute(ADD_STUDENT, (student_id, first_name, middle_name, last_name))


def view_student(classID):
    with connection:
        cursor = connection.cursor()
        cursor.execute(VIEW_STUDENT, (classID,))
        return cursor.fetchall()


def view_student_class(studentID):
    with connection:
        cursor = connection.cursor()
        cursor.execute(VIEW_STUDENT_CLASS, (studentID,))
        return cursor.fetchall()


def remove_student(name):
    with connection:
        cursor = connection.cursor()
        cursor.execute(REMOVE_STUDENT, ('%'+name+'%',))
        return cursor.fetchall()


def add_teacher(teacherID, first_name, middle_name, last_name):
    with connection:
        connection.execute(ADD_TEACHER, (teacherID, first_name, middle_name, last_name))


def view_teacher(classID):
    with connection:
        cursor = connection.cursor()
        cursor.execute(VIEW_TEACHER)
        return cursor.fetchall()


def view_teacher_class(teacherID):
    with connection:
        cursor = connection.cursor()
        cursor.execute(VIEW_TEACHER_CLASS, (teacherID,))
        return cursor.fetchall()


def remove_teacher(name):
    with connection:
        cursor = connection.cursor()
        cursor.execute(REMOVE_TEACHER, ('%'+name+'%',))
        return cursor.fetchall()


def add_class(classID, teacherID, subjectID):
    with connection:
        connection.execute(ADD_CLASS, (classID, teacherID, subjectID))


def view_class():
    with connection:
        cursor = connection.cursor()
        cursor.execute(VIEW_CLASS)
        return cursor.fetchall()


def remove_class(classID):
    with connection:
        cursor = connection.cursor()
        cursor.execute(REMOVE_CLASS, (classID,))
        return cursor.fetchall()


def add_subject(subjectID, subject, unit):
    with connection:
        connection.execute(ADD_SUBJECT, (subjectID, subject, unit))


def view_subject():
    with connection:
        cursor = connection.cursor()
        cursor.execute(VIEW_SUBJECT)
        return cursor.fetchall()


def remove_subject(subjectID):
    with connection:
        cursor = connection.cursor()
        cursor.execute(REMOVE_SUBJECT, (subjectID,))
        return cursor.fetchall()

def view_student_subject():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SHOW_STUDENTS_SUBJECT)
        return cursor.fetchall()

def view_teacher_subject():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SHOW_TEACHERS_SUBJECT)
        return cursor.fetchall()
