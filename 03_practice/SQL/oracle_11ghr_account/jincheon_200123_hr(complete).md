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
--hire_year 	 avg_salary
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
-- 	  city  	  avg_salary 		count_emp
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
--employee_id 		first_name 	   last_name
--		101				Neena		Kochhar
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
--last_name 	salary
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
--employee_id 		 first_name 	  last_name 	depratment_name
--		104				Bruce			Ernst			IT
--		107				Diana			Lorentz			IT
--		113				Luis			Popp			Finance
--		119				Karen			Colmenares		Purchasing
--		124				Kevin			Mourgos			Shipping
--		127				James			Landry			Shipping
--		132				TJ				Olson			Shipping
--		135				Ki				Gee				Shipping
--		148				Gerald			Cambrault		Sales
--		155				Oliver			Tuvault			Sales
--		163				Danielle		Greene			Sales
--		171				William			Smith			Sales
--		172				Elizabeth		Bates			Sales
--		178				Kimberely		Grant			<Not Assigned>
--		182				Martha			Sullivan		Shipping
--		187				Anthony			Cabrio			Shipping
--		191				Randall			Perkins			Shipping
--		195				Vance			Jones			Shipping
--		198				Donald			OConnell		Shipping


--6. 업무명(job_title)이 ‘Sales Representative’인 직원 중에서 연봉(salary)이 9,000이상, 10,000 이하인
--   직원들의 이름(first_name), 성(last_name)과 연봉(salary)를 출력하시오

select a.first_name
		 , a.last_name
		 , a.salary
	from employees a
		 , jobs b
 where a.job_id = b.job_id
 	 and job_title = 'Sales Representative'
 	 and a.salary between 9000 and 10000
;

-- [결과]
--first_name	last_name		salary
--	Peter		Tucker			10000
--	David		Bernstein		9500
--	Peter		Hall			9000
--	Janette		King			10000
--	Patrick		Sully			9500
--	Allan		McEwen			9000
--	Danielle	Greene			9500
--	Harrison	Bloom			10000
--	Tayler		Fox				9600


--7. 부서별로 가장 적은 급여를 받고 있는 직원의 이름, 부서이름, 급여를 출력하시오.
--   이름은 last_name만 출력하며, 부서이름으로 오름차순 정렬하고,
--   부서가 같은 경우 이름을 기준 으로 오름차순 정렬하여 출력합니다.

select a.last_name
		 , b.department_name
		 , a.salary
	from employees a
		 , departments b
		 , (
				select min(salary) as min_salary
						 , department_id
					from employees
				 group by department_id
			 ) c
 where a.department_id = b.department_id
 	 and a.department_id = c.department_id
 	 and a.salary = c.min_salary
 order by a.department_id, a.last_name
;

-- [결과]
--last_name 		department_name 		salary
--Whalen			 Administration			4400
--Fay				Marketing				6000
--Colmenares		Purchasing				2500
--Mavris			Human Resources			6500
--Olson				Shipping				2100
--Lorentz			IT						4200
--Baer				Public Relations		10000
--Kumar				Sales					6100
--De Haan			Executive				17000
--Kochhar			Executive				17000
--Popp				Finance					6900
--Gietz				Accounting				8300


--8. EMPLOYEES 테이블에서 급여를 많이 받는 순서대로 조회했을 때 결과처럼 6번째부터 10 번째까지
--   5명의 last_name, first_name, salary를 조회하는 sql문장을 작성하시오.

select last_name
		 , first_name
		 , salary
	from (
				select last_name
						 , first_name
						 , salary
						 , rank() over(order by salary desc) as rank_salary
					from employees
 			 )
 where rank_salary between 5 and 10
;

-- [결과]
--last_name 	first_name 		salary
--Partners		Karen			13500
--Hartstein	  	Michael		 	13000
--Greenberg		Nancy		 	12008
--Higgins		Shelley		 	12008
--Errazuriz		Alberto		 	12000
--Ozer			Lisa		 	11500


