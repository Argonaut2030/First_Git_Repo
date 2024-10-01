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
