# contact_dto.py

```python
"""연락처 프로그램에서 사용할 데이터 전송 단위인
DTO(domain transfer object)를 정의한 모듈
"""


class ContactDTO(object):
    """연락처 프로그램에서 사용할 데이터 전송 단위인
    DTO를 구현한 클래스
    
    contno: 연락처 id
    name: 이름
    phoneno: 전화번호
    email: 이메일
    group: 구분 이름
    """

    def __init__(self, no: int = 0, nm: str = "",
                 pn: str = "", em: str = "", grp=""):
        self._contno = no
        self._name = nm
        self._phoneno = pn
        self._email = em
        self._group = grp

    def __str__(self):
        return "변수 이름 설명\n" \
               "contno: 연락처 id, name: 이름, phoneno: 전화번호, " \
               "email: 이메일, group: 구분 이름"

    @property
    def contno(self) -> int:
        return self._contno

    @contno.setter
    def contno(self, no: int):
        self._contno = no

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, nm: str):
        self._name = nm

    @property
    def phoneno(self) -> str:
        return self._phoneno

    @phoneno.setter
    def phoneno(self, pn: str):
        self._phoneno = pn

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, em: str):
        self._email = em

    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, grp):
        self._group = grp


```