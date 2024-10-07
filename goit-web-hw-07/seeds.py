import random

from faker import Faker
from sqlalchemy.exc import SQLAlchemyError

from conf.db import session
from conf.models import Teacher, Group, Subject, Student, Grade

fake = Faker('uk-UA')

def insert_groups():
    for _ in range(3):
        group = Group(
            name = fake.word()
        )
        session.add(group)
       
# def insert_students():
#     for id in range (1, 4):
#         for _ in range(10):
#             student = Student(
#                 fullname = fake.name()
#                 group_id = id
#             )
#             session.add(student)

def insert_students():
    for group_id in range(1, 4):
        for _ in range(10):
            student = Student(fullname=fake.name(), group_id=group_id)
            session.add(student)
            session.flush()  # Commit the transaction to get the generated ID

            for subject_id in range(1, 7):
                for _ in range(3):
                    grade = Grade(student_id=student.id, subjects_id=subject_id,
                                  grade=random.randint(0, 100), grade_date=fake.date_this_decade())
                    session.add(grade)

# def insert_students():
#     students = []  # List to store Student objects

#     for group_id in range(1, 4):
#         for _ in range(10):
#             student = Student(fullname=fake.name(), group_id=group_id)
#             students.append(student)  # Add student to the list

#             for subject_id in range(1, 7):
#                 for _ in range(3):
#                     grade = Grade(student_id=student.id, subjects_id=subject_id,
#                                 grade=random.randint(0, 100), grade_date=fake.date_this_decade())
#                     session.add(grade)

#     # Add all students to the session at once
#     session.add_all(students)


def insert_teachers():
    for _ in range(5):
        teacher = Teacher(
            fullname=fake.name()
        )
        session.add(teacher)

def insert_subjects():
    for teachers in range (1, 6):
        for _ in range (2):
            subjects = Subject(
                name = fake.word(),
                teacher_id = teachers
            )
            session.add(subjects)





if __name__ == '__main__':
    try:
        insert_groups()
        insert_teachers()
        insert_subjects()
        insert_students()
        session.commit()
        # insert_rel()
        # session.commit()
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
    finally:
        session.close()
