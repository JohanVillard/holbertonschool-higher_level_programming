-- List all cities contained in the database
SELECT cities.id, cities.name, states.name
FROM cities -- Select the fields to display
INNER JOIN states -- Principal table to be queried
ON cities.state_id = states.id -- Join the tables
ORDER BY cities.id ASC
