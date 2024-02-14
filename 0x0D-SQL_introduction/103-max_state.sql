-- Displays the masx temp of each state ordered by state name
SELECT `state`, MAX(value) AS max_temp
FROM temperatures
ORDER BY state 
