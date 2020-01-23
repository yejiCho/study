# SUM, MAX, MIN (프로그래머스)

```sql
-- SUM, MAX, MIN 1
SELECT max(datetime)
  from animal_ins
;

-- SUM, MAX, MIN 2
SELECT MIN(datetime)
  from animal_ins
;

-- SUM, MAX, MIN 3
SELECT count(*)
  from animal_ins
;

-- SUM, MAX, MIN 4
SELECT count(distinct name) 
  from animal_ins
 where name is not null
;
```