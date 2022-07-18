-- Query to return countries by number of fans in descending order

SELECT origin, sum(fans) AS nb_fans FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
