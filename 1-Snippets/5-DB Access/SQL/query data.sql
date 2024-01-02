


postgres=# select * from emp;
 empid |       empname        | deptid | salary | mgrid
-------+----------------------+--------+--------+-------
   100 | David Wallace        |      9 |   1000 |   100
   101 | Michael Scott        |      1 |    900 |   100
   102 | Creed Bratton        |     12 |    300 |   101
   103 | Pam Beesly           |      5 |    300 |   101
   104 | Toby Flenderson      |     14 |    300 |   101
   105 | Dwight Shrute        |      2 |    600 |   101
   106 | Tod Pecker           |      8 |    400 |   101
   107 | Stanley Hudson       |      2 |    400 |   105
   108 | Phliiis Vance        |      2 |    450 |   105
   109 | Jim Halpert          |      2 |    500 |   105
   110 | Andy Bernard         |      2 |    300 |   105
   111 | Oscar Martinez       |      3 |    400 |   101
   112 | Kevin Malone         |      3 |    350 |   111
   113 | Angela Lipton        |      3 |    350 |   111
   114 | Meredith Palmer      |     13 |    300 |   101
   115 | Kelly Kapoor         |      4 |    300 |   101
   116 | Ryan Howard          |      7 |    100 |   101
(17 rows)



*** ======= list of all tables
SELECT
   *
FROM
   pg_catalog.pg_tables
WHERE
   schemaname != 'pg_catalog'
AND schemaname != 'information_schema';


*** ======= queries

select * from emp where deptid = 2

select * from emp where mgrid = 105

# also show mgr name
select aa.empname, bb.empname as "mgr name", 
from emp aa, emp bb
where aa.mgrid = bb.empid
and
aa.mgrid = 105

#with dept names
select aa.empname, bb.empname as "mgr name", dd.deptname
from emp aa, emp bb, dept dd
where aa.mgrid = bb.empid
and aa.deptid = dd.deptid

------ do types of joins

select * 
from dept inner join emp 
on dept.deptid = emp.deptid


select *
from dept left join emp
on dept.deptid = emp.deptid

select * 
from dept right join emp 
on dept.deptid = emp.deptid



select * 
from dept left join emp 
on dept.deptid = emp.deptid
where emp.deptid is null


select * 
from dept right join emp 
on dept.deptid = emp.deptid
where dept.deptid is null

select * 
from dept full join emp 
on dept.deptid = emp.deptid


select * 
from dept full join emp 
on dept.deptid = emp.deptid
where dept.deptid is null or emp.deptid is null


select * 
from dept left join emp 
on dept.deptid = emp.deptid
order by emp.empname

select mgrid, sum(salary)
from emp
group by mgrid

select empid, empname, deptname from emp cross join dept


select * 
from dept left outer join emp 
on dept.deptid = emp.deptid


select * from emp
where emp.deptid in
( select dd.deptid
from dept dd
where dd.deptname like 'C%' )




