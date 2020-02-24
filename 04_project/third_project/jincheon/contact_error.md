# contact_error.py

```python
"""입력값 유효성 검사를 위한
관련 함수, 클래스를 정의한 모듈
"""
import re


def valid_integer(num: str, start: int, stop: int):
    """숫자 유효성 검사
    범위내의 숫자일 경우 int 타입으로 바꿔서 리턴
    올바른 입력값이 아닐 경우 InputNumberError 발생

    :param num: 검사할 문자열
    :param start: 시작 위치
    :param stop: 마지막 위치(해당값 미포함)
    :return: int 타입으로 바꿔서 리턴
    """

    if num.isdigit():
        num = int(num)
        if num not in range(start, stop):
            raise InputNumberError(start, stop)
    else:
        raise InputNumberError(start, stop)

    return num


def valid_name(name: str):
    """이름 유효성 검사
    이름을 입력하지 않았거나 입력 길이가 20자가 넘을 경우
    InputNameError 발생
    
    :param name: 검사할 문자열
    """
    
    if not name or len(name) > 20:
        raise InputNameError()


def valid_phoneno(ph_num: str):
    """전화번호 유효성 검사
    전화번호 형식이 아닐 경우 InputPhoneNumberError 발생
    ex) 01012341234, 010-1234-1234, 02 123 1234
    
    :param ph_num: 검사할 문자열
    :return: 모든 문자를 숫자로 바꿔서 리턴
    """

    p = re.compile(r'(^0\d{1,2})\D?(\d{3,4})\D?(\d{4})$')
    m = p.match(ph_num)
    if m:
        return m.group(1) + m.group(2) + m.group(3)
    else:
        raise InputPhoneNumberError()


def valid_email(email: str):
    """이메일 유효성 검사
    이메일 형식이 아닐 경우 InputEmailError 발생
    입력값이 빈문자열일 수 있음

    :param email: 검사할 문자열
    """
    if email:
        if len(email) <= 20:
            p = re.compile(r'^[a-zA-Z0-9+-_￦.]+[@][a-zA-Z0-9+-_￦]+[.][a-zA-Z]{2,4}$')
            m = p.match(email)
            if not m:
                raise InputEmailError()
        else:
            raise InputEmailError()


def valid_group(cfc: str):
    """구분 유효성 검사
    구분을 입력하지 않았거나 입력 길이가 20자가 넘을 경우
    InputGroupError 발생

    :param cfc: 검사할 문자열
    """
    if not cfc or len(cfc) > 20:
        raise InputGroupError()


class InputNumberError(Exception):
    """숫자 입력 예외 클래스"""
    def __init__(self, start, stop):
        self._start = start
        self._stop = stop

    def __str__(self):
        return f"{self._start}~{self._stop-1} 사이의 숫자를 입력하세요."


class InputNameError(Exception):
    """이름 입력 예외 클래스"""
    def __str__(self):
        return "20자 이하의 이름을 입력하세요."


class InputPhoneNumberError(Exception):
    """전화번호 입력 예외 클래스"""
    def __str__(self):
        return "올바른 전화번호 형식이 아닙니다.\n" \
               "ex) 01012341234, 010-1234-1234, 010 1234 1234"


class InputEmailError(Exception):
    """이메일 입력 예외 클래스"""
    def __str__(self):
        return "올바른 이메일 형식이 아닙니다.\n" \
               "20자 이하의 이메일을 입력하세요.\n" \
               "ex) ggg123@gmail.com, nnn123@naver.com"


class InputGroupError(Exception):
    """구분 입력 예외 처리 클래스"""
    def __str__(self):
        return "20자 이하의 구분을 입력하세요."


```