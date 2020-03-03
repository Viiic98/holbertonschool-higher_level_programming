-- List the max temperature of every state
-- Group by state and ordered by state
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state ASC;
