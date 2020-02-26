```sql

-- PHONEBOOK 테이블 생성
CREATE TABLE PHONEBOOK (
	p_id number(35),
	pname VARCHAR2(50) NOT NULL,
	telnum	varchar2(50) not null,
	email varchar2(50) not null,
	sepno number(35) not null
);

-- PHONEBOOK에서 p_id를 PK로 설정
alter table PHONEBOOK
add constraints PHONEBOOK_p_id_pk
primary key(p_id);

-- SEPARATION 테이블 생성
CREATE TABLE SEPARATION (
	sepno number(35),
	sep varchar2(50) NOT NULL
);

-- SEPARATION에 sepno를 PK로 설정
alter table SEPARATION
add constraints SEPARATION_sepno_pk
primary key(sepno);

-- PHONEBOOK에서 SEPARATION의 sepno를 FK로 참조
alter table PHONEBOOK
add constraints PHONEBOOK_sepno_fk
foreign key(sepno)
references SEPARATION(sepno);

```