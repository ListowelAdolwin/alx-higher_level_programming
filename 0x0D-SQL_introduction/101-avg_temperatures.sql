-- Lists average of temperatures
-- Group them by city
-- Order them by temperature value
SELECT city, AVG(value) AS avg_temp 
FROM temperatures 
GROUP BY city 
ORDER BY avg_temp DESC;