--9. 사원의 부서가 속한 도시(city)가 ‘Seattle’인 사원의 이름, 해당 사원의 매니저 이름, 사원 의 부서이름을 출력하시오.
--   이때 사원의 매니저가 없을 경우 ‘<없음>’이라고 출력하시오. 이름은 last_name만 출력하며,
--   사원의 이름을 오름차순으로 정렬하시오.

select a.last_name
		 , case when a.manager_id is null then '<없음>'
		 				else b.last_name
		 	 end as manager_name
		 , c.department_name
	from employees a
		 , employees b
		 , departments c
		 , locations d
 where a.manager_id = b.employee_id(+)
   and a.department_id = c.department_id
 	 and c.location_id = d.location_id
 	 and d.city = 'Seattle'
 order by a.last_name
 ;
 
-- [결과]
--last_name 	manager_name 		department_name
--Baida			Raphaely			Purchasing
--Chen			Greenberg			Finance
--Colmenares	Raphaely			Purchasing
--De Haan		King				Executive
--Faviet		Greenberg			Finance
--Gietz			Higgins				Accounting
--Greenberg		Kochhar				Finance
--Higgins		Kochhar				Accounting
--Himuro		Raphaely			Purchasing
--Khoo			Raphaely			Purchasing
--King			<없음>			  	Executive
--Kochhar		King				Executive
--Popp			Greenberg			Finance
--Raphaely		King				Purchasing
--Sciarra		Greenberg			Finance
--Tobias		Raphaely			Purchasing
--Urman			Greenberg			Finance
--Whalen		Kochhar				Administration


--10. 각 업무(job) 별로 연봉(salary)의 총합을 구하고자 한다. 연봉 총합이 가장 높은 업무부터
--    업무명(job_title)과 연봉 총합을 조회하시오. 단 연봉총합이 30,000보다 큰 업무만 출력하시오.

select b.job_title
		 , sum(a.salary) as sum_salary
	from employees a
		 , jobs b
 where a.job_id = b.job_id
 group by b.job_title
having sum(a.salary) > 30000
 order by sum_salary desc
;

-- [결과]
--		job_title 						sum_salary
--Sales Representative					250500
--Shipping Clerk						64300
--Sales Manager							61000
--Stock Clerk							55700
--Accountant							39600
--Stock Manager							36400


--11. 각 사원(employee)에 대해서 사번(employee_id), 이름(first_name), 업무명(job_title),
--    부서 명(department_name)을 조회하시오.

SELECT	a.EMPLOYEE_ID
		 ,	a.FIRST_NAME
		 ,	c.JOB_TITLE
		 , 	b.DEPARTMENT_NAME
	FROM	employees a
		 , 	departments b
		 ,	jobs c
 WHERE 	a.DEPARTMENT_ID = b.DEPARTMENT_ID(+)
 	 AND	a.JOB_ID = c.JOB_ID(+)
 ;


--12. 2001~20003년사이에 입사한 직원의 이름(first_name), 입사일(hire_date), 관리자사번 (employee_id),
--    관리자 이름(fist_name)을 조회합니다. 단, 관리자가 없는 사원정보도 출력 결과에 포함시켜 출력한다.

SELECT	a.first_name
		 ,	a.hire_date
		 ,	b.employee_id AS manager_id
		 ,	b.first_name AS manager_first_name
	FROM	EMPLOYEES a
		 ,	EMPLOYEES b
 WHERE	a.MANAGER_ID = b.employee_id(+)
   AND	TO_NUMBER(TO_CHAR(a.hire_date, 'yyyy'))	BETWEEN	2001 AND 2003
;

