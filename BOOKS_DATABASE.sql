CREATE TABLE books(

id SERIAL PRIMARY KEY,
TITLE text,
cost NUMERIC(10,2),
rating VARCHAR(20),
url TEXT
);

SELECT * FROM books LIMIT 5;

SELECT COUNT(*) FROM books;

SELECT rating, COUNT(*) AS BOOKS_FOUND
FROM books
GROUP BY rating;

