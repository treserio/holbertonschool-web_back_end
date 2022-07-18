-- Query to return top 5 countries by number of fans

SELECT origin, sum(fans) AS nb_fans FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
