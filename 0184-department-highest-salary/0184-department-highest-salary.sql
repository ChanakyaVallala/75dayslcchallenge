# Write your MySQL query statement below
select Department,Employee,Salary from
(select d.name as Department,e.name as Employee,e.salary as Salary,dense_rank() over (partition by departmentID order by salary DESC) as rnk
from Employee e join Department d on e.departmentId=d.id) t where rnk=1;

