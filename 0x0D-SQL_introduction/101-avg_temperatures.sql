-- displays the average temperature (Fahrenheit) by city
-- ordered by temperature (descending)
-- mysql -h localhost -u root -p hbtn_0c_0 <<EOF
source temperatures.sql;

SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE city IS NOT NULL
GROUP BY city
ORDER BY avg_temp DESC;
