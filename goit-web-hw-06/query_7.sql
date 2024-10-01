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