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