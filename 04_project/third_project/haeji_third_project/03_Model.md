```python

# Model

import cx_Oracle
from Domain import Domain

class Model:

    # 모든 검색 결과를 불러오는 sql 실행함수 생성
    def sel_all(self, sql):
        conn = cx_Oracle.connect("haeji/1234@localhost:1521/xe")
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()

        cursor.close()
        conn.close()
        return data

    # 하나의 검색 결과를 불러오는 sql 실행함수 생성
    def sel_one(self, sql):
        conn = cx_Oracle.connect("haeji/1234@localhost:1521/xe")
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()

        cursor.close()
        conn.close()
        return data

    # delete, update에 쓸 sql 함수 생성
    def dml(self, sql, data):
        conn = cx_Oracle.connect("haeji/1234@localhost:1521/xe")
        cursor = conn.cursor()
        cursor.execute(sql, data)
        cursor.close()
        conn.commit()
        conn.close()

    # delete, update에 쓸 sql 함수 생성(data 없는 버전)
    def dml_one(self, sql):
        conn = cx_Oracle.connect("haeji/1234@localhost:1521/xe")
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()

    """
    phonebook에 있는 p_id(pk) 중 max 값을 검색해서 sel_id에 저장한 다음
    p_id가 없을 경우 1로 시작하며, 있을 경우 max p_id에서 +1을 해서 저장
    """
    def select_maxid(self):
        sql = "select max(p_id) from PHONEBOOK"
        sel_id = self.sel_one(sql)[0]
        p_id = sel_id + 1 if sel_id else 1
        return p_id
    
    #입력한 구분(sep)과 같은 구분을 SEPARATION 테이블에서 검색해서 sepno(구분ID)를 뽑아와서 get_sepno에 저장
    def get_sepno(self, sep_name):
        sql = f"select sepno from separation where sep = '{sep_name}'"
        get_sepno = self.sel_one(sql)

        if get_sepno:
            # get_sepno의 값이 있을 경우 get_sepno를 리턴
            get_sepno = get_sepno[0]
            return get_sepno

        else:
            """
            get_sepno의 값이 없을 경우 sepno(구분)의 max를 검색한다음 
            sepno가 하나도 없으면 1부터 시작하고 아니면 max sepno에서 +1해서 저장
            그리고 새로 추가된 sep(구분)과 sepno(구분ID)를 insert해서 구분 테이블에 저장
            """
            sql_1 = "select max(sepno) from SEPARATION"
            max_sep = self.sel_one(sql_1)[0]
            get_sepno = max_sep + 1 if max_sep else 1

            sql_2 = "insert into SEPARATION values(:1, :2)"
            data = (get_sepno, sep_name)
            self.dml(sql_2, data)
            return get_sepno

    # 생성한 DTO에 입력한 값들을 담아와서 데이터베이스에 삽입함
    def insert_db(self, DTO):
        sql = "insert into PHONEBOOK values(:1, :2, :3, :4, :5)"
        p_id = DTO.get_p_id()
        pname = DTO.get_pname()
        telnum = DTO.get_telnum()
        email = DTO.get_email()
        sepno = DTO.get_sepno()
        data = (p_id, pname, telnum, email, sepno)
        self.dml(sql, data)

    """
    PHONEBOOK에 저장된 id(pk)와 pname(이름), telnum(연락처), email(이메일), 
    그리고 SEPARATION(구분테이블)에 있는 sep(구분)을 검색해서 모두 all_list에 저장
    """
    def output(self):
        sql = "select a.p_id, a.pname, a.telnum, a.email, b.sep " \
              "from PHONEBOOK a, SEPARATION b " \
              " where a.sepno  = b.sepno"
        
        all_list = self.sel_all(sql)
        return all_list

    """
    입력받은 수정할 회원 이름과 같은 PHONEBOOK에 저장된 id(pk)와 pname(이름), telnum(연락처), email(이메일), 
    그리고 SEPARATION(구분테이블)에 있는 sep(구분)을 검색해서 모두 mod_data에 저장
    그리고 mod_data를 리스트 내포를 써서 Domain에 저장함. 그리고 그 Domain은 mod_list에 저장
    """
    def search_modify_list(self, name):
        sql = f"select a.p_id, a.pname, a.telnum, a.email, b.sep " \
                f"  from PHONEBOOK a, SEPARATION b " \
                f" where a.sepno = b.sepno " \
                f"   AND pname = '{name}'"

        mod_data = self.sel_all(sql)
        mod_list = [Domain(row[0], row[1], row[2], row[3], row[4])
                    for row in mod_data]
        return mod_list

    # 생성한 DTO에 입력한 값들을 담아와서 데이터베이스에 업데이트함
    def update_db(self, DTO):
        p_id = DTO.get_p_id()
        pname = DTO.get_pname()
        telnum = DTO.get_telnum()
        email = DTO.get_email()
        sepno = DTO.get_sepno()
        sql = f"update PHONEBOOK set pname = '{pname}', " \
              f"telnum = '{telnum}', email = '{email}', " \
              f" sepno = '{sepno}' where  p_id = '{p_id}'"
        self.dml_one(sql)

    """
    입력받은 삭제할 회원 이름과 같은 PHONEBOOK에 저장된 id와 pname(이름), telnum(연락처), email(이메일), 
    그리고 SEPARATION(구분테이블)에 있는 sep(구분)을 검색해서 모두 del_data에 저장
    그리고 del_data를 리스트 내포를 써서 Domain에 저장함. 그리고 그 Domain은 del_list에 저장
    """
    def search_delete_list(self, name):
        sql = f"select a.p_id, a.pname, a.telnum, a.email, b.sep " \
              f"  from PHONEBOOK a, SEPARATION b " \
              f" where a.sepno = b.sepno AND pname = '{name}'"
        del_data = self.sel_all(sql)
        del_list = [Domain(row[0], row[1], row[2], row[3], row[4])
                    for row in del_data]
        return del_list

    # 생성한 DTO에서 p_id를 받아와서 p_id(PK)와 같은 p_id를 가지고 있는 데이터를 PHONEBOOK에서 삭제함
    def delete_db(self, DTO):
        p_id = DTO.get_p_id()
        sql = f"delete from PHONEBOOK where p_id = '{p_id}'"
        self.dml_one(sql)
    
    # SEPARATION(구분) 테이블을 검색해서 PHONEBOOK에서 참조하고 있지 않은 구분들을 전체 삭제
    def sep_delete_all(self):
        sql = "delete from SEPARATION " \
              "where sepno in (select b.sepno " \
                               "from PHONEBOOK a, SEPARATION b " \
                               "where a.sepno(+) = b.sepno " \
                               "group by b.sepno " \
                               "having count(a.sepno) = 0)"
        self.dml_one(sql)

```