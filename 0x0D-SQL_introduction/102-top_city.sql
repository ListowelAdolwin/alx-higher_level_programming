-- Display top 4 temperatures
-- Order in descending
SELECT city, value
FROM temperatures
ORDER BY  value DESC
LIMIT 3
