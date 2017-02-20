# https://www.hackerrank.com/challenges/the-pads
select concat(name,"(",left(occupation, 1),")") from occupations order by name;
select concat("There are total ", count(occupation), " ", lower(occupation), "s.")
    from occupations 
        group by occupation 
        order by count(occupation), occupation;
