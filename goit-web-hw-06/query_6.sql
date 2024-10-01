-- Знайти список студентів у певній групі.
SELECT  
    s.fullname ,
    g.name
FROM students s
JOIN groups g on s.group_id =g.id 
where s.group_id =2
;