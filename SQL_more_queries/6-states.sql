-- Create a database and define table with variable constraints

-- Create a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Choose a database
USE hbtn_0d_usa;

-- Create a table
CREATE TABLE IF NOT EXISTS states (
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
	);
