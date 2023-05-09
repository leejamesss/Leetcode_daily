SELECT email AS Email FROM Person GROUP BY email HAVING COUNT(*) > 1
# https://leetcode.cn/problems/duplicate-emails/submissions/
