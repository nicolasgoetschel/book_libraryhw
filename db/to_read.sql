DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

CREATE TABLE authors (
  id SERIAL PRIMARY KEY,
  author_name VARCHAR(255)
);

CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  pages VARCHAR(255),
  genre VARCHAR(255),
  read BOOLEAN,
  author_id INT NOT NULL REFERENCES authors(id)
);