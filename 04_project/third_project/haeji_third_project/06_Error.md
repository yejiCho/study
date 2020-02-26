```python

import re

# 이메일 검사용 정규표현식
def email_check(email):
    p = re.compile(r'\w+[@]\w+[.]\w+$')
    m = p.match(email)
    if not m:
        raise EmailError()

# 연락처 검사용 정규표현식
def telnum_check(telnum):
    p = re.compile(r'(^0\d{1,2})\D?(\d{3,4})\D?(\d{4})$')
    m = p.match(telnum)
    if m:
        return m.group(1) + m.group(2) + m.group(3)
    else:
        raise TelnumError()

# 이름 체크 에러
def name_check(pname):
    if not pname:
        raise NameError()

# 구분 체크 에러
def sep_name_check(sep_name):
    if not sep_name:
        raise SepNameError()

# 이메일 에러 출력 클래스
class EmailError(Exception):
    def __str__(self):
        return "올바른 이메일 형식이 아닙니다."

# 연락처 에러 출력 클래스
class TelnumError(Exception):
    def __str__(self):
        return "올바른 연락처 형식이 아닙니다."

# 구분 체크 에러 출력 클래스
class SepNameError(Exception):
    def __str__(self):
        return "구분을 입력해주세요"
    
# 이름 체크 에러 출력 클래스
class NameError(Exception):
    def __str__(self):
        return "이름을 입력해주세요"


```