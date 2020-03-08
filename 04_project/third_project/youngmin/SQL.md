```sql
--SQL

--contact 테이블 생성
create table contact (
		      id number primary key,
		      names varchar2(50) not null,
		      phone varchar2(50) not null,
		      email varchar2(50) not null,
		      div_id number not null
		     )
;

--division 테이블 생성
create table divisions (
			div_id number primary key,
			division varchar2(50)
			)
;

--FK설정(contact테이블의 div_id가 divisions테이블의 div_id를 참조)
alter table contact
add constraints divi_id
foreign key(div_id)
references divisions(div_id)
;

--테이블 내용확인
select * from contact;
select * from divisions;

--테이블 삭제
drop table contact;
drop table divisions;


--insert 해보기 위한 값들
insert into divisions values(1, '가족');
insert into divisions values(2, '친구');
insert into divisions values(3, '회사');
insert into divisions values(4, '기타');

```