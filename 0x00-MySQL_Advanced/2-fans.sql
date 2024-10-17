-- Script that ranks country of origins of bands
-- ordered by the number of fans
-- Script executes on any database
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
