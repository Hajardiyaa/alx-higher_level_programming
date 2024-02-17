-- Creating database `hbtn_0d_usa` in MySQL Server if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switching to the `hbtn_0d_usa` database
USE hbtn_0d_usa;

-- Creating table `cities` in MySQL Server with an auto-incrementing unique ID,
-- a state_id column as a foreign key referencing states table, and a name column.
CREATE TABLE IF NOT EXISTS cities(
    `id` INT UNIQUE AUTO_INCREMENT NOT NULL,
    `state_id` INT NOT NULL,
    `name` VARCHAR(256),
    PRIMARY KEY(`id`),
    FOREIGN KEY(`state_id`) REFERENCES states(`id`)
);

