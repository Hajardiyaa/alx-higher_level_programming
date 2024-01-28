-- Retrieve and display all records from the `second_table`
-- in the MySQL Server database `hbtn_0c_0`.
-- The records will be filtered to include only those with a non-null 'name'
-- and sorted in descending order based on the 'score' column.

SELECT score, name
FROM second_table
WHERE `name` IS NOT NULL
ORDER BY score DESC;

