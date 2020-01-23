# 프로그래머스
'''sql

- select_01

SELECT *
from ANIMAL_INS
ORDER BY ANIMAL_ID ;

- select_02

SELECT NAME, DATETIME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC

- select_03

SELECT ANIMAL_ID, NAME
from ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick'
ORDER BY ANIMAL_ID;

- select_04

SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION != 'Aged'
ORDER BY ANIMAL_ID;

- select_05

SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;

- select_06

SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME, DATETIME DESC;

- select _07

SELECT NAME
FROM ANIMAL_INS
WHERE DATETIME =(SELECT MIN(DATETIME) FROM ANIMAL_INS);

- sum,max,min_01

SELECT MAX(DATETIME) AS "시간"
FROM ANIMAL_INS;

- sum,max,min_02

SELECT MIN(DATETIME) AS "시간"
FROM ANIMAL_INS;

- sum,max,min_03

SELECT COUNT(ANIMAL_ID) AS COUNT
FROM ANIMAL_INS;

- sum,max,min_04

SELECT COUNT(DISTINCT NAME) AS COUNT
FROM ANIMAL_INS;

- group by_01

SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS COUNT
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE ASC;

- group by_02

SELECT NAME, COUNT(NAME) AS COUNT
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
GROUP BY NAME HAVING COUNT(NAME) > 1
ORDER BY NAME;

- group by_03

SELECT TO_CHAR(DATETIME,'HH24') AS HOUR, COUNT(DATETIME) AS COUNT
FROM ANIMAL_OUTS
WHERE 8 < TO_CHAR(DATETIME,'HH24') 
AND   TO_CHAR(DATETIME,'HH24') < 20
GROUP BY TO_CHAR(DATETIME,'HH24')
ORDER BY HOUR ASC;

- group by_04

SELECT A.HOUR, COUNT(B.DATETIME) AS COUNT
FROM (SELECT LEVEL-1 AS HOUR
      FROM DUAL
      CONNECT BY LEVEL <=24) A
      LEFT JOIN ANIMAL_OUTS B
      ON (A.HOUR = TO_NUMBER(TO_CHAR(B.DATETIME,'HH24')))
GROUP BY A.HOUR
ORDER BY A.HOUR

- is null_01

SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL
ORDER BY ANIMAL_ID ASC;

- is null_02

SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
ORDER BY  ANIMAL_ID ASC;

- is null_03

SELECT animal_type, NVL(name,'No name') as name, sex_upon_intake
from animal_ins
order by animal_id;

- join_01

SELECT b.animal_id, b.name
from animal_outs b
left join animal_ins a
on (a.animal_id = b.animal_id)
where a.datetime is null
order by b.animal_id;

- join_02

SELECT b.animal_id, b.name
from animal_outs b, animal_ins a
where a.animal_id = b.animal_id
and a.datetime > b.datetime
order by a.datetime asc;

- join_03

SELECT *
from ( select a.name, a.datetime
        from animal_ins a
        left join animal_outs b
        on (a.animal_id = b.animal_id)
        where b.datetime is null
        order by a.datetime
       )
where rownum <= 3;

- join_04

select a.animal_id, a.animal_type, a.name
from animal_ins a
inner join animal_outs b
on (a.animal_id = b.animal_id)
where a.sex_upon_intake !=  b.sex_upon_outcome;

- string, date_01

SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('Lucy','Ella','Pickle','Rogan','Sabrina','Mitty')
ORDER BY ANIMAL_ID;

- string, date_02

SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE 
UPPER(NAME) LIKE '%EL%'
AND ANIMAL_TYPE LIKE 'Dog'
ORDER BY NAME ;


- string, date_03

        CASE WHEN SEX_UPON_INTAKE LIKE 'Neut%' THEN 'O'
            WHEN SEX_UPON_INTAKE LIKE 'Spay%' THEN 'O'
            ELSE 'X'
            END AS 중성화
 FROM ANIMAL_INS
 ORDER BY ANIMAL_ID;

- string, date_04

SELECT *
 from (select b.animal_id, b.name
       from animal_outs b
       left join animal_ins a
       on(a.animal_id = b.animal_id)
       order by nvl((b.datetime - a.datetime),0) desc )
where rownum < 3;

- string, date_05

SELECT animal_id, name, to_char(datetime, 'YYYY-MM-DD') as 날짜
from animal_ins
order by animal_id;

'''