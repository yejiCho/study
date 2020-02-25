```python
# Model

import cx_Oracle
from Domain import Domain


class Model:
#DB연동 메소드
    def exec_one(self, sql):
        """
        :param sql: db 연동 sql 문
        :return: 1개 row 만 가져와 return
        """
        conn = cx_Oracle.connect("py/1234@localhost:1521/xe")
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()
        cursor.close()
        conn.close()
        return data

    def exec_all(self, sql):
        """
        :param sql: db 연동 sql 문
        :return: 전체 row 를 가져와 저장
        """
        conn = cx_Oracle.connect("py/1234@localhost:1521/xe")
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    def exec_insert(self, sql, data):
        """
        회원추가 시에 사용할 db 연동 메소드
        :param sql: db 연동 sql 문
        :param data: value 값 담고있는 변수
        :return: 해당하는 db 데이터들
        """
        conn = cx_Oracle.connect("py/1234@localhost:1521/xe")
        cursor = conn.cursor()
        cursor.execute(sql, data)
        cursor.close()
        conn.commit()
        conn.close()

    def exec_modify_delete(self, sql):
        """
        회원삭제 시에 사용할 db 연동 메소드
        :param sql: db 연동 sql 문
        """
        conn = cx_Oracle.connect("py/1234@localhost:1521/xe")
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()

    def division_id_create(self, division_input):
        """
        한글로 입력받은 '구분'을 번호형식(PK)으로 바꿔줄 메소드
        :param division_input: 사용자에게 입력받은 한글로 된 '구분'
        :return: 입력받은 한글 '구분'과 매칭되는 구분 id 'div_id'
        """
        sql_1 = f"select div_id from divisions where division = '{division_input}'"
        input_division = self.exec_one(sql_1)
        if input_division:
            # 가져온 input_division (튜플)이 있으면 튜플에서 꺼내 return
            division_id = input_division[0]
            return division_id
        else:
            # 가져온 input_division(튜플)이 비어있다면 구분테이블의 id의 최대값을 가져오는 sql 문 사용해
            # Max 값이 0이 아니면 +1 해서 0이면 1로 div_id_insert 변수에 저장
            sql_1 = "select max(div_id) from divisions"
            div_id_max = self.exec_one(sql_1)[0]
            div_id_insert = div_id_max + 1 if div_id_max else 1

            # insert sql 문 사용해 생성한 구분번호와 입력받은 구분이름 insert 생성한 구분번호를 return
            sql_2 = "insert into divisions values(:1, :2)"
            insert_data = (div_id_insert, division_input)
            self.exec_insert(sql_2, insert_data)
            division_id = div_id_insert
            return division_id

    def contact_id_create(self):
        """
        연락처 테이블의 id 최대값을 가져오는 sql 문 연락처 테이블에 들어갈 id 생성 메소드
        :return: Max 값이 0이 아니면 +1 해서 0이면 1로 id 를 생성해 return
        """
        sql_3 = "select max(id) from contact"
        id_max = self.exec_one(sql_3)[0]
        id = id_max+1 if id_max else 1
        return id

    def insert_db(self, do):
        """
        db에 insert 문 사용해 데이터를 추가시키는 메소드
        :param do: 데이터를 Domain Object 로 담고있는 변수
        """
        sql_4 = "insert into contact values(:1, :2, :3, :4, :5)"
        id = do.get_id()
        name = do.get_name()
        phone = do.get_phone()
        email = do.get_email()
        division = do.get_division()

        cont = (id, name, phone, email, division)
        self.exec_insert(sql_4, cont)

    def show(self):
        """
        db에 저장되어 있는 sql 문에 해당하는 데이터를 전부 가져와 Domain Object 로 묶어 반환하는 메소드
        :return: Domain Object 를 리스트로 담고 있는 all_list
        """
        sql = 'select a.id, a.names, a.phone, a.email, b.division ' \
              'from contact a, divisions b ' \
              'where a.div_id = b.div_id'
        all = self.exec_all(sql)
        all_list = [Domain(rows[0], rows[1], rows[2], rows[3], rows[4]) for rows in all]
        return all_list

    def object_list_disassemble(self, object_list):
        """
        Domain object 를 담고있는 리스트 해체기
        :param object_list: Domain Object 를 리스트로 담고 있는 object_list
        :return:리스트에서 오브젝트를 추출해 getter 를 이용해 요소를 추출하고 튜플로 묶은 후 각각을 리스트에 저장하여 return
        """
        #
        inputname_list = [
                          (inputname_object.get_id(), inputname_object.get_name(), inputname_object.get_phone(),
                           inputname_object.get_email(), inputname_object.get_division())
                           for inputname_object in object_list
                          ]
        return inputname_list

    def search_inputname_matching(self, inputname):
        """
        검색할 회원의 이름을 입력받아 매칭되는 데이터를 Domain Object 에 담아 리스트로 반환
        :param inputname: 회원 검색 시 입력받은 회원이름
        :return: 입력받은 이름과 매칭되는 데이터를 Domain Object 로 묶어 리스트에 저장한 inputname_objectlist
        """
        sql = "select a.id, a.names, a.phone, a.email, b.division " \
              "from contact a, divisions b " \
              f"where a.div_id = b.div_id and a.names = '{inputname}'"
        inputname_list = self.exec_all(sql)
        inputname_objectlist=[
                              Domain(
                                     inputname_rows[0], inputname_rows[1],
                                     inputname_rows[2], inputname_rows[3], inputname_rows[4]
                                     )
                              for inputname_rows in inputname_list
                              ]
        return inputname_objectlist

    def modify_run(self, do):
        """
        회원 수정 시 수정할 정보를 담고있는 Domain Object 인 do를 입력받아 저장된 요소들을 db 에 update 하는 메소드
        :param do: 수정할 정보를 담고있는 Domain Object do
        """
        update_id = do.get_id()
        name = do.get_name()
        phone = do.get_phone()
        email = do.get_email()
        division_id = do.get_division()

        sql_1 = f"update contact " \
                f"set names = '{name}', phone = '{phone}', email = '{email}', div_id = '{division_id}' " \
                f"where id = {update_id}"
        self.exec_modify_delete(sql_1)

    def delete_run(self, delete_id):
        """
        회원 삭제 시  삭제할 id를 입력받아 db 에서 삭제하는 메소드
        :param delete_id: db 에서 삭제할 row 의 id
        """
        sql_1 = f"delete from contact where id = {delete_id}"
        self.exec_modify_delete(sql_1)

    def delete_exit(self):
        """
        프로그램 종료 시 구분테이블에서 연락처테이블과 매칭되지 않는 구분 id와 구분이름 삭제 메소드
        """
        sql = "delete " \
              "from divisions " \
              "where div_id in" \
                             "(select div_id " \
                                "from (select nvl(a.div_id,0)as ndiv_id, b.div_id , b.division " \
                                        "from contact a , divisions b " \
                                       "where a.div_id(+) = b.div_id ) " \
                               "where ndiv_id = 0)"
        self.exec_modify_delete(sql)
```