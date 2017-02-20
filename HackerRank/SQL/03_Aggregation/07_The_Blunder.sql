# https://www.hackerrank.com/challenges/the-blunder
select ceil(avg(salary) - avg(cast(replace(concat(salary, ""), "0", "") as unsigned))) from employees
