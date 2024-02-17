-- Creating database `hbtn_0d_2` if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Creating user `user_0d_2` at localhost if it doesn't already exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Granting SELECT privilege on all tables in database `hbtn_0d_2` to user_0d_2 at localhost
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';

