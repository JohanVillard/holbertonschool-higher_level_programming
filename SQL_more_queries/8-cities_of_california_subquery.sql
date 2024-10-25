-- List all cities of California in the database
SELECT cities.id, cities.name
FROM cities
JOIN states
WHERE states.name = "California"
ORDER BY cities.id ASC;

