-- Retrieving the ID and name of all cities in the state of `California`
-- from the database `hbtn_0d_usa`.
SELECT `id`, `name`
FROM `cities`
WHERE `state_id` = (
    SELECT `id` FROM `states`
    WHERE `name` = "California"
);

