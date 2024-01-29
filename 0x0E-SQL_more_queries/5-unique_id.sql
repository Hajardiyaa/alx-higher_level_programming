-- Creating table `unique_id` in MySQL Server with a UNIQUE constraint on the ID column.
CREATE TABLE IF NOT EXISTS unique_id(
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

