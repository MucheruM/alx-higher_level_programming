-- Creates a MySQL server user_0d_1 with all priviliges
-- The user password should be set to user_0d_1_pwd
-- The script should not fail if the user exists

-- First create the server with the password
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Give access to all priviliges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
