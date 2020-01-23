# hr계정 연습문제
## 현재(20.01.22) 4번까지 완료

``` sql

--1. 직책(Job Title)이 Sales Manager인 사원들의 입사년도와 입사년도(hire_date)별 평균 급여를 출력하시오.
--   출력 시 년도를 기준으로 오름차순 정렬하시오.
SELECT HIRE_DATE
		 , AVG(SALARY)
	FROM JOBS J
		 , EMPLOYEES E
 WHERE JOB_TITLE = 'Sales Manager'
   and J.JOB_ID = E.JOB_ID
GROUP BY HIRE_DATE 
ORDER BY HIRE_DATE
;


--2. 각 도시(city)에 있는 모든 부서 직원들의 평균급여를 조회하고자 한다.
--   평균급여가 가장 낮은 도시부터 도시명(city)과 평균연봉, 해당 도시의 직원수를 출력하시오.
--   단, 도시에 근 무하는 직원이 10명 이상인 곳은 제외하고 조회하시오.
SELECT CITY
		 , AVG(SALARY)
		 , COUNT(EMPLOYEE_ID)
	FROM LOCATIONS L
		 , EMPLOYEES E
		 , DEPARTMENTS D
 WHERE  L.LOCATION_ID = D.LOCATION_ID
 	 and	E.DEPARTMENT_ID = D.DEPARTMENT_ID 
GROUP BY CITY
HAVING COUNT(EMPLOYEE_ID)<=10
ORDER BY AVG(SALARY)
;


--3. ‘Public  Accountant’의 직책(job_title)으로 과거에 근무한 적이 있는 모든 사원의 사번과 이름을 출력하시오.
--   (현재 ‘Public Accountant’의 직책(job_title)으로 근무하는 사원은 고려 하지 않는다.)
--   이름은 first_name, last_name을 아래의 실행결과와 같이 출력한다.

--> 지금의 직책은 PA가 아니지만 과거의 직책이 PA인 사원 
SELECT E.EMPLOYEE_ID
		 , FIRST_NAME || LAST_NAME 
	FROM EMPLOYEES E
		 , JOBS J
		 , JOB_HISTORY JH
 WHERE J.JOB_TITLE = 'Public Accountant' 
 	 AND J.JOB_ID = JH.JOB_ID -- JH에는 JOB_TITLE이 없기 때문에두 테이블의 JOB_ID를 매치시켜야 한다.
 	 AND JH.EMPLOYEE_ID = E.EMPLOYEE_ID -- JH와 E테이블간의 연결 
 	 AND E.JOB_ID != JH.JOB_ID -- 현재는 PA가 아닌 사원을 고르는 조건
ORDER BY E.EMPLOYEE_ID
;

--4. 자신의 매니저보다 연봉(salary)를 많이 받는 직원들의 성(last_name)과 연봉(salary)를 출 력하시오.
SELECT JR.LAST_NAME
		 , JR.SALARY
	FROM EMPLOYEES JR --junior에 관련된 테이블로 쓸 것임.
		 , EMPLOYEES MG --manager에 관련된 테이블로 쓸 것임.
 WHERE JR.MANAGER_ID = MG.EMPLOYEE_ID
 	 AND JR.SALARY > MG.SALARY
;


--5. 2007년에 입사(hire_date)한 직원들의 사번(employee_id), 이름(first_name), 성(last_name),
--   부서명(department_name)을 조회합니다.
--   이때, 부서에 배치되지 않은 직원의 경우, ‘<Not Assigned>’로 출력하시오.

--> Employees 테이블의 DEPARTMENT_ID 는 NULL가능,
--> DEPARTMENTS의 DEPARTMENT_ID와 DEPARTMENT_NAME은 NOT NULL
SELECT HIRE_DATE, EMPLOYEE_ID, EMPLOYEE_ID, FIRST_NAME, LAST_NAME, DEPARTMENT_NAME
	FROM DEPARTMENTS D
		 , EMPLOYEES E
	WHERE TO_CHAR(HIRE_DATE,'YYYY') = '2007'
-- WHERE D.DEPARTMENT_ID = E.DEPARTMENT_ID -- D와 E테이블 연결.

;
SELECT EMPLOYEE_ID, DEPARTMENT_NAME, E.DEPARTMENT_ID
	FROM DEPARTMENTS D, EMPLOYEES E
WHERE E.DEPARTMENT_ID IS NULL;

```