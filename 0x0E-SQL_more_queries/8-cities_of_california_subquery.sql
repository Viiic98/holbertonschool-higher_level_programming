-- List all cities that can be found in California
-- Listed in ascending order
SELECT cities.id, cities.name
FROM states, cities
WHERE states.id = cities.state_id
AND states.name = 'California';
