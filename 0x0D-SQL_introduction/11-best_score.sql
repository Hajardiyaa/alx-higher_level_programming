-- Retrieve and display all records from the `second_table`
-- in the MySQL Server database `hbtn_0c_0` where the 'score' is greater than or equal to 10.
-- The records will be sorted in descending order based on the 'score' column.

SELECT score, name
FROM second_table
WHERE `score` >= 10
ORDER BY score DESC;

