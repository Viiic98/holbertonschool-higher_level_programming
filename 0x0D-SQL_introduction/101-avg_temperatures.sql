-- From a imported table
-- Display the average of temperatures group by city
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
