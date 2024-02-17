-- Update the 'score' field of a record in the `second_table`
-- of the MySQL Server database.
-- Specifically, set the 'score' to 10 for the record with the name 'Bob'.

UPDATE second_table
SET `score` = '10'
WHERE `name` = 'Bob';

