-- List the number of records with same score in MySQL server
SELECT `score`, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC
