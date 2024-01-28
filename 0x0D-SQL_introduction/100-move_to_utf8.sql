-- Set the character set of the `hbtn_0c_0` database to UTF-8 in MySQL Server.

USE hbtn_0c_0;

-- Modify the database and table character set to UTF-8.
-- The collation is also set to utf8mb4_unicode_ci for proper Unicode support.

ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

