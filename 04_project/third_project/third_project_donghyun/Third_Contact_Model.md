```python

import cx_Oracle
from Third_Contact_DomainObject import DTO

# 도움 주신 분 Jincheon


class Model:
    # Jin_cheon = '반복되는 sql 구문을 함수로 만들어 보자'
    def __init__(self):
        self._USER = 'grandsisters'
        self._PASS = '1234'
        self._CONN = 'localhost:1521/xe'

    #   select all,
    def connect_all_re(self, sql):
        conn = cx_Oracle.connect(self._USER, self._PASS, self._CONN)
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        conn.close()

        return data

    #   select one,
    def connect_one_re(self, sql):
        conn = cx_Oracle.connect(self._USER, self._PASS, self._CONN)
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()
        cursor.close()
        conn.close()

        return data

    #   insert, update, delete
    def connect_commit(self, sql, data):
        conn = cx_Oracle.connect(self._USER, self._PASS, self._CONN)
        cursor = conn.cursor()
        cursor.execute(sql, data)
        cursor.close()
        conn.commit()
        conn.close()

    def id(self):
        sql='select max(Num) from new_Member'
        name_id = self.connect_one_re(sql)[0]
        nameid = name_id+1 if name_id else 1
        return nameid

    def insert_gid(self, dto):
        gname = dto.group
        sql = f"select DivisionNum from Divisions where DivisionName = '{gname}'"
        group = self.connect_one_re(sql)

        if group:
            group = group[0]
            return group
        else:
            sql = 'select max(DivisionNum) from Divisions'
            group_id = self.connect_one_re(sql)[0]
            group = group_id + 1

            sql2 = 'insert into Divisions values(:1, :2)'
            data = (group, f'{gname}')
            self.connect_commit(sql2, data)
            return group

    def insert_man(self,dto):
        Num = self.id()
        Nm = dto.name
        PhoneNumber = dto.phno
        Email = dto.email
        DivisionName = self.insert_gid(dto)

        sql = "insert into new_Member values(:1, :2, :3, :4, :5)"
        data = (Num, Nm, PhoneNumber, Email, DivisionName)
        self.connect_commit(sql, data)

    # 도움 주신 분 Do_yeon
    def select_man(self):
        sql = "select nM.Num,nM.Nm,nM.PhoneNumber,nM.Email,Dv.DivisionName " \
              "from new_Member nM,Divisions Dv " \
              "where nM.DivisionNum = Dv.DivisionNum"
        data = self.connect_all_re(sql)
        list = [DTO(row[0], row[1], row[2], row[3], row[4]) for row in data]
        return list

    def search_man(self, name):
        sql = f"select nM.Num,nM.Nm,nM.PhoneNumber,nM.Email,Dv.DivisionName " \
              f"from new_Member nM,Divisions Dv " \
              f"where nM.DivisionNum = Dv.DivisionNum " \
              f"and nM.Nm = '{name}'"
        data = self.connect_all_re(sql)
        list = [DTO(row[0], row[1],row[2],row[3],row[4]) for row in data]
        return list

    def delete_man(self, dto):
        sql = f"delete from new_Member where Num = :1"
        data = (dto.id,)
        self.connect_commit(sql, data)

    def up_man(self, dto):
        Num = dto.id
        Nm = dto.name
        PhoneNumber = dto.phno
        Email = dto.email
        DivisionName = self.insert_gid(dto)

        sql = "update new_Member set Nm = :1, PhoneNumber = :2, Email = :3, DivisionNum = :4 where Num = :1"
        data = (Nm, PhoneNumber, Email, DivisionName, Num)
        self.connect_commit(sql, data)

```