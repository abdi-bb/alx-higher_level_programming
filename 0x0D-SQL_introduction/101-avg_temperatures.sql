-- displays the average temperature (Fahrenheit) by city
-- ordered by temperature (descending)
-- mysql -h localhost -u root -p hbtn_0c_0 <<EOF
source temperatures.sql;

SELECT city, AVG(temperature) AS avg_temp
FROM temperature
WHERE name IS NOT NULL
GROUP BY city
ORDER BY avg_temp DESC;
EOF

