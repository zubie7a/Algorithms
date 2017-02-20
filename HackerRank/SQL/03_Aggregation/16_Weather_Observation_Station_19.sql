# https://www.hackerrank.com/challenges/weather-observation-station-19
select distinct round(sqrt(pow(x.minlat - x.minlong, 2) + pow(x.maxlat - x.maxlong, 2)), 4) from station
    join (
        select
            min(lat_n) as minlat,
            max(lat_n) as maxlat,
            min(long_w) as minlong,
            max(long_w) as maxlong
        from station
    ) x
