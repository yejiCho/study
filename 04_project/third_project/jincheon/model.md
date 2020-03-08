# model.py

```python
"""DB연동 모델을 위한
추상화 클래스를 정의한 모듈
"""
from abc import *

import cx_Oracle as cxo


class ModelDB(metaclass=ABCMeta):
    """DB 모델 추상화 클래스
    
    기본기능:
    insert_data(): db로 데이터 삽입
    select_all_data(): db에 저장된 모든 데이터 추출
    update_data(): db에 데이터 수정
    delete_data(): db에 데이터 삭제

    _exec_dml(): dml(insert, update, delete) sql 실행
    _exec_selectone(): 한 row 가져오는 sql 실행
    _exec_selectall(): 모든 row 가져오는 sql 실행
    """
    def __init__(self):
        self._user = ""
        self._passwd = ""
        self._conn = ""

    @abstractmethod
    def insert_data(self, dto):
        """데이터 추가 구현"""
        pass

    @abstractmethod
    def select_all_data(self):
        """전체 데이터 조회 구현"""
        pass

    @abstractmethod
    def update_data(self, dto):
        """데이터 수정 구현"""
        pass

    @abstractmethod
    def delete_data(self, dto):
        """데이터 삭제 구현"""
        pass

    def db_login(self):
        """db 연결 검사
        연결됐을 경우 빈문자열 리턴, 연결 안됐을 경우 메시지 리턴

        :return: 연결 검사 메시지
        """
        result = ""
        try:
            conn = cxo.connect(self._user, self._passwd, self._conn)
            conn.close()
        except cxo.DatabaseError:
            result = "유효하지 않은 id와 비밀번호입니다."

        return result

    def _exec_dml(self, sql: str, data: tuple = tuple()):
        """DB에 연동하여 dml(insert, update, delete)을 실행
        
        :param sql: 실행할 sql문
        :param data: sql문에 필요한 데이터(default tuple())
        """
        conn = cxo.connect(self._user, self._passwd, self._conn)
        cursor = conn.cursor()
        cursor.execute(sql, data)

        cursor.close()
        conn.commit()
        conn.close()

    def _exec_selectone(self, sql: str) -> tuple:
        """DB에 연동하여 한 row를 가져오는 select sql 실행
        
        :param sql: 실행할 sql문
        """
        conn = cxo.connect(self._user, self._passwd, self._conn)
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()

        cursor.close()
        conn.close()

        return data

    def _exec_selectall(self, sql: str) -> list:
        """DB에 연동하여 모든 row를 가져오는 select sql 실행

        :param sql: 실행할 sql문
        """
        conn = cxo.connect(self._user, self._passwd, self._conn)
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return data


```