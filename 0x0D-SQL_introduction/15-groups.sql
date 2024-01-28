-- Retrieve the count of records with each unique 'score'
-- The results are grouped by 'score' and displayed in descending order.

SELECT score, COUNT(`score`) as number
FROM second_table
GROUP BY score
ORDER BY score DESC;

