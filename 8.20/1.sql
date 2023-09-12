SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5;
https://leetcode.cn/problems/classes-more-than-5-students/
