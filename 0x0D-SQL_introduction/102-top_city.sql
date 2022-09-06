-- Display top 4 temperatures
-- Order in descending
SELECT city, value
FROM temperatures
WHERE month = 7 OR month = 8
ORDER BY  value DESC
LIMIT 3;
