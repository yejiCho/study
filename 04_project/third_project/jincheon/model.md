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

    @staticmethod
    def _exec_dml(sql: str, data: tuple = tuple()):
        # DB에 연동하여 dml(insert, update, delete)을 실행
        conn = cxo.connect('contact_user/1234@localhost:1521/xe')
        cursor = conn.cursor()
        cursor.execute(sql, data)

        cursor.close()
        conn.commit()
        conn.close()

    @staticmethod
    def _exec_selectone(sql: str) -> tuple:
        # DB에 연동하여 한 row를 가져오는 select sql 실행
        conn = cxo.connect('contact_user/1234@localhost:1521/xe')
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()

        cursor.close()
        conn.close()

        return data

    @staticmethod
    def _exec_selectall(sql: str) -> list:
        # DB에 연동하여 모든 row를 가져오는 select sql 실행
        conn = cxo.connect('contact_user/1234@localhost:1521/xe')
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return data


```