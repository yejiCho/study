# SELECT

# [프로그래머스-모든 레코드 조회하기](https://programmers.co.kr/learn/courses/30/lessons/59034?language=oracle)


```sql

# ANIMAL_INS 테이블의 모든 레코드 조회
# ANIMAL_ID 오름차순

SELECT      * 
FROM        ANIMAL_INS
ORDER BY    ANIMAL_ID
;


```

# [프로그래머스-역순 정렬하기](https://programmers.co.kr/learn/courses/30/lessons/59035?language=oracle)


```sql

# ANIMAL_INS 테이블에서 NAME, DATETIME 조회
# ANIMAL_ID를 역순 정렬

SELECT      NAME , DATETIME
FROM        ANIMAL_INS
ORDER BY    ANIMAL_ID   DESC
;


```

# [프로그래머스-아픈 동물 찾기](https://programmers.co.kr/learn/courses/30/lessons/59036?language=oracle)

```sql

# 아픈동물의 animal_id와 name 검색
# animal_id 오름차순 정렬

select      animal_id, name
from        animal_ins
where       intake_condition = 'Sick'
order by    animal_id
;

```

# [프로그래머스 - 어린 동물 찾기](https://programmers.co.kr/learn/courses/30/lessons/59037?language=oracle)

```sql

# INTAKE_CONDITION 이 AGED가 아닌 ANIMAL_ID 와 NAME 조회
# ANIMAL_ID 오름차순 정렬

SELECT      ANIMAL_ID   , NAME
FROM        ANIMAL_INS
WHERE       INTAKE_CONDITION != 'Aged'
ORDER BY    ANIMAL_ID

```

# [프로그래머스 - 동물의 아이디와 이름](https://programmers.co.kr/learn/courses/30/lessons/59403?language=oracle)

```sql

SELECT  ANIMAL_ID , NAME
FROM    ANIMAL_INS
ORDER BY ANIMAL_ID
;

```

# [프로그래머스 - 여러 기준으로 정렬하기](https://programmers.co.kr/learn/courses/30/lessons/59404?language=oracle)

```sql

SELECT      ANIMAL_ID, NAME, DATETIME
FROM        ANIMAL_INS

ORDER BY    NAME ASC, DATETIME DESC

;


```


# [프로그래머스 - 상위 n개 레코드](https://programmers.co.kr/learn/courses/30/lessons/59405)

```sql

# DATETIME 정렬해서 열번호가 1인 것 만 추출

SELECT  NAME
FROM    (SELECT NAME
        FROM    ANIMAL_INS
        order by DATETIME
        )
WHERE ROWNUM = 1
;

```

# SUM, MAX, MIN

# [프로그래머스 - 최댓값 구하기](https://programmers.co.kr/learn/courses/30/lessons/59415)

```sql

SELECT  MAX(DATETIME)
FROM    ANIMAL_INS
;

```

# [프로그래머스 - 최솟값 구하기](https://programmers.co.kr/learn/courses/30/lessons/59038)

```sql

SELECT  MIN(DATETIME)
FROM    ANIMAL_INS
;

```

# [프로그래머스 - 동물 수 구하기](https://programmers.co.kr/learn/courses/30/lessons/59406)

```sql

SELECT  COUNT(*)
FROM    ANIMAL_INS

```


# [프로그래머스 - 중복 제거하기](https://programmers.co.kr/learn/courses/30/lessons/59408?language=oracle)

```sql

SELECT  COUNT(DISTINCT  NAME)
FROM    ANIMAL_INS
WHERE   NAME IS NOT NULL
;

```

# GROUP BY

# [프로그래머스 - 고양이와 개는 몇 마리 있을까](https://programmers.co.kr/learn/courses/30/lessons/59040?language=oracle)

```sql

SELECT  ANIMAL_TYPE, COUNT(ANIMAL_TYPE)  count
FROM    ANIMAL_INS
GROUP   BY  ANIMAL_TYPE
ORDER   BY  ANiMAL_TYPE

```

# [프로그래머스 - 동명 동물 수 찾기](https://programmers.co.kr/learn/courses/30/lessons/59041?language=oracle)

