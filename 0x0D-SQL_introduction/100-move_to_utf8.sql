-- converts hbtn_0c_0 database to utf8
-- table: first_table to utf8
-- field: name to utf8
USE `hbtn_0c_0`
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
