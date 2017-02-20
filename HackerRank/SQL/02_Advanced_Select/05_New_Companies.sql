# https://www.hackerrank.com/challenges/the-company
select
    distinct c.company_code, c.founder, e.leadCount, e.seniorCount, e.managerCount, e.employeeCount
    from company c
        join(
            select company_code,
            count(distinct lead_manager_code) as leadCount,
            count(distinct senior_manager_code) as seniorCount,
            count(distinct manager_code) as managerCount,
            count(distinct employee_code) as employeeCount
            from employee group by company_code        
        ) e on c.company_code = e.company_code
    order by c.company_code
