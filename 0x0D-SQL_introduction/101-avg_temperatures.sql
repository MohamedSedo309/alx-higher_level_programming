-- Import in hbtn_0c_0 database this table dump a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT city, AVG(value) AS avg_tmp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