-- [결과]
--first_name 		hire_date 		manager_id 		manager_first_name
--Steven			2003-06-17
--Lex				2001-01-13			100					Steven
--Nancy				2002-08-17			101					Neena
--Daniel			2002-08-16			108					Nancy
--Den				2002-12-07			100					Steven
--Alexander			2003-05-18			114					Den
--Payam				2003-05-01			100					Steven
--Renske			2003-07-14			123					Shanta
--Trenna			2003-10-17			124					Kevin
--Jennifer			2003-09-17			101					Neena
--Susan				2002-06-07			101					Neena
--Hermann			2002-06-07			101					Neena
--Shelley			2002-06-07			101					Neena
--William			2002-06-07			205					Shelley


--13. ‘Sales’ 부서에 속한 직원의 이름(first_name), 급여(salary), 부서이름(department_name)을 조회하시오.
--    단, 급여는 100번 부서의 평균보다 적게 받는 직원 정보만 출력되어야 한다.

SELECT a.FIRST_NAME
		 , a.SALARY
		 , b.DEPARTMENT_NAME
	from EMPLOYEES a
		 , DEPARTMENTS b
 WHERE a.DEPARTMENT_ID = b.DEPARTMENT_ID
 	 AND a.SALARY < (
 										SELECT AVG(c.salary)
 											FROM EMPLOYEES c
 										 WHERE c.DEPARTMENT_ID = 100
 										 GROUP BY c.department_id
 									)
   AND b.DEPARTMENT_NAME = 'Sales'
 ORDER BY a.SALARY
;


--14. Employees 테이블에서 입사한달(hire_date)별로 인원수를 조회하시오.

SELECT TO_CHAR(hire_date, 'yyyy-mm')
	   , COUNT(*)
	FROM EMPLOYEES
 GROUP BY TO_CHAR(hire_date, 'yyyy-mm')
 ORDER BY TO_CHAR(hire_date, 'yyyy-mm')
;


--15. 부서별 직원들의 최대, 최소, 평균급여를 조회하되,
--    평균급여가 ‘IT’ 부서의 평균급여보다 많고, ‘Sales’ 부서의 평균보다 적은 부서 정보만 출력하시오.

SELECT b.DEPARTMENT_NAME
	   , MAX(a.SALARY) AS max_salary
		 , MIN(a.SALARY) AS min_salary
		 , ROUND(AVG(a.SALARY), 2) AS avg_salary
	FROM EMPLOYEES a
		 , DEPARTMENTS b
 WHERE a.DEPARTMENT_ID = b.DEPARTMENT_ID
 GROUP BY b.DEPARTMENT_NAME
HAVING AVG(a.SALARY) > (
												SELECT AVG(a.SALARY)
											  	FROM EMPLOYEES a
											  		 , DEPARTMENTS b
											   WHERE a.DEPARTMENT_ID = b.DEPARTMENT_ID
											   GROUP BY b.DEPARTMENT_NAME
											  HAVING b.DEPARTMENT_NAME = 'IT'
											 )
	 AND AVG(a.SALARY) < (
	 											SELECT AVG(a.SALARY)
											  	FROM EMPLOYEES a
											  		 , DEPARTMENTS b
											   WHERE a.DEPARTMENT_ID = b.DEPARTMENT_ID
											   GROUP BY b.DEPARTMENT_NAME
											  HAVING b.DEPARTMENT_NAME = 'Sales'
	 										 )
;

-- [결과]
--department_name 		max_salary 		min_salary 		avg_salary
--Human Resources			6500			6500			6500
--Finance					12008			6900			8601.33


--16. 각 부서별로 직원이 한명만 있는 부서만 조회하시오.
--    단, 직원이 없는 부서에 대해서는 ‘<신생부서>’라는 문자열이 출력되도록 하고,
--    출력결과는 다음과 같이 부서명이 내림차순 으로 정렬되어야한다.

SELECT CASE WHEN COUNT(a.EMPLOYEE_ID) = 0 THEN '<신생부서>'
					  WHEN COUNT(a.EMPLOYEE_ID) = 1 THEN b.DEPARTMENT_NAME
			 END AS department_name
		 , COUNT(a.EMPLOYEE_ID) AS count_emp
	FROM EMPLOYEES a
		 , DEPARTMENTS b
 WHERE a.DEPARTMENT_ID(+) = b.DEPARTMENT_ID
 GROUP BY b.DEPARTMENT_NAME
