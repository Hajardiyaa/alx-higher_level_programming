-- Creating user user_0d_1 at localhost if it doesn't already exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Granting all privileges on all databases and tables to user_0d_1 at localhost
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Refreshing privileges to apply the changes
FLUSH PRIVILEGES;

