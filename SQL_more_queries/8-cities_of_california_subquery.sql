-- List all cities of California in the database
SELECT id, state_id, name
FROM cities
WHERE state_id
ORDER BY cities.id ASC;

