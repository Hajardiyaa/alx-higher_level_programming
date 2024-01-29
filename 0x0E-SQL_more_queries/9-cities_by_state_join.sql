-- Retrieving information about all cities along with their corresponding states
-- from the database `hbtn_0d_usa` using a LEFT JOIN.
SELECT cities.id, cities.name, states.name
FROM cities
LEFT JOIN states
ON cities.state_id = states.id;

