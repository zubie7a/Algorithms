# https://www.hackerrank.com/challenges/weather-observation-station-11
select distinct(city) from station
    where city rlike "^[^AaEeIiOoUu].*" or city rlike ".*[^AaEeIiOoUu]$";