```sql

SELECT      NAME, COUNT( NAME)
FROM        ANIMAL_INS
WHERE       NAME IS NOT NULL
GROUP BY    NAME
HAVING      COUNT(NAME) >= 2
ORDER BY    NAME
;

```

# [프로그래머스 - 입양 시각 구하기(1)](https://programmers.co.kr/learn/courses/30/lessons/59412)

```sql


SELECT  TO_CHAR(DATETIME, 'HH24') AS HOUR, COUNT(DATETIME) AS COUNT
FROM    ANIMAL_OUTS
WHERE   TO_CHAR(DATETIME, 'HH24') >= 9 AND TO_CHAR(DATETIME, 'HH24') <= 19
GROUP BY TO_CHAR(DATETIME, 'HH24')
ORDER BY    HOUR
;

```


# IS NULL

# [프로그래머스 - 이름이 없는 동물의 아이디](https://programmers.co.kr/learn/courses/30/lessons/59039?language=oracle)

```sql

SELECT  ANIMAL_ID
FROM    ANIMAL_INS
WHERE   NAME IS NULL
ORDER BY    ANIMAL_ID

```

# [프로그래머스 - 이름이 있는 동물의 아이디](https://programmers.co.kr/learn/courses/30/lessons/59407)

```sql

SELECT  ANIMAL_ID
FROM    ANIMAL_INS
WHERE   NAME IS NOT NULL
ORDER BY ANIMAL_ID

```

# [프로그래머스 - NULL 처리하기](https://programmers.co.kr/learn/courses/30/lessons/59410)

```sql

SELECT      ANIMAL_TYPE, NVL(NAME,'No name') NAME, SEX_UPON_INTAKE
FROM        ANIMAL_INS
ORDER BY    ANIMAL_ID

```

# JOIN

# [프로그래머스 - 없어진기록](https://programmers.co.kr/learn/courses/30/lessons/59042?language=oracle)

```sql

SELECT      B.ANIMAL_ID, B.NAME
FROM        ANIMAL_INS  A   
RIGHT OUTER JOIN    ANIMAL_OUTS B
ON          (A.ANIMAL_ID = B.ANIMAL_ID)
WHERE       A.ANIMAL_ID IS NULL
ORDER BY    B.ANIMAL_ID
;

```

# [프로그래머스 - 있었는데요 없었습니다.](https://programmers.co.kr/learn/courses/30/lessons/59043)

```sql
-- 보호 시작일 보다 입양일이 더 빠른 동물의 아이디와 이름을 조회하는 QL문 작성
-- 결과는 보호 시작일이 빠른순
-- a쿼리와 b쿼리의 동물아이디는 같지만 a.DATETIME이 더빠른 것 추출

SELECT      a.ANIMAL_ID, a.NAME
FROM        ANIMAL_INS  a, ANIMAL_OUTS  b
WHERE       a.ANIMAL_ID = b.ANIMAL_ID
AND         a.DATETIME  > b.DATETIME
ORDER BY    a.DATETIME
;

```

# [오랜 기간 보호한 동물](https://programmers.co.kr/learn/courses/30/lessons/59044)

```sql

--ORACLE은 3개까지 추출하기위해서 SELECT절로감싸줘야함
SELECT  *
FROM    (SELECT A.NAME  , A.DATETIME
        FROM    ANIMAL_INS  A
        LEFT    OUTER JOIN  ANIMAL_OUTS B
        ON  A.ANIMAL_ID = B.ANIMAL_ID
        WHERE   B.DATETIME IS NULL
        ORDER BY A.DATETIME)
WHERE   ROWNUM <= 3

-- SELECT a.name, a.datetime
-- FROM animal_ins a
-- LEFT OUTER JOIN animal_outs b on (a.animal_id = b.animal_id)
-- WHERE b.animal_id is NULL
-- AND    ROWNUM <= 3
-- ORDER BY a.datetime
-- ;

-- SELECT NAME, DATETIME 
-- FROM ANIMAL_INS A 
-- WHERE A.ANIMAL_ID NOT IN (
--                             SELECT B.ANIMAL_ID 
--                             FROM ANIMAL_OUTS B ) 
-- AND ROWNUM <= 3
-- ORDER BY A.DATETIME
-- ;



```

