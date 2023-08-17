-- lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).
-- Connect to the MySQL server as root or a user with SELECT permission
mysql -u root -p

-- Enter the root password when prompted

-- Use the information_schema database
USE information_schema;

-- Create a temporary table to store the user privileges
CREATE TEMPORARY TABLE user_privs (
  GRANTEE VARCHAR(81),
  PRIVILEGE_TYPE VARCHAR(64),
  IS_GRANTABLE VARCHAR(3)
);

-- Insert the user privileges from the user_privileges table
INSERT INTO user_privs
SELECT GRANTEE, PRIVILEGE_TYPE, IS_GRANTABLE
FROM user_privileges
WHERE GRANTEE LIKE "'user_0d_1'@'localhost'" OR GRANTEE LIKE "'user_0d_2'@'localhost'";

-- Insert the user privileges from the schema_privileges table
INSERT INTO user_privs
SELECT GRANTEE, PRIVILEGE_TYPE, IS_GRANTABLE
FROM schema_privileges
WHERE GRANTEE LIKE "'user_0d_1'@'localhost'" OR GRANTEE LIKE "'user_0d_2'@'localhost'";

-- Insert the user privileges from the table_privileges table
INSERT INTO user_privs
SELECT GRANTEE, PRIVILEGE_TYPE, IS_GRANTABLE
FROM table_privileges
WHERE GRANTEE LIKE "'user_0d_1'@'localhost'" OR GRANTEE LIKE "'user_0d_2'@'localhost'";

-- Insert the user privileges from the column_privileges table
INSERT INTO user_privs
SELECT GRANTEE, PRIVILEGE_TYPE, IS_GRANTABLE
FROM column_privileges
WHERE GRANTEE LIKE "'user_0d_1'@'localhost'" OR GRANTEE LIKE "'user_0d_2'@'localhost'";

-- Select and display the user privileges from the temporary table
SELECT * FROM user_privs;

-- Drop the temporary table
DROP TABLE user_privs;
