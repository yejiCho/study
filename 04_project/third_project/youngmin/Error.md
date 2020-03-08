```python
# Error

import re


def not_name(name):
    """
    이름에 공백 입력시 에러 발생
    :param name: 사용자가 입력한 이름
    :return: 에러발생
    """
    if not name:
        raise NameError()
    if len(name) > 50:
        raise NameError()

def not_reg_phone(phone):
    """
    연락처 정규식 지정 및 예외처리
    :param phone: 사용자가 입력한 연락처
    :return: -를 포함해서 입력받았을 경우 -를 제외한 연락처 or 에러발생
    """
    P = re.compile(r'(\d{2,3})\D?(\d{3,4})\D?(\d{4})')  # \D?= 숫자가 아닌 것 0개or1개, 숫자만 그룹핑
    match_P = P.match(phone)
    if match_P:
        return match_P.group(1)+match_P.group(2)+match_P.group(3)  # -를 포함해서 입력받았을 경우 -를 제외하고 return
    else:
        raise PhoneRegError()

def not_reg_email(email):
    """
    이메일 정규식 지정 및 예외처리
    :param email: 사용자가 입력한 이메일
    :return: 에러발생
    """
    E = re.compile(r'\w+[@]\w+[.]\w+', re.IGNORECASE)  # 틀 만들기(옵션 : 대소문자 구분 안함)
    if not E.match(email):
        raise EmailError()
    if len(email) > 50:
        raise EmailError()

def not_division(division_input):
    """
    구분에 공백 입력시 에러 발생
    :param division_input: 사용자가 입력한 구분
    :return: 에러발생
    """
    if not division_input:
        raise DivisionError()
    if len(division_input) > 50:
        raise DivisionError()

def wrong_number():
    """
    :return: 범위 밖의 번호 입력시에 출력문구
    """
    print("해당하는 번호만 입력하여 주십시오.")

def wrong_name():
    """
    :return: 회원검색 시에 저장된 회원 외의 이름을 입력시 출력문구
    """
    print("입력하신 이름의 회원이 없습니다.")


# 에러발생 시 exception 할 출력문구 문자열을 담은 클래스들
class NameError(Exception):
    def __str__(self):
        return "\n 이름을 입력하여 주십시오.(50자 이내)\n"

class PhoneRegError(Exception):
    def __str__(self):
        return "\n전화번호 형식에 맞게 입력해주십시오.\n" \
               "ex)010-1234-1234\n"

class EmailError(Exception):
    def __str__(self):
        return "\n이메일 형식에 맞게 입력하여 주십시오.(50자 이내)\n" \
               "ex)abcd@email.com\n"

class DivisionError(Exception):
    def __str__(self):
        return "\n구분을 꼭 입력하여 주십시오.(50자 이내)\n"
```