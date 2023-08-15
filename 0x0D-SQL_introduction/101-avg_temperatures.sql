-- Displays the average temperature by city ordered by temperature (descending)
-- from the table temperatures
SELECT city, AVG(value) AS avg_temp
  FROM temperatures
 GROUP BY city
 ORDER BY avg_tmp DESC;
