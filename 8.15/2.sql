WITH first_login AS(
    SELECT player_id,MIN(event_date) AS first_login_date
    FROM Activity 
    GROUP BY player_id
)

SELECT ROUND(CAST(COUNT(*) AS FLOAT)/ (SELECT COUNT(*) FROM first_login),2) AS fraction
FROM(
    SELECT player_id
    FROM Activity
    WHERE(player_id,event_date)IN (
        SELECT player_id,DATE_ADD(first_login_date,INTERVAL 1 DAY) AS next_day
        FROM first_login 
    )
    GROUP BY player_id
) AS subquery;


-- https://leetcode.cn/problems/game-play-analysis-iv/submissions/?envType=daily-question&envId=2023-09-01
