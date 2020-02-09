# error.py

``` python
"""에러 처리를 위한
관련 함수, 클래스를 정의한 모듈
"""


def get_integer(num: str, start: int, stop: int) -> int:
    """범위 내에 올바른 정수값을 입력받아 리턴
    올바른 입력 값이 아닐 경우
    InputNumberError 발생

    키워드 인수:
    num -- 검사할 문자열
    start -- 시작 위치
    stop -- 마지막 위치(해당값 미포함)
    """
    if num.isdigit():
        num = int(num)
        if num not in range(start, stop):
            raise InputNumberError()
    else:
        raise InputNumberError()

    return num


def get_name(name: str) -> str:
    """이름을 입력하지 않았을 경우
    InputNameError 발생
    """
    if not name:
        raise InputNameError()

    return name


def get_phone_number(ph_num: str) -> str:
    """올바른 전화번호값을 입력받아 리턴
    전화번호는 9~11자리 숫자로 구성
    올바른 입력값이 아닐 경우
    InputPhoneNumberError 발생
    """
    if not ph_num.isdigit():
        raise InputPhoneNumberError()
    elif len(ph_num) not in range(9, 12):
        raise InputPhoneNumberError()

    return ph_num


def get_classification(cfc: str) -> str:
    """올바른 구분값을 입력받아 리턴
    1, 가족 입력 -- '가족' 리턴
    2, 친구 입력 -- '친구' 리턴
    3, 회사 입력 -- '회사' 리턴
    4, 기타 입력, 미입력 -- '기타' 리턴
    그외 InputClassificationError 발생
    """
    checks = [('가족', '1'), ('친구', '2'),
              ('회사', '3'), ('기타', '4', '')]
    for value in checks:
        if cfc in value:
            return value[0]

    raise InputClassificationError()


class InputNumberError(Exception):
    """숫자 입력 예외 처리 클래스"""
    def __str__(self):
        return "입력 값이 올바르지 않습니다."


class InputNameError(Exception):
    """이름 입력 예외 처리 클래스"""
    def __str__(self):
        return "이름을 입력하세요."


class InputPhoneNumberError(Exception):
    """전화번호 입력 예외 처리 클래스"""
    def __str__(self):
        return "전화번호를 9~11자리 숫자 형식으로 입력하세요."


class InputClassificationError(Exception):
    """구분 입력 예외 처리 클래스"""
    def __str__(self):
        return "잘못된 구분 입력입니다."


```