HAVING COUNT(a.EMPLOYEE_ID) <= 1
 ORDER BY department_name DESC
;

-- [결과]
--department_name 		count_emp
--Public Relations			1
--Human Resources			1
--Administration			1
--<신생부서>				0
--<신생부서>				0
--<신생부서>				0
--<신생부서>				0
--<신생부서>				0
--<신생부서>				0
--<신생부서>				0
--<신생부서>				0
--<신생부서>				0
--<신생부서>				0
--<신생부서>				0
--<신생부서>				0
--<신생부서>				0
--<신생부서>				0
--<신생부서>				0
--<신생부서>				0


--17. 부서별 입사월별 직원수를 출력하시오.
--    단, 직원수가 5명 이상인 부서만 출력되어야 하며 출력결과는 부서이름 순으로 한다.

SELECT b.DEPARTMENT_NAME
     , TO_CHAR(a.HIRE_DATE, 'mm') AS hire_month
		 , COUNT(a.EMPLOYEE_ID) AS count_emp
	FROM EMPLOYEES a
		 , DEPARTMENTS b
 WHERE a.DEPARTMENT_ID = b.DEPARTMENT_ID
 	 AND b.DEPARTMENT_NAME IN (
														SELECT b.DEPARTMENT_NAME
															FROM EMPLOYEES a
																 , DEPARTMENTS b
														 WHERE a.DEPARTMENT_ID = b.DEPARTMENT_ID
														 GROUP BY b.DEPARTMENT_NAME
														HAVING COUNT(a.EMPLOYEE_ID) >= 5
														)
 GROUP BY b.DEPARTMENT_NAME , TO_CHAR(a.HIRE_DATE, 'mm')
 ORDER BY b.DEPARTMENT_NAME, hire_month
;

-- [결과]
--department_name	hire_month			count_emp
--Finance				03					1
--Finance				08					2
--Finance				09					2
--Finance				12					1
--IT					01					1
--IT					02					2
--IT					05					1
--IT					06					1
--Purchasing			05					1
--Purchasing			07					1
--Purchasing			08					1
--Purchasing			11					1
--Purchasing			12					2
--Sales					01					7
--Sales					02					2
--Sales					03					12
--Sales					04					3
--Sales					05					1
--Sales					08					2
--Sales					10					2
--Sales					11					3
--Sales					12					2
--Shipping				01					5
--Shipping				02					8
--Shipping				03					4
--Shipping				04					4
--Shipping				05					2
--Shipping				06					5
--Shipping				07					6
--Shipping				08					3
--Shipping				09					1
--Shipping				10					4
--Shipping				11					1
--Shipping				12					2


--18. 국가(country_name) 별 도시(city)별 직원수를 조회하시오.
--    단, 부서에 속해있지 않은 직원 이 있기 때문에 106명의 직원만 출력이 된다.

SELECT d.COUNTRY_NAME
		 , c.CITY
		 , COUNT(*) AS count_emp
	from EMPLOYEES a
		 , DEPARTMENTS b
		 , LOCATIONS c
		 , COUNTRIES d
 WHERE a.DEPARTMENT_ID = b.DEPARTMENT_ID
 	 AND b.LOCATION_ID = c.LOCATION_ID
 	 AND c.COUNTRY_ID = d.COUNTRY_ID
 GROUP BY d.COUNTRY_NAME, c.CITY
 ORDER BY d.COUNTRY_NAME, c.CITY
;

-- [결과]
--country_name 						city 									count_emp
--Canada							Toronto										2
--Germany							Munich										1
--United Kingdom					London										1
--United Kingdom					Oxford										34
--United States of America			Seattle										18
--United States of America			South San Francisco							45
--United States of America			Southlake									5


