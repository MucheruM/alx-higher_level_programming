-- Creates the database with the passwod 'user_od_2_pwd
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON	`hbtn_0d_2`.* TO 'user_0d_2'@'localhost'
