-- Count number of occurrences of each score
SELECT score, COUNT(score) AS number -- number is a temporary column
FROM second_table
GROUP BY score  -- Removes duplicates
ORDER BY number DESC

