create database  if not exists book;

CREATE TABLE  books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    price VARCHAR(20),
    press VARCHAR(255),
    content TEXT
);