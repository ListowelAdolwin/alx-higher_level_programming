-- Lists score and name of records
-- Records that are NOT NULL
SELECT score, name
FROM second_table 
WHERE name IS NOT NULL 
ORDER BY score DESC;

