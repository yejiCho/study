```python

#Domain

class Domain:
    # 생성자 선언 및 초기화
    def __init__(self, p_id=0, pname="", telnum="", email="", sepno=""):

        self._p_id = p_id
        self._pname = pname
        self._telnum = telnum
        self._email = email
        self._sepno = sepno

    def get_p_id(self):
        return self._p_id

    def set_p_id(self, p_id):
        self._p_id = p_id

    def get_pname(self):
        return self._pname

    def set_pname(self, pname):
        self._pname = pname

    def get_telnum(self):
        return self._telnum

    def set_telnum(self, telnum):
        self._telnum = telnum

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_sepno(self):
        return self._sepno

    def set_sep_no(self, sepno):
        self._sepno = sepno


```