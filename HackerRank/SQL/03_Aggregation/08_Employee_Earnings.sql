# https://www.hackerrank.com/challenges/earnings-of-employees
select max(months*salary) as x, count(*) from employee where months*salary = (select max(months*salary) from employee)
