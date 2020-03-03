-- List all cities in the database hbtn_0d_usa
-- Using JOIN
SELECT cities.id, cities.name, states.name
FROM states
INNER JOIN cities
ON states.id = cities.state_id;
