# https://www.hackerrank.com/challenges/weather-observation-station-16
select round(lat_n, 4) from station where lat_n > 38.7780 order by lat_n limit 1
