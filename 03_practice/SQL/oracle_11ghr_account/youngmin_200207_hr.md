```sql
--오라클 11g hr계정 연습문제

--1. 직책(Job Title)이 Sales Manager인 사원들의 입사년도와 입사년도(hire_date)별 평균 급여를 출력하시오.
--   출력 시 년도를 기준으로 오름차순 정렬하시오.

select to_char(a.hire_date,'YYYY')as hire_year
	 , avg(a.salary)as avgsal
  from employees a
	 , jobs b
 where a.job_id = b.job_id
   and b.Job_Title = 'Sales Manager'
group by a.hire_date
order by hire_year
;


--2. 각 도시(city)에 있는 모든 부서 직원들의 평균급여를 조회하고자 한다.
--   평균급여가 가장 낮은 도시부터 도시명(city)과 평균연봉, 해당 도시의 직원수를 출력하시오.
--   단, 도시에 근 무하는 직원이 10명 이상인 곳은 제외하고 조회하시오.

select *
	from(
		select c.city
			 , round(avg(salary))as avgsal
			 , count(*)as counts
		  from (
			 	select a.department_id
			 		 , b.city
				  from departments a
					 , locations b
			 	 where a.location_id = b.location_id
			 	) c
			    , employees d
		 where c.department_id = d.department_id
		 group by city
		 order by avgsal
        )
where counts<11
;


--3. ‘Public  Accountant’의 직책(job_title)으로 과거에 근무한 적이 있는 모든 사원의 사번과 이름을 출력하시오.
--   (현재 ‘Public Accountant’의 직책(job_title)으로 근무하는 사원은 고려 하지 않는다.)
--   이름은 first_name, last_name을 아래의 실행결과와 같이 출력한다.

select d.employee_id
	 , d.first_name
	 , d.last_name
from (
	  select a.job_title
		   , b.employee_id
		   , b.start_date
		   , b.end_date
		from jobs a
		   , job_history b
	   where a.job_id = b.job_id
  	     and a.job_title = 'Public Accountant'
  	  ) c
  	  , employees d
where c.employee_id = d.employee_id
  and c.end_date is not null
order by d.employee_id
;


--4. 자신의 매니저보다 연봉(salary)를 많이 받는 직원들의 성(last_name)과 연봉(salary)를 출 력하시오.

select a.last_name
	 , b.salary
  from employees a
	 , employees b
 where a.manager_id = b.employee_id
   and a.salary > b.salary
;


--5. 2007년에 입사(hire_date)한 직원들의 사번(employee_id), 이름(first_name), 성(last_name),
--   부서명(department_name)을 조회합니다.
--   이때, 부서에 배치되지 않은 직원의 경우, ‘<Not Assigned>’로 출력하시오.

select a.employee_id
	 , a.first_name
	 , a.last_name
	 , nvl(b.department_name, 'Not Assigned')as dename
  from (
		select employee_id
			 , first_name
			 , last_name
			 , department_id
			 , to_char(hire_date,'YYYY')as hire_year
	      from employees
		) a
	    , departments b
where a.department_id = b.department_id(+)
  and a.hire_year = '2007'
order by a.employee_id
;


--6. 업무명(job_title)이 ‘Sales Representative’인 직원 중에서 연봉(salary)이 9,000이상, 10,000 이하인
--   직원들의 이름(first_name), 성(last_name)과 연봉(salary)를 출력하시오

select a.first_name
	 , a.last_name
	 , a.salary
  from employees a
	 , jobs b
 where a.job_id = b.job_id
   and b.job_title = 'Sales Representative'
   and a.salary between 9000 and 10000
;


--7. 부서별로 가장 적은 급여를 받고 있는 직원의 이름, 부서이름, 급여를 출력하시오.
--   이름은 last_name만 출력하며, 부서이름으로 오름차순 정렬하고,
--   부서가 같은 경우 이름을 기준 으로 오름차순 정렬하여 출력합니다.

select c.last_name
	 , d.department_name
	 , c.salary
  from (
        select b.last_name
			 , b.salary
			 , b.department_id
		  from (
				select department_id
					 , min(salary) as salary
				  from employees
			    group by department_id
			 	) a
				, employees b
		  where a.department_id = b.department_id
  			and a.salary = b.salary
  	    )c
  	    , departments d
where c.department_id = d.department_id
order by d.department_name
	   , c.last_name
;


--8. EMPLOYEES 테이블에서 급여를 많이 받는 순서대로 조회했을 때 결과처럼 6번째부터 10 번째까지
--   5명의 last_name, first_name, salary를 조회하는 sql문장을 작성하시오.

select last_name
	 , first_name
	 , salary
  from (
	    select last_name
	  	     , first_name
		     , salary
		     , rownum as num
		  from (
		  	    select last_name
		  		     , first_name
		  		     , salary
			      from employees
			    order by salary desc
		  	    )
		)
 where num between 6 and 10
;


--9. 사원의 부서가 속한 도시(city)가 ‘Seattle’인 사원의 이름, 해당 사원의 매니저 이름, 사원 의 부서이름을 출력하시오.
--   이때 사원의 매니저가 없을 경우 ‘<없음>’이라고 출력하시오. 이름은 last_name만 출력하며,
--   사원의 이름을 오름차순으로 정렬하시오.

select last_name
	 , nvl(manager_name, '<없음>') as manager_name
	 , department_name
  from (
 		select a.last_name
 			 , b.last_name as manager_name
 			 , c.department_name
		  from employees a
			 , employees b
			 , departments c
			 , locations d
 		 where a.manager_id = b.employee_id(+)
 		   and a.department_id = c.department_id
		   and c.location_id = d.location_id
		   and d.city = 'Seattle'
		)
order by last_name
;


--10. 각 업무(job) 별로 연봉(salary)의 총합을 구하고자 한다. 연봉 총합이 가장 높은 업무부터
--    업무명(job_title)과 연봉 총합을 조회하시오. 단 연봉총합이 30,000보다 큰 업무만 출력하시오.
-- {group by에 선언을 해야 select절에서 사용할 수 있다는것 기억하자!!}

select b.job_title
	 , sum(a.salary)as sumsal
  from employees a
	 , jobs b
 where a.job_id = b.job_id
group by b.job_title
having sum(a.salary) > 30000
order by sumsal desc
;


--11. 각 사원(employee)에 대해서 사번(employee_id), 이름(first_name), 업무명(job_title),
--    부서 명(department_name)을 조회하시오.

select a.employee_id
	 , a.first_name
	 , c.job_title
	 , b.department_name
  from employees a
	 , departments b
	 , jobs c
 where a.department_id = b.department_id(+)
   and a.job_id = c.job_id(+)
order by a.employee_id
;


--12. 2001~2003년사이에 입사한 직원의 이름(first_name), 입사일(hire_date), 관리자사번 (employee_id),
--    관리자 이름(first_name)을 조회합니다. 단, 관리자가 없는 사원정보도 출력 결과에 포함시켜 출력한다.

select a.first_name
	 , a.hire_date
	 , a.employee_id
	 , b.first_name
  from employees a
	 , employees b
 where a.manager_id = b.employee_id(+)
   and to_char(a.hire_date,'YYYY') between 2001 and 2003
 ;


--13. ‘Sales’ 부서에 속한 직원의 이름(first_name), 급여(salary), 부서이름(department_name)을 조회하시오.
--    단, 급여는 100번 부서의 평균보다 적게 받는 직원 정보만 출력되어야 한다.

select a.first_name
	 , a.salary
	 , b.department_name
  from employees a
	 , departments b
 where a.department_id = b.department_id
   and b.department_name = 'Sales'
   and a.salary < (
    			   select avg(salary)
    				 from employees
    		 		where department_id = '100'
   					group by department_id
   				   )
order by a.salary
;


--14. Employees 테이블에서 입사한달(hire_date)별로 인원수를 조회하시오.

select count(*)
  from employees
group by to_char(hire_date,'mm')
;



--15. 부서별 직원들의 최대, 최소, 평균급여를 조회하되,
--    평균급여가 ‘IT’ 부서의 평균급여보다 많고, ‘Sales’ 부서의 평균보다 적은 부서 정보만 출력하시오.

select max(salary)
	 , min(salary)
	 , round(avg(salary))as avgsal
  from employees
group by department_id
having avg(salary) > (
 					  select avg(a.salary)
 						from employees a
 					 	   , departments b
 					   where a.department_id = b.department_id
 						 and b.department_name = 'IT'
 					  group by a.department_id
 					  )
   and avg(salary) < (
	 				  select avg(a.salary)
 						from employees a
 						   , departments b
 					   where a.department_id = b.department_id
 						 and b.department_name = 'Sales'
 				 	  group by a.department_id
	 				  )
;


--16. 각 부서별로 직원이 한명만 있는 부서만 조회하시오.
--    단, 직원이 없는 부서에 대해서는 ‘<신생부서>’라는 문자열이 출력되도록 하고,
--    출력결과는 다음과 같이 부서명이 내림차순 으로 정렬되어야한다.

select count(a.employee_id)as count_emp
	 , case
	   when count(a.employee_id)=0 then '<신생부서>'
	   else b.department_name
	   end as department_name
  from employees a
	 , departments b
 where a.department_id(+) = b.department_id
group by b.department_name
having count(a.employee_id)<=1
order by department_name desc
;


--17. 부서별 입사월별 직원수를 출력하시오.
--    단, 직원수가 5명 이상인 부서만 출력되어야 하며 출력결과는 부서이름 순으로 한다.

select b.department_name
	 , to_char(hire_date, 'MM')as hire_month
	 , count(*)
  from employees a
	 , departments b
 where a.department_id = b.department_id(+)
   and a.department_id in(
   						  select department_id
   							from employees
   						  group by department_id
   			 			  having count(employee_id)>=5
   						  )
group by department_name
	   , to_char(hire_date, 'MM')
order by b.department_name
;


--18. 국가(country_name) 별 도시(city)별 직원수를 조회하시오.
--    단, 부서에 속해있지 않은 직원 이 있기 때문에 106명의 직원만 출력이 된다.

select count(*)
	 , d.country_name
	 , c.city
  from employees a
	 , departments b
	 , locations c
	 , countries d
 where a.department_id = b.department_id
   and b.location_id = c.location_id
   and c.country_id = d.country_id
group by d.country_name
	   , c.city
;


--19. 각 부서별 최대 급여자의 아이디(employee_id), 이름(first_name), 급여(salary)를 출력하시오.
--    단, 최대 급여자가 속한 부서의 평균급여를 마지막으로 출력하여 평균급여와 비교할 수 있게 할 것.

select a.employee_id
	 , a.first_name
	 , a.salary
	 , round(b.sal_avg)
  from employees a
       , (
		  select max(salary)as sal_max
	    , avg(salary)as sal_avg
	    , department_id
		    from employees
		  group by department_id
		  )b
 where a.department_id = b.department_id
   and a.salary = b.sal_max
order by a.employee_id
;


--20. 커미션(commission_pct)별 직원수를 조회하시오.
--    커미션은 아래실행결과처럼 0.2, 0.25는 모두 .2로, 0.3, 0.35는 .3 형태로 출력되어야 한다.
--    단, 커미션 정보가 없는 직원들도 있는 데 커미션이 없는 직원 그룹은 ‘<커미션 없음>’이 출력되게 한다.

select count(*)
	 , case
	   when to_char(commission_pct, '.9') is null then '<커미션 없음>'
	   else to_char(commission_pct, '.9')
	   end as commission
  from employees
group by to_char(commission_pct, '.9')
;


--21. 커미션(commission_pct)을 가장 많이 받은 상위 4명의 부서명(department_name),
--    직원명 (first_name), 급여(salary), 커미션(commission_pct) 정보를 조회하시오.
--    출력결과는 커미션 을 많이 받는 순서로 출력하되 동일한 커미션에 대해서는 급여가 높은 직원이 먼저 출력 되게 한다.

select c.department_name
	 , c.first_name
	 , c.salary
	 , c.commission_pct
from (
	  select a.employee_id
		   , b.department_name
		   , a.first_name
		   , a.salary
		   , a.commission_pct
		from employees a
		   , departments b
	   where a.department_id = b.department_id
		 and a.commission_pct is not null
	  order by a.commission_pct desc
			 , a.salary desc
	  )c
 where rownum<=4
;


```