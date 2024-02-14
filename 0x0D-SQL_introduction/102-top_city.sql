-- Displays top 3 cities with the highest temp during July and August

-- Selects city and calculates the average temp (AS avg_temp) in DESC
SELECT city, AVG(value) AS avg_temp
-- Specifies the table from which to retrieve data
FROM `temperatures`
-- Filter the data for months 7(July) and 8(August)
WHERE month IN (7, 8)
-- Groups the result by city
GROUP BY `city`
-- Orders the result by avg temp in desc order
ORDER BY avg_temp DESC
-- Limits the output to the top 3 records
LIMIT 3;
