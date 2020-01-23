# GROUP BY (프로그래머스)

```sql
-- GROUP BY 1
SELECT animal_type
     , count(*) as count
  from animal_ins
 group by animal_type
 order by animal_type asc
;

-- GROUP BY 2
select name
     , count
  from ( 
        SELECT name
             , count(name) as count
          from animal_ins
         group by name
       )
 where count > 1
 order by name
;

-- GROUP BY 3
SELECT to_char(datetime, 'hh24') as hour
     , count(*) as count
  from animal_outs
 where to_char(datetime, 'hh24') between 9 and 19
 group by to_char(datetime, 'hh24')
 order by hour asc
;

-- GROUP BY 4
select b.hour
     , count(a.datetime) as count
  from animal_outs a
 right outer join (
                    select level-1 as hour
                    from dual
                    connect by level <= 24 
                   ) b
    on to_number(to_char(a.datetime, 'hh24')) = b.hour
 group by b.hour
 order by b.hour
;
```