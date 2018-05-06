# https://www.hackerrank.com/challenges/african-cities
select distinct name
    from city
    join (
        select code
            from country
            where continent = "Africa"
    ) a on a.code = countrycode
    where a.code = countrycode
