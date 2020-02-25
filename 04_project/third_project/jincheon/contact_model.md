# contact_model.py

```python
"""연락처 프로그램의 모델을 정의한 모델"""
from contact_dto import ContactDTO

from model import ModelDB


class ContactModel(ModelDB):
    """model 모듈의 ModelDB 클래스를 상속 받아
    연락처 프로그램에 적합한 모델을 구현한 클래스
    """

    def __init__(self, user, passwd):
        super().__init__()
        self._user = user
        self._passwd = passwd
        self._conn = 'localhost:1521/xe'

    def _select_grpno(self, grp: str) -> int:
        # 구분 이름값을 입력받아 구분 번호를 리턴
        sql = f"SELECT grpno" \
              f"  FROM grps" \
              f" WHERE grpnm = '{grp}'"
        grp_tp = self._exec_selectone(sql)
        grpno = grp_tp[0] if grp_tp else 0

        return grpno

    def _insert_group(self, grp: str) -> int:
        # 입력받은 구분을 DB에 추가
        sql = "SELECT NVL(MAX(grpno)+1, 1)" \
              "  FROM grps"
        grpno = self._exec_selectone(sql)[0]

        sql = "INSERT INTO grps " \
              "VALUES(:1,:2)"
        data = (grpno, grp)

        self._exec_dml(sql, data)

        return grpno

    def delete_unused_group(self):
        """grps 테이블에서
        contacts 테이블이 참조하지 않는 row를 모두 삭제
        """
        sql = "DELETE grps" \
              " WHERE grpno IN (" \
              "                SELECT b.grpno" \
              "                  FROM contacts a, grps b" \
              "                 WHERE a.grpno(+) = b.grpno" \
              "                 GROUP BY b.grpno" \
              "                HAVING COUNT(a.grpno) = 0" \
              "               )"

        self._exec_dml(sql)

    def insert_data(self, dto: ContactDTO):
        """입력받은 연락처 dto를 DB 형식으로 바꿔서 DB에 삽입

        :param dto: 입력받은 연락처 dto(id 존재 X)
        """
        # 연락처 id를 구한다
        sql = "SELECT NVL(MAX(contno)+1, 1)" \
              "  FROM contacts"
        contno = self._exec_selectone(sql)[0]
        
        # 구분 id를 구하고 id가 없을 경우 구분을 추가
        grpno = self._select_grpno(dto.group)
        group = grpno if grpno else self._insert_group(dto.group)

        sql = "INSERT INTO contacts " \
              "VALUES(:1,:2,:3,:4,:5)"
        data = (contno, dto.name, dto.phoneno, dto.email, group)

        self._exec_dml(sql, data)

    def update_data(self, dto: ContactDTO):
        """입력받은 dto의 내용을 참조하여 DB에서 id를 찾아 수정

        :param dto: 입력받은 연락처 dto(id 존재 O)
        """
        # 구분 id를 구하고 id가 없을 경우 구분을 추가
        grpno = self._select_grpno(dto.group)
        group = grpno if grpno else self._insert_group(dto.group)

        sql = "UPDATE contacts" \
              "   SET nm=:1, phoneno=:2" \
              "     , email=:3, grpno=:4" \
              " WHERE contno=:5"
        data = (dto.name, dto.phoneno, dto.email, group, dto.contno)

        self._exec_dml(sql, data)

    def delete_data(self, dto: ContactDTO):
        """입력받은 dto의 내용을 참조하여 DB에서 id를 찾아 삭제

        :param dto: 입력받은 연락처 dto(id 존재 O)
        """
        sql = "DELETE FROM contacts" \
              " WHERE contno=:1"
        data = (dto.contno,)

        self._exec_dml(sql, data)

    def select_all_data(self) -> list:
        """contacts 테이블에 저장된 모든 row를 dto 형식으로 바꿔서
        리스트로 저장한 후 리턴
        
        :return: dto 오브젝트가 저장된 리스트
        """
        sql = "SELECT a.contno, a.nm" \
              "     , a.phoneno, a.email" \
              "     , b.grpnm" \
              "  FROM contacts a, grps b" \
              " WHERE a.grpno = b.grpno"
        data = self._exec_selectall(sql)

        dto_list = [
            ContactDTO(v[0], v[1], v[2], v[3], v[4])
            for v in data
        ]

        return dto_list

    def select_name_match_data(self, name: str) -> list:
        """contacts 테이블에 저장된 row 중 입력받은 이름과 같은 row를
        dto 형식으로 바꿔서 리스트로 저장한 후 리턴
        
        :param name: 매칭할 이름
        :return: dto 오브젝트가 저장된 리스트
        """
        sql = f"SELECT a.contno, a.nm" \
              f"     , a.phoneno, a.email" \
              f"     , b.grpnm" \
              f"  FROM contacts a, grps b" \
              f" WHERE a.grpno = b.grpno" \
              f"   AND a.nm = '{name}'"
        data = self._exec_selectall(sql)

        dto_list = [
            ContactDTO(v[0], v[1], v[2], v[3], v[4])
            for v in data
        ]

        return dto_list

    def select_phoneno_match_data(self, phno: str) -> list:
        """contacts 테이블에 저장된 row 중 입력받은 전화번호와 같은 row를
        dto 형식으로 바꿔서 리스트로 저장한 후 리턴
        
        :param phno: 매칭할 전화번호
        :return: dto 오브젝트가 저장된 리스트
        """
        sql = f"SELECT a.contno, a.nm" \
              f"     , a.phoneno, a.email" \
              f"     , b.grpnm" \
              f"  FROM contacts a, grps b" \
              f" WHERE a.grpno = b.grpno" \
              f"   AND a.phoneno = '{phno}'"
        data = self._exec_selectall(sql)

        dto_list = [
            ContactDTO(v[0], v[1], v[2], v[3], v[4])
            for v in data
        ]

        return dto_list

    def select_email_match_data(self, email: str) -> list:
        """contacts 테이블에 저장된 row 중 입력받은 이메일과 같은 row를
        dto 형식으로 바꿔서 리스트로 저장한 후 리턴
        
        :param email: 매칭할 이메일
        :return: dto 오브젝트가 저장된 리스트
        """
        sql = f"SELECT a.contno, a.nm" \
              f"     , a.phoneno, a.email" \
              f"     , b.grpnm" \
              f"  FROM contacts a, grps b" \
              f" WHERE a.grpno = b.grpno" \
              f"   AND a.email = '{email}'"
        data = self._exec_selectall(sql)

        dto_list = [
            ContactDTO(v[0], v[1], v[2], v[3], v[4])
            for v in data
        ]

        return dto_list

    def select_group_match_data(self, grp: str) -> list:
        """contacts 테이블에 저장된 row 중 입력받은 구분과 같은 row를
        dto 형식으로 바꿔서 리스트로 저장한 후 리턴

        :param grp: 매칭할 구분
        :return: dto 오브젝트가 저장된 리스트
        """
        sql = f"SELECT a.contno, a.nm" \
              f"     , a.phoneno, a.email" \
              f"     , b.grpnm" \
              f"  FROM contacts a, grps b" \
              f" WHERE a.grpno = b.grpno" \
              f"   AND b.grpnm = '{grp}'"
        data = self._exec_selectall(sql)

        dto_list = [
            ContactDTO(v[0], v[1], v[2], v[3], v[4])
            for v in data
        ]

        return dto_list




```