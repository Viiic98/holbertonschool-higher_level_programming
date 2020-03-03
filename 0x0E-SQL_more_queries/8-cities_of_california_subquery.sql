-- List all cities that can be found in California
--
SELECT hbtn_0d_usa.cities.id 'id', hbtn_0d_usa.cities.name 'name'
FROM hbtn_0d_usa.cities
WHERE hbtn_0d_usa.cities.state_id = (
      	       SELECT hbtn_0d_usa.states.id 'id' 
	       FROM hbtn_0d_usa.states 
	       WHERE name = "California")
ORDER BY id;
