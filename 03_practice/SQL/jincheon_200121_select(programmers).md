# select (프로그래머스)

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
SELECT animal_id
     , name
  from animal_ins
 where intake_condition = 'Sick'
 order by animal_id asc
;

-- select 4
SELECT animal_id
     , name
  from animal_ins
 where intake_condition <> 'Aged'
 order by animal_id asc
;

-- select 5
SELECT animal_id, name
  from animal_ins
 order by animal_id asc
;

-- select 6
SELECT animal_id
     , name
     , datetime
  from animal_ins
 order by name asc
        , datetime desc
;

-- select 7
select name
from (
        select name
          from animal_ins
         order by datetime asc
     )
where rownum = 1
;
```