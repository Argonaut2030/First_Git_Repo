from sqlalchemy import func, desc, select, and_

from conf.models import Grade, Teacher, Student, Group, Subject
from conf.db import session


def select_01():
    """
    SELECT
        s.id,
        s.fullname,
        ROUND(AVG(g.grade), 2) AS average_grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 5;
    """
    result = session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Student).join(Grade).group_by(Student.id).order_by(desc('average_grade')).limit(5).all()
    return result


def select_02():
    """
    -- Знайти студента із найвищим середнім балом з певного предмета.
    SELECT 
        s.id, 
        s.fullname, 
        ROUND(AVG(g.grade), 2) AS average_grade
    FROM grades g
    JOIN students s ON s.id = g.student_id
    where g.subject_id = 1
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 1;
    """
    result = session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Grade).join(Student).filter(Grade.subjects_id == 1).group_by(Student.id).order_by(
        desc('average_grade')).limit(1).all()
    return result

def select_03():
    """
    -- Знайти середній бал у групах з певного предмета.
    SELECT 
        s.group_id, 
        ROUND(AVG(g.grade), 2) AS average_grade
    FROM grades g
    JOIN students s ON s.id = g.student_id
    where g.subject_id = 2
    GROUP BY s.group_id
    ORDER BY average_grade DESC
    ;

    """
    result = session.query(Student.group_id,func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Grade).join(Student).filter(Grade.subjects_id == 2).group_by(Student.group_id).order_by(
        desc('average_grade')).all()
    return result

def select_04():
    """
    -- Знайти середній бал на потоці (по всій таблиці оцінок)
    SELECT  
        ROUND(AVG(g.grade), 2) AS average_grade
    FROM grades g
    ;


    """
    result = session.query( func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Grade).all()
    return result


def select_05():
    """
    -- Знайти які курси читає певний викладач.
    SELECT  
        t.fullname ,
        s.name
    FROM teachers t
    JOIN subjects s on t.id =s.teacher_id 
    ;


    """
    result = session.query(Teacher.fullname, Subject.name).select_from(Teacher).join(Subject).all()
    return result

def select_06():
    """
    -- Знайти список студентів у певній групі.
    SELECT  
        s.fullname ,
        g.name
    FROM students s
    JOIN groups g on s.group_id =g.id 
    where s.group_id =2
    ;
    """
    result = session.query(Student.fullname,Group.name).select_from(Student).join(Group).filter(Student.group_id == 2).all()
    return result

def select_07():
    """
    -- Знайти оцінки студентів у окремій групі з певного предмета.
    SELECT  
        s.fullname ,
        s.group_id ,
        g.subject_id ,
        g.grade 
    FROM students s
    JOIN grades g on s.id = g.student_id 
    WHERE s.group_id = 2 AND g.subject_id = 3
    ;
    """
    result = session.query(Student.fullname,Student.group_id, Grade.subjects_id, Grade.grade).select_from(Student)\
    .join(Grade).filter(and_(Student.group_id == 2, Grade.subjects_id == 3)).all()
    return result

def select_08():
    """
    -- Знайти середній бал, який ставить певний викладач зі своїх предметів
    SELECT  
        g.subject_id ,
        s.name,
        s.teacher_id,
        ROUND(AVG(g.grade), 2) AS average_grade
    FROM grades g
    JOIN subjects  s on g.subject_id = s.id 
    WHERE s.teacher_id = 2
    GROUP BY s.teacher_id , g.subject_id ,  s.name 
    ;
    """
    result = session.query(Grade.subjects_id,Subject.name, Subject.teacher_id,func.round(func.avg(Grade.grade), 2).label('average_grade')).select_from(Grade)\
    .join(Subject).filter(Subject.teacher_id == 2).group_by(Subject.teacher_id, Grade.subjects_id, Subject.name).all()
    return result

def select_09():
    """
    -- Знайти список курсів, які відвідує студент.
    SELECT  
        g.student_id ,
        g.subject_id ,
        s.name
    FROM grades g
    JOIN subjects  s on g.subject_id = s.id 
    WHERE g.student_id = 2
    group by g.subject_id ,  g.student_id, s.name
    ;

    """
    result = session.query(Grade.subjects_id, Grade.student_id, Subject.name).select_from(Grade)\
    .join(Subject).filter(Grade.student_id == 2).group_by(Grade.subjects_id, Grade.student_id, Subject.name).all()
    return result

def select_10():
    """
    -- Список курсів, які певному студенту читає певний викладач.
    SELECT  
        g.student_id ,
        g.subject_id ,
        s.name,
        t.fullname 
    FROM grades g
    JOIN subjects  s on g.subject_id = s.id 
    join teachers t on s.teacher_id = t.id 
    WHERE g.student_id = 2 and t.id = 2
    group by g.subject_id ,  g.student_id, s.name,  t.fullname 
    ;


    """
    result = session.query( Grade.student_id, Grade.subjects_id, Subject.name, Teacher.fullname).select_from(Grade)\
    .join(Subject).join(Teacher).filter(and_ (Grade.student_id == 2, Teacher.id == 3)).group_by(Grade.subjects_id, Grade.student_id, Subject.name, Teacher.fullname).all()
    return result

if __name__ == '__main__':
    # print(select_01())
    # print(select_02())
    # print(select_03())
    # print(select_04())
    # print(select_05())
    # print(select_06())
    # print(select_07())
    # print(select_09())
    print(select_10())