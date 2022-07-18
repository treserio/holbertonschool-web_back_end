-- Query to return 'Glam rock' bands by descending
-- order of lifespan, (split - formed)

SELECT band_name, (if(split, split, year(CURDATE())) - formed) AS lifespan FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
