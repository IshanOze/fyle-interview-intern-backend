-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
WITH CTE AS(SELECT teacher_id, COUNT(*) as c, grade
FROM assignments
WHERE teacher_id <> "None" AND grade <> "None"
GROUP BY teacher_id, grade)

SELECT c
FROM cte
WHERE grade = "A" AND teacher_id = 2