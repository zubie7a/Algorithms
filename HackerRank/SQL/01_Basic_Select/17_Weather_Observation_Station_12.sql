# https://www.hackerrank.com/challenges/weather-observation-station-12
select distinct(city) from station
    where city rlike "^[^AaEeIiOoUu].*[^AaEeIiOoUu]$";
