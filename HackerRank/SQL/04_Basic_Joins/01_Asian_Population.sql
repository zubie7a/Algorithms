# https://www.hackerrank.com/challenges/asian-population
select sum(population)
    from city
    join (
        select code
            from country
            where continent = "Asia"
    ) a on a.code = countrycode
    where a.code = countrycode
