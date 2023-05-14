DELETE 
FROM Person
WHERE id NOT IN (
    SELECT id 
    FROM (
        SELECT MIN(id) AS id 
        FROM Person 
        GROUP BY LOWER(email)
    ) p
);
# https://leetcode.cn/problems/delete-duplicate-emails/submissions/
