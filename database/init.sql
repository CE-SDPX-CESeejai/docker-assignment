-- Create database
CREATE DATABASE IF NOT EXISTS SpdxDocker;
USE SpdxDocker;

-- Create USERS table
CREATE TABLE IF NOT EXISTS USERS (
    uid INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL
);

-- Insert sample data
INSERT INTO USERS (name, age) VALUES ('Alice', 30);
INSERT INTO USERS (name, age) VALUES ('Bob', 25);
