# https://www.hackerrank.com/challenges/weather-observation-station-5
select city, length(city) from station order by length(city) asc limit 1;
select city, length(city) from station order by length(city) desc limit 1;
