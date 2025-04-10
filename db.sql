CREATE DATABASE IF NOT EXISTS login_db;
USE login_db;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

INSERT INTO users (username, password) VALUES 
('thfdfzn', '3221'),
('thfdfzi', '2341'),
('thffdin', '2341'),
('tzdsdin', '2341'),
('thsddazin', '2341'),
('thsddszn', '2341'),
('thdsdzin', '2341'),
('hzn', '2341'),
('thdsdaszin', '2341'),
('thdsin', '2341'),
('tjjin', '2341'),
('jjin', '2341'),
('jzin', '2341'),
('tin', '2341'),
('tjn', '2341'),
('tzin', '2341'),
('n', '2341'),
('thn', '2341'),
('tn', '2341'),
('zin', '2341'),
('in', '2341'),
('tin', '2341');
('thfdfznsfdf', '3221'),
('thfdsdfsdfzi', '2341'),
('thfdgsgfdin', '2341'),
('tzdsgfsfsgsgsddin', '2341'),
('thsdgsdgssgdazin', '2341'),
('thssgsgdgddszn', '2341'),
('tsgsdhdsdzin', '2341'),
('hgsgsdgdzn', '2341'),
('thgdgsdsdaszin', '2341'),
('thdsggdsin', '2341');
ALTER TABLE users AUTO_INCREMENT = 1;
