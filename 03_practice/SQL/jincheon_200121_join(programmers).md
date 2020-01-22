# JOIN (프로그래머스)

```sql
-- JOIN 1
SELECT animal_id
     , name
  from animal_outs a
 where not exists (
                    select 1
                      from animal_ins b
                     where a.animal_id = b.animal_id
                  )
 order by animal_id
;


```