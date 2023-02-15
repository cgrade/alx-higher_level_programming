--A sql script that create database and tables with few tweaking constraints
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY, state_id INT NOT NULL FOREIGN KEY(state_id) REFRENCES states(id), name VARCHAR(256) NOT NULL);

