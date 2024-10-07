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