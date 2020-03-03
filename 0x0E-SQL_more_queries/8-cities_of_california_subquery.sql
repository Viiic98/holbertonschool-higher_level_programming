-- List all cities that can be found in California
-- Listed in ascending order
USE `hbtn_0d_usa`;
SELECT cities.id 'id', cities.name 'name' FROM cities 
WHERE state_id = (SELECT states.id 'id' FROM states WHERE states.name = 'California')
ORDER BY cities.id ASC;
