# String, Date

```sql

-- 1. 루시와 엘라 찾기

SELECT ANIMAL_ID
     , NAME
     , SEX_UPON_INTAKE
  FROM ANIMAL_INS
 WHERE NAME = any('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
 ORDER BY animal_id
;

-- 2. 이름에 el이 들어가는 동물 찾기

SELECT animal_id
     , name
  FROM animal_ins
 WHERE (name like '%El%' or name like '%el%') 
   and animal_type = 'Dog'
 ORDER BY name
;

-- 3. 중성화 여부 파악하기

SELECT animal_id
	 , name
     , case when sex_upon_intake like 'Neutered%' then  'O'
			when sex_upon_intake like 'Spayed%' then 'O'
    		else 'X'
    		 end as 중성화
  FROM animal_ins
 ORDER BY animal_id
;

-- 4. 오랜 기간 보호한 동물(2)

SELECT ANIMAL_ID, NAME
  FROM( 
        SELECT O.ANIMAL_ID
             , O.NAME
             , O.DATETIME - I.DATETIME AS PERIOD
		  FROM ANIMAL_INS I
             , ANIMAL_OUTS O
    	 WHERE I.ANIMAL_ID = O.ANIMAL_ID
		 ORDER BY PERIOD DESC
	    ) 
 WHERE ROWNUM <=2
;

-- 5. DATETIME에서 DATE로 형 변환

SELECT ANIMAL_ID
     , NAME
     , TO_CHAR(DATETIME, 'YYYY-MM-DD')
  FROM ANIMAL_INS
 ORDER BY ANIMAL_ID
;

```