-- List score and name of name is not empty in descending order
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
