-- displays average temperature by city ordered by temperature
SELECT city, AVG(value) AS 'avg_temp' FROM temperatures GROUP BY city ORDER BY avg_temp DESC;updates a value in a table
UPDATE second_table SET score = 2 WHERE name = 'Bob';
