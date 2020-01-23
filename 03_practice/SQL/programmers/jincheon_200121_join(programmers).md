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

-- JOIN 2
SELECT animal_id
     , name
  from animal_ins a
 where exists (
               select 1
                 from animal_outs b
                where a.animal_id = b.animal_id
                  and a.datetime > b.datetime
              ) 
 order by datetime
;

-- JOIN 3
select name
     , datetime
  from (
        SELECT name
             , datetime
          from animal_ins a
         where not exists (
                            select 1
                              from animal_outs b
                             where a.animal_id = b.animal_id
                         )
         order by datetime
      ) 
 where rownum <= 3
;

-- JOIN 4
SELECT a.animal_id
     , a.animal_type
     , a.name
  from animal_ins a
     , animal_outs b 
 where a.animal_id = b.animal_id
   and a.sex_upon_intake like 'Intact%'
   and (   b.sex_upon_outcome like 'Spayed%' 
        or b.sex_upon_outcome like 'Neutered%')
 order by a.animal_id
;


```