# [프로그래머스-보호소에서 중성화한 동물](https://programmers.co.kr/learn/courses/30/lessons/59045)

```sql

-- ANIMAL_INS : 동물 보호소에 들어온 동물의 정보를 담은 테이블
-- ANIMAL_OUT : 동물 보호소에서 입양 보낸 동물의 정보를 담은 테이블


SELECT  A.ANIMAL_ID  , A.ANIMAL_TYPE, A.NAME
FROM    ANIMAL_INS  A, ANIMAL_OUTS B

WHERE   A.ANIMAL_ID = B.ANIMAL_ID

AND     A.SEX_UPON_INTAKE  <>  B.SEX_UPON_OUTCOME
AND    ( B.SEX_UPON_OUTCOME  LIKE 'Spayed%' OR B.SEX_UPON_OUTCOME LIKE 'Neutered%' )
;   


```

# String , Date

# [프로그래머스-루시와 엘라 찾기](https://programmers.co.kr/learn/courses/30/lessons/59046)


```sql

-- Oracle 10g부처 정규식 함수가 추가 되었으며, 그 중에서 REGECP_LIKE 함수를 사용하여 다중 검색을 쉽게 할 수 있게 되었다.

SELECT  ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM    ANIMAL_INS
WHERE   REGEXP_LIKE (NAME, 'Lucy|Ella|Rogan|Sabrina|Mitty|Pickle')
ORDER   BY  ANIMAL_ID
;

SELECT  ANIMAL_ID   , NAME, SEX_UPON_INTAKE
FROM    ANIMAL_INS
WHERE   (NAME LIKE 'Lucy' OR NAME LIKE 'Ella' OR NAME LIKE 'Rogan' OR NAME LIKE 'Sabrina' OR NAME LIKE 'Mitty' OR NAME LIKE 'Pickle')
ORDER BY ANIMAL_ID

```

# [프로그래머스 - 이름에 el이 들어가는 동물 찾기](https://programmers.co.kr/learn/courses/30/lessons/59047)

```sql

SELECT ANIMAL_ID, NAME 
FROM ANIMAL_INS 
WHERE ( NAME LIKE '%el%' OR NAME LIKE '%El%')
AND ANIMAL_TYPE = 'Dog' 
ORDER BY NAME
;

```

# [프로그래머스 - 중성화 여부 파악하기](https://programmers.co.kr/learn/courses/30/lessons/59409)

```sql

--ORACLE CASE WHEN ~ THEN ~ ELSE END

-- 조건문과 조건문 사이에는 콤마(,)를 사용하지 않습니다.
-- CASE문은 반드시 END로 끝내야 합니다.
-- CASE문은 ANSI SQL 형식도 지원합니다.
-- 결과 부분은 NULL을 사용해서는 안됩니다.

--case when x < y then a when x = y then b else c end
--: 조건 x<y 가 true 일 경우 a 로, 조건 x = y 일 경우엔 b 로 그렇지 않으면 c 로 변경


SELECT  animal_id,name, 
    case when sex_upon_intake 
    like '%Neutered%' or sex_upon_intake like '%Spayed%' 
    then 'O'
    else 'X' end as 중성화
from 
    animal_ins
order by animal_id
;

```


# [프로그래머스 - 오랜 기간 보호한 동물 (2)](https://programmers.co.kr/learn/courses/30/lessons/59411)


```sql

SELECT  *
FROM    (SELECT  A.ANIMAL_ID, A.NAME
        FROM    ANIMAL_INS A, ANIMAL_OUTS B
        WHERE   A.ANIMAL_ID = B.ANIMAL_ID
        ORDER BY   B.DATETIME - A.DATETIME  DESC
        )
WHERE   ROWNUM <= 2
;

```

# [프로그래머스 - DATETIME에서 DATE로 형 변환](https://programmers.co.kr/learn/courses/30/lessons/59414)

```sql


SELECT ANIMAL_ID, NAME , TO_CHAR(DATETIME, 'YYYY-MM-DD' )AS 날짜
FROM    ANIMAL_INS
ORDER BY ANIMAL_ID


```