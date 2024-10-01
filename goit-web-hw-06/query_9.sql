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
