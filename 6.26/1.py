# https://leetcode.cn/problems/employees-earning-more-than-their-managers/
SELECT e.name AS Employee
FROM Employee e, Employee m
WHERE e.managerId = m.id AND e.salary > m.salary;
