# String, Date (프로그래머스)

```sql
-- String, Date 1
SELECT animal_id
     , name
     , sex_upon_intake
  from animal_ins
 where name = any('Lucy','Ella','Pickle','Rogan','Sabrina','Mitty')
 order by animal_id
;

-- String, Date 2
SELECT animal_id
     , name
 from animal_ins
where (   name like 'El%'
       or name like '%el%' )
  and animal_type = 'Dog'
order by name
;

-- String, Date 3
SELECT animal_id
     , name
     , case when sex_upon_intake like 'Neutered%' then 'O'
            when sex_upon_intake like 'Spayed%' then 'O'
            else 'X'
        end as 중성화
  from animal_ins
 order by animal_id
;

-- String, Date 4
select animal_id
     , name
  from (
        SELECT a.animal_id
             , a.name
          from animal_ins a
             , animal_outs b
         where a.animal_id = b.animal_id
         order by b.datetime - a.datetime desc
        )
 where rownum <= 2
;

-- String, Date 5
SELECT animal_id
     , name
     , to_char(datetime, 'YYYY-MM-DD') as 날짜
  from animal_ins
 order by animal_id
;
```