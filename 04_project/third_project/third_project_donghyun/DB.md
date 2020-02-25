--SELECT * FROM Divisions;
--SELECT * FROM new_Member;

--DELETE Divisions;
--DELETE new_Member;

--DROP TABLE Divisions cascade constraints;
--DROP TABLE new_Member cascade constraints;

--commit;

--INSERT INTO Divisions values(1, '가족');
--INSERT INTO Divisions values(2, '친구');
--INSERT INTO Divisions values(3, '회사');
--INSERT INTO Divisions values(4, '기타');

CREATE TABLE Divisions(
DivisionNum NUMBER PRIMARY KEY
,DivisionName VARCHAR2(30)
);

CREATE TABLE new_Member(
Num NUMBER PRIMARY KEY
,Nm VARCHAR2(50) NOT NULL
,PhoneNumber VARCHAR2(50) NOT NULL
,Email VARCHAR2(50) NOT NULL
,DivisionNum NUMBER NOT NULL
,CONSTRAINT DIV FOREIGN KEY(DivisionNum)
REFERENCES Divisions(DivisionNum)
);