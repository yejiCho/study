```python
# Domain


class Domain:  # 도메인 오브젝트 클래스
    def __init__(self, id=0, name="", phone="", email="", division=""):
        """
        생성자 지정 및 초기화
        id, name, phone, email, division 을 모두
        입력 시 바로 self 로 삽입하게끔 형식지정
        """
        self._id = id
        self._name = name
        self._phone = phone
        self._email = email
        self._division = division

    # 요소 각각의 getter, setter 생성 및 private 처리
    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_phone(self):
        return self._phone

    def set_phone(self, phone):
        self._phone = phone

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_division(self):
        return self._division

    def set_division(self, division):
        self._division = division
```