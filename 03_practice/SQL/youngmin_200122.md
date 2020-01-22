# 프로그래머스
```sql
-- select 1
SELECT *
from animal_ins
order by animal_id
;


-- select 2
SELECT name, datetime 
from animal_ins
order by animal_id desc
;


-- select 3
SELECT animal_id, name
from animal_ins
where intake_condition = 'Sick'
order by animal_id
;


-- select 4
SELECT animal_id, name
from animal_ins
where intake_condition !='Aged'
order by animal_id
;


-- select 5
SELECT animal_id, name
from animal_ins
order by animal_id
;


-- select 6
SELECT animal_id, name, datetime
from animal_ins
order by name asc, datetime desc
;


-- select 7
SELECT name 
FROM (SELECT * 
      FROM animal_ins 
      ORDER BY datetime) 
WHERE rownum = 1;


-- sum, max, min 1
SELECT MAX(DATETIME)
    from ANIMAL_INS
;


-- sum, max, min 2
SELECT MIN(DATETIME)
    from ANIMAL_INS
;



-- sum, max, min 3 
SELECT count(*)
from ANIMAL_INS
;



-- sum, max, min 4
SELECT count(distinct name)
from animal_ins
;


-- group by 1
select animal_type,count(*)      
from animal_ins
group by animal_type
order by animal_type
;



-- group by 2
SELECT name, count(name)
from animal_ins
group by name
having count(name)>1
order by name
;



-- group by 3
select hour,count(hour)
from (SELECT to_char(datetime,'HH24')as hour
      from animal_outs)
group by hour
having hour between 9 and 19 
order by hour
;



-- group by 4 (요거는 모르겠음...)
SELECT A.HOUR, COUNT(B.DATETIME) AS COUNT
  FROM (SELECT LEVEL-1 AS HOUR
          FROM DUAL
        CONNECT BY LEVEL <=24) A
    LEFT JOIN ANIMAL_OUTS B
            ON A.HOUR = TO_NUMBER(TO_CHAR(B.DATETIME,'HH24'))
GROUP BY A.HOUR
ORDER BY A.HOUR


-- is null 1
SELECT animal_id
from animal_ins
where name is null
order by animal_id
;



-- is null 2
SELECT animal_id
from animal_ins
where name is not null
order by animal_id
;



-- is null 3
SELECT animal_type, nvl(name,'No name'), sex_upon_intake
from animal_ins
order by animal_id
;



-- join 1
select animal_id, named
from(SELECT a.animal_id as id, b.animal_id, a.name, b.name as named
    from animal_ins a, animal_outs b
    where a.animal_id(+) = b.animal_id)
where name is null
  and named is not null
order by animal_id
;



-- join 2
SELECT a.animal_id, a.name
from animal_ins a, animal_outs b
where a.animal_id = b.animal_id
  and a.datetime > b.datetime
 order by a.datetime
;



-- join 3
select *
from(select name, datetime
from(SELECT a.name, a.datetime, b.name as named, b.datetime as noout
    from animal_ins a, animal_outs b
    where a.animal_id = b.animal_id(+))
where noout is null
order by datetime)
where rownum<4
;



-- join 4
SELECT a.animal_id, a.animal_type, a.name
from animal_ins a, animal_outs b
where a.animal_id = b.animal_id
  and a.sex_upon_intake != b.sex_upon_outcome 
order by a.animal_id
;


-- string, date 1
SELECT animal_id, name, sex_upon_intake
from animal_ins
where name =any('Lucy','Ella','Pickle','Rogan','Sabrina', 'Mitty')
order by animal_id
;



-- string, date 2
select animal_id, name
from animal_ins
where upper(name) like upper('%el%') --upper함수 안배운거인듯
  and animal_type = 'Dog'
order by name
;



-- string, date 3
SELECT animal_id, name, decode(sex_upon_intake, 'Neutered Male','O'
                                              , 'Neutered Female','O'
                                              , 'Spayed Male','O'
                                              , 'Spayed Female','O'
                                              , 'X')as gender
from animal_ins
order by animal_id
;



-- string, date 4
select animal_id, name
from(SELECT a.animal_id, a.name, b.animal_id as ids, b.name as names
        from animal_ins a, animal_outs b
        where a.animal_id = b.animal_id    
        order by (b.datetime-a.datetime) desc)
where rownum<3        
;



-- string, date 5
SELECT animal_id, name, to_char(datetime,'YYYY-MM-DD')
from animal_ins
order by animal_id
;
```