-- Delete all records from the `second_table` in the MySQL Server database `hbtn_0c_0`
-- where the 'score' is less than or equal to 5.
-- This operation removes records with low scores from the table.

DELETE FROM second_table
WHERE `score` <= 5;

