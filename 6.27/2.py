SELECT d.name AS Department, e1.name AS Employee, e1.salary AS Salary FROM Employee e1
JOIN Department d ON e1.departmentId = d.id
WHERE e1.salary = (
SELECT MAX(salary) FROM Employee e2 WHERE e2.departmentId = e1.departmentId
)
# https://leetcode.cn/problems/department-highest-salary/submissions/
