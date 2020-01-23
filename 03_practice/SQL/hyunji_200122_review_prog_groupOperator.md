# 집합연산자
## 집합연산자를 통해 연산할 시 테이블 간의 컬럼 개수가 동일하게 불러와야 한다.
```sql
-- SELECT O.ANIMAL_ID
--     , O.NAME
-- FROM (
--     SELECT * 
--     FROM ANIMAL_OUTS 
--     MINUS
--     SELECT *
--     FROM ANIMAL_INS 
--     ) -- 두 테이블의 컬럼 개수가 다르므로 연산 불가능
-- ORDER BY O.ANIMAL_ID
-- ;
SELECT ANIMAL_ID, NAME
FROM(SELECT ANIMAL_ID, NAME
    FROM ANIMAL_OUTS 
    MINUS
    SELECT ANIMAL_ID, NAME
    FROM ANIMAL_INS 
    )
ORDER BY ANIMAL_ID
;
```