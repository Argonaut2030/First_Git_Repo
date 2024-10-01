-- Знайти які курси читає певний викладач.
SELECT  
    t.fullname ,
    s.name
FROM teachers t
JOIN subjects s on t.id =s.teacher_id 
;