--19. 각 부서별 최대 급여자의 아이디(employee_id), 이름(first_name), 급여(salary)를 출력하시오.
--    단, 최대 급여자가 속한 부서의 평균급여를 마지막으로 출력하여 평균급여와 비교할 수 있게 할 것.

SELECT a.EMPLOYEE_ID
		 , a.FIRST_NAME
		 , b.DEPARTMENT_NAME
		 , a.SALARY
		 , ROUND(c.avg_salary, 2) AS dept_avg_salary
	FROM EMPLOYEES a
		 , DEPARTMENTS b
		 , (
				SELECT d.DEPARTMENT_ID
						 , MAX(d.SALARY) AS max_salary
						 , AVG(d.SALARY) AS avg_salary
 		  		FROM EMPLOYEES d
 		  	 GROUP BY d.DEPARTMENT_ID
				) c
 WHERE a.DEPARTMENT_ID = b.department_id
   AND a.DEPARTMENT_ID = c.DEPARTMENT_ID
   AND a.SALARY = c.max_salary
 ORDER BY a.EMPLOYEE_ID
;

-- [결과]
--employee_id 		first_name		 department_name 		salary 		dept_avg_salary
--100				Steven				Executive			24000			19333.33
--103				Alexander			IT					9000			5760
--108				Nancy				Finance				12008			8601.33
--114				Den					Purchasing			11000			4150
--121				Adam				Shipping			8200			3475.56
--145				John				Sales				14000			8955.88
--200				Jennifer			Administration		4400			4400
--201				Michael				Marketing			13000			9500
--203				Susan				Human Resources		6500			6500
--205				Shelley				Accounting			12008			10154
--204				Hermann				Public Relations	10000			10000


--20. 커미션(commission_pct)별 직원수를 조회하시오.
--    커미션은 아래실행결과처럼 0.2, 0.25는 모두 .2로, 0.3, 0.35는 .3 형태로 출력되어야 한다.
--    단, 커미션 정보가 없는 직원들도 있는 데 커미션이 없는 직원 그룹은 ‘<커미션 없음>’이 출력되게 한다.

SELECT CASE WHEN TO_CHAR(a.COMMISSION_PCT, '.9') IS NULL THEN '<커미션 없음>'
						ELSE TO_CHAR(a.COMMISSION_PCT, '.9')
				END AS commission_pct
		 , COUNT(a.EMPLOYEE_ID) AS count_emp
	FROM EMPLOYEES a
 GROUP BY TO_CHAR(a.COMMISSION_PCT, '.9')
 ORDER BY COMMISSION_PCT
;

-- [결과]
--COMMISSION_PCT 	count_emp
-- .1					6
-- .2					12
-- .3					13
-- .4					4
--<커미션 없음>			72


--21. 커미션(commission_pct)을 가장 많이 받은 상위 4명의 부서명(department_name),
--    직원명 (first_name), 급여(salary), 커미션(commission_pct) 정보를 조회하시오.
--    출력결과는 커미션 을 많이 받는 순서로 출력하되 동일한 커미션에 대해서는 급여가 높은 직원이 먼저 출력 되게 한다.

SELECT department_name
		 , first_name
		 , salary
		 , commission_pct
	from (
				SELECT b.DEPARTMENT_NAME
						 , a.FIRST_NAME
						 , a.SALARY
						 , a.COMMISSION_PCT
						 , rank() over(order by a.COMMISSION_PCT DESC, a.SALARY DESC) as rank_commission_pct
					FROM EMPLOYEES a
						 , DEPARTMENTS b
				 WHERE a.DEPARTMENT_ID = b.DEPARTMENT_ID
				   AND a.COMMISSION_PCT IS NOT NULL
   		)
 WHERE rank_commission_pct <= 4
;

-- [결과]
--department_name	first_name		salary	commission_pct
--Sales					John		14000		0.4
--Sales					Janette		10000		0.35
--Sales					Patrick		9500		0.35
--Sales					Allan		9000		0.35
```