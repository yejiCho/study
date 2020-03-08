```python

import re

# 도움 주신 분 Jin_cheon
# 예외처리와 정규식을 동시에!


class NameError(Exception):
    def __str__(self):
        return "올바른 이름 형식에 맞춰 입력해주세요. (한글 혹은 영어로 50자 이내)"


class PhoneNumberError(Exception):
    def __str__(self):
        return "올바른 전화 번호 형식에 맞춰 입력해주세요.(0으로 시작하는 특수문자를 제외한 8~10자리의 숫자)"


class EmailError(Exception):
    def __str__(self):
        return "올바른 Email 형식에 맞춰 입력해주세요."


class DivisionError(Exception):
    def __str__(self):
        return "관계를 입력해주세요.(30자 이내의 문자)"


def name_catch(name):
    if not name or len(name) > 50:
        raise NameError()


def pn_catch(phno):
    p = re.compile(r'^0\d{8,10}$')
    m = p.match(phno)
    if not m:
        raise PhoneNumberError()


def dv_catch(group):
    if not group or len(group) > 50:
        raise DivisionError()


def em_catch(email):
    p = re.compile(r'[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}')
    m = p.match(email)
    if not m or len(email) > 50:
        raise EmailError()
```