# JOIN
```SQL
-- 1. 없어진 기록 찾기

SELECT ANIMAL_ID
     , NAME
  FROM(
        SELECT ANIMAL_ID, NAME
          FROM ANIMAL_OUTS 
         MINUS
        SELECT ANIMAL_ID, NAME
          FROM ANIMAL_INS 
        )
 ORDER BY ANIMAL_ID
;

-- 2. 있었는데요 없었습니다

SELECT I. ANIMAL_ID
     , I. NAME
  FROM ANIMAL_INS I
     , ANIMAL_OUTS O
 WHERE I.DATETIME > O.DATETIME
   AND I.ANIMAL_ID = O.ANIMAL_ID
 ORDER BY I. DATETIME
;

-- 3. 오랜 기간 보호한 동물(1)

SELECT NAME, DATETIME
  FROM(
        SELECT NAME, DATETIME
          FROM   ANIMAL_INS I
         WHERE NOT EXISTS(
                           SELECT *
                             FROM ANIMAL_OUTS O
                            WHERE O.ANIMAL_ID = I.ANIMAL_ID
                            )  
         ORDER BY DATETIME
         )
 WHERE ROWNUM <=3
    ;

-- 4. 보호소에서 중성화한 동물

-- Spayed Female : 중성화된 암컷, Neutered Male : 중성화된 수컷

SELECT I.ANIMAL_ID
     , I.ANIMAL_TYPE
     , I.NAME
  FROM ANIMAL_INS I
     , ANIMAL_OUTS O
 WHERE I.ANIMAL_ID = O.ANIMAL_ID 
   AND I.SEX_UPON_INTAKE like 'Intact%'
   AND O.SEX_UPON_OUTCOME != I.SEX_UPON_INTAKE
 ORDER BY I.ANIMAL_ID
;

```