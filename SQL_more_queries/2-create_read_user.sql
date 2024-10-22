-- Create a database and an user

-- Create the database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege in database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Ensure the privileges take effect
FLUSH PRIVILEGES;
