-- Display rows in a table
-- Only where a specific colum exists and is ordered by score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
