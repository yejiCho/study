```python

# 도움 주신 분 Jin_cheon


class DTO:
    def __init__(self, id=0, name="", phno="", email="", group=""):
        self._id = id
        self._name = name
        self._phno = phno
        self._email = email
        self._group = group

    # id
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    # name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    # phone_number
    @property
    def phno(self):
        return self._phno

    @phno.setter
    def phno(self, phno):
        self._phno = phno

    # email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    # group
    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, group):
        self._group = group
```