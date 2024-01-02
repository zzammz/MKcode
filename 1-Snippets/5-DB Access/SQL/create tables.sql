

*** ======= create db & tables
create database testdb

dept
CREATE TABLE dept (
   DEPTID INT PRIMARY KEY      NOT NULL,
   DEPTNAME           CHAR(50) NOT NULL
);

create table dept (
   deptid int primary key not null,
   deptname char (20) not null
);


create table dept 
(   deptid int primary key not null,
   deptname char (20) not null);


emp
create table emp (
   empid int primary key      not null,
   empname           char(20) not null,
   deptid            int not null,
   salary            int not null,
   mgrid             int not null
);

alter table emp
add salary int not null;

update dept
set deptname = 'Temp'
where deptid = 07;



*** ======= table schema
\d emp

*** ======= insert data

insert into dept (deptid, deptname) values (01, 'Mgmt');
insert into dept (deptid, deptname) values (02, 'Sales');
insert into dept (deptid, deptname) values (03, 'Accounting');
insert into dept (deptid, deptname) values (04, 'Cust Services');
insert into dept (deptid, deptname) values (05, 'Reception');
insert into dept (deptid, deptname) values (06, 'Warehouse');
insert into dept (deptid, deptname) values (07, 'Intern');
insert into dept (deptid, deptname) values (08, 'Field');
insert into dept (deptid, deptname) values (09, 'CFO');
insert into dept (deptid, deptname) values (10, 'Party Plan');
insert into dept (deptid, deptname) values (11, 'Coordinator');
insert into dept (deptid, deptname) values (12, 'Quality Assurance');
insert into dept (deptid, deptname) values (13, 'Supplier Relations');
insert into dept (deptid, deptname) values (14, 'Human Resources');



postgres=# select * from dept;
 deptid |       deptname
--------+----------------------
      1 | Mgmt
      2 | Sales
      3 | Accounting
      4 | Cust Services
      5 | Reception
      6 | Warehouse
      7 | Temp
      8 | Field
      9 | CFO
     10 | Party Plan
     11 | Coordinator
	 12 | Quality Assurance
	 13 | Supplier Relations
	 14 | Human Resources
(14 rows)

insert into emp (empid, empname, deptid, salary, mgrid) values (100, 'David Wallace', 09, 1000, 100);
insert into emp (empid, empname, deptid, salary, mgrid) values (101, 'Michael Scott', 01, 900, 100);
insert into emp (empid, empname, deptid, salary, mgrid) values (102, 'Creed Bratton', 12, 300, 101);
insert into emp (empid, empname, deptid, salary, mgrid) values (103, 'Pam Beesly', 05, 300, 101);
insert into emp (empid, empname, deptid, salary, mgrid) values (104, 'Toby Flenderson', 14, 300, 101);

insert into emp (empid, empname, deptid, salary, mgrid) values (105, 'Dwight Shrute', 02, 600, 101);
insert into emp (empid, empname, deptid, salary, mgrid) values (106, 'Tod Pecker', 08, 400, 101);
insert into emp (empid, empname, deptid, salary, mgrid) values (107, 'Stanley Hudson', 02, 400, 105);
insert into emp (empid, empname, deptid, salary, mgrid) values (108, 'Phliiis Vance', 02, 450, 105);
insert into emp (empid, empname, deptid, salary, mgrid) values (109, 'Jim Halpert', 02, 500, 105);
insert into emp (empid, empname, deptid, salary, mgrid) values (110, 'Andy Bernard', 02, 300, 105);

insert into emp (empid, empname, deptid, salary, mgrid) values (111, 'Oscar Martinez', 03, 400, 101);
insert into emp (empid, empname, deptid, salary, mgrid) values (112, 'Kevin Malone', 03, 350, 111);
insert into emp (empid, empname, deptid, salary, mgrid) values (113, 'Angela Lipton', 03, 350, 111);

insert into emp (empid, empname, deptid, salary, mgrid) values (114, 'Meredith Palmer', 13, 300, 101);

insert into emp (empid, empname, deptid, salary, mgrid) values (115, 'Kelly Kapoor', 04, 300, 101);
insert into emp (empid, empname, deptid, salary, mgrid) values (116, 'Ryan Howard', 07, 100, 101);

insert into emp (empid, empname, deptid, salary, mgrid) values (117, 'Jo Bennett', 00, 10000, 117);


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



