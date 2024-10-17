-- Creates users table with id, email and name columns
-- Creates unique constraint on email column
-- If users table already exists, script should not fail
-- Script can be executed on any database

CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
);
