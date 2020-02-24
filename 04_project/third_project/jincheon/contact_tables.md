# contact_tables.sql

```sql
CREATE TABLE contacts(
	contno  NUMBER,
	nm      NVARCHAR2(20) NOT NULL,
	phoneno VARCHAR2(11)  NOT NULL,
	email   VARCHAR2(30),
	grpno   NUMBER(3)     NOT NULL
);

CREATE TABLE grps(
	grpno NUMBER,
	grpnm NVARCHAR2(20)
);

ALTER TABLE grps
ADD CONSTRAINTS grps_grpno_pk PRIMARY KEY (grpno)
ADD CONSTRAINTS grps_grpnm_uk UNIQUE (grpnm)
;

ALTER TABLE contacts
ADD CONSTRAINTS contacts_contno_pk PRIMARY KEY (contno)
ADD CONSTRAINTS contacts_grpno_fk  FOREIGN KEY (grpno) REFERENCES grps(grpno)
;

```