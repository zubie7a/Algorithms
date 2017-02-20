# https://www.hackerrank.com/challenges/weather-observation-station-18
select distinct round(abs(x.minlat - x.minlong) + abs(x.maxlat - x.maxlong), 4) from station 
    join (
        select 
            min(lat_n) as minlat,
            max(lat_n) as maxlat,
            min(long_w) as minlong,
            max(long_w) as maxlong
        from station
    ) x
