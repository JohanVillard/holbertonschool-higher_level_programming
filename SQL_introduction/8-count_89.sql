-- Display number of id equal to 89
SELECT
	COUNT(id)  -- Compte les id
	AS total_id 
FROM 
	first_table
WHERE
	id = 89;
