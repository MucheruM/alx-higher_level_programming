-- Displays top 3 cities temp during July and August DESC
SELECT city, AVG(value) AS avg_temp
FROM `temperatures`
WHERE month IN (7, 8)
GROUP BY `city`
GROUP BY `avg_temp`
DESC
LIMIT 3;
