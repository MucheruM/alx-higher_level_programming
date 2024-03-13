-- Lists all records with score >= 10 in second_table

-- Order score, name DESC
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score
DESC;
