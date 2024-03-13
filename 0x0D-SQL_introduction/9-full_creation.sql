-- Creates a second_table with multiple rows

CREATE TABLE IF NOT EXISTS second_table (
       id INT,
       name VARCHAR(256),
       score INT
);

INSERT INTO second_table (id, name, score) VALUE (1, "John", score);
INSERT INTO second_table (id, name, score) VALUE (2, "Alex", score);
INSERT INTO second_table (id, name, score) VALUE (3, "Bob", score);
INSERT INTO second_table (id, name, score) VALUE (4, "George", score);
