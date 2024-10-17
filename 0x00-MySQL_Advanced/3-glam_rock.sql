-- Script that lists all bands with Glam rock as their style
-- in the database metal_bands
-- Calculates lifespan until between when formed and split
SELECT band_name, (IFNULL(split, 2022) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
