# 오라클 11g hr계정 연습문제

```sql
--1. 직책(Job Title)이 Sales Manager인 사원들의 입사년도와 입사년도(hire_date)별 평균 급여를 출력하시오.
--   출력 시 년도를 기준으로 오름차순 정렬하시오.

select hire_year
		 , avg(salary) as avg_salary
	from (
				select to_char(a.hire_date, 'yyyy') as hire_year
						 , a.salary
				  from employees a
				  	 , jobs b
				 where a.job_id = b.job_id
				 	 and b.job_title = 'Sales Manager'
	  	 )
 group by hire_year
 order by hire_year
;

-- [결과]
--hire_year avg_salary
--	2004			14000
--  2005			12750
--	2007			11000
--	2008			10500


--2. 각 도시(city)에 있는 모든 부서 직원들의 평균급여를 조회하고자 한다.
--   평균급여가 가장 낮은 도시부터 도시명(city)과 평균연봉, 해당 도시의 직원수를 출력하시오.
--   단, 도시에 근 무하는 직원이 10명 이상인 곳은 제외하고 조회하시오.

select c.city
		 , round(avg(a.salary), 2) as avg_salary
		 , count(a.employee_id) as count_emp
	from employees a
		 , departments b
		 , locations c
 where a.department_id = b.department_id
   and b.location_id = c.location_id
 group by c.city
having count(a.employee_id) < 10
 order by avg_salary
;

-- [결과]
-- 		city  	avg_salary count_emp
--	Southlake		5760				5
--	London			6500				1
--	Toronto			9500				2
--	Munich			10000				1


--3. ‘Public  Accountant’의 직책(job_title)으로 과거에 근무한 적이 있는 모든 사원의 사번과 이름을 출력하시오.
--   (현재 ‘Public Accountant’의 직책(job_title)으로 근무하는 사원은 고려 하지 않는다.)
--   이름은 first_name, last_name을 아래의 실행결과와 같이 출력한다.

select a.employee_id
		 , a.first_name
		 , a.last_name
	from employees a
		 , job_history b
		 , jobs c
 where a.employee_id = b.employee_id
 	 and b.job_id = c.job_id
 	 and c.job_title = 'Public Accountant'
;

-- [결과]
--employee_id first_name last_name
--		101				Neena			Kochhar
--		200				Jennifer	Whalen


--4. 자신의 매니저보다 연봉(salary)를 많이 받는 직원들의 성(last_name)과 연봉(salary)를 출 력하시오.

select a.last_name
		 , a.salary
	from employees a
		 , employees b
 where a.manager_id = b.employee_id
   and a.salary > b.salary
;

-- [결과]
--last_name salary
--	Ozer		11500
--	Abel		11000


--5. 2007년에 입사(hire_date)한 직원들의 사번(employee_id), 이름(first_name), 성(last_name),
--   부서명(department_name)을 조회합니다.
--   이때, 부서에 배치되지 않은 직원의 경우, ‘<Not Assigned>’로 출력하시오.

select a.employee_id
		 , a.first_name
		 , a.last_name
		 , case when b.department_name is null then '<Not Assigned>'
		 				else b.department_name
		   end as department_name
  from employees a
  	 , departments b
 where a.department_id = b.department_id(+)
   and to_char(hire_date, 'yyyy') = '2007'
;


-- [결과]
--employee_id first_name last_name depratment_name
--		104				Bruce			Ernst					IT
--		107				Diana			Lorentz				IT
--		113				Luis			Popp				Finance
--		119				Karen			Colmenares	Purchasing
--		124				Kevin			Mourgos			Shipping
--		127				James			Landry			Shipping
--		132				TJ				Olson				Shipping
--		135				Ki				Gee					Shipping
--		148				Gerald		Cambrault		Sales
--		155				Oliver		Tuvault			Sales
--		163				Danielle	Greene			Sales
--		171				William		Smith				Sales
--		172				Elizabeth	Bates				Sales
--		178				Kimberely	Grant				<Not Assigned>
--		182				Martha		Sullivan		Shipping
--		187				Anthony		Cabrio			Shipping
--		191				Randall		Perkins			Shipping
--		195				Vance			Jones				Shipping
--		198				Donald		OConnell		Shipping
```