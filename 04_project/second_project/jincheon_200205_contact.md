# contact.py

```python
from error import get_integer
from error import get_name
from error import get_phone_number
from error import get_classification
from error import InputNumberError
from error import InputNameError
from error import InputPhoneNumberError
from error import InputClassificationError
"""연락처 프로그램 처리를 위한
관련 함수, 클래스를 정의한 모듈
"""


def get_menu():
    """메뉴를 출력하고 메뉴번호 입력받아 리턴"""
    print("""
    ==============================
     다음 메뉴 중 하나를 선택하세요.
    ==============================
    1. 연락처 추가
    2. 연락처 목록 보기
    3. 연락처 정보 수정하기
    4. 연락처 삭제
    5. 종료
    메뉴 번호 입력>>""", end=' ')
    try:
        menu_num = get_integer(1, 6)
    except InputNumberError as e:
        print(e)
        return 0

    return menu_num


def input_one_contact() -> dict:
    """올바른 이름, 전화번호, 구분을 입력받아
    딕셔너리에 저장 후 리턴

    one_contact: dict -- 한명의 연락처
        key: 'nm', value: 이름값
        key: 'phoneno', value: 전화번호값
        key 'clfc', value: 구분값
    """
    while 1:
        try:
            name = get_name()
            break
        except InputNameError as e:
            print(e)

    while 1:
        try:
            phone_number = get_phone_number()
            break
        except InputPhoneNumberError as e:
            print(e)

    while 1:
        try:
            classification = get_classification()
            break
        except InputClassificationError as e:
            print(e)

    one_contact = {
        'nm': name,
        'phoneno': phone_number,
        'clfc': classification
    }
    return one_contact


class Contact(object):
    """연락처 저장 및 처리를 하는 클래스
    멤버 변수:
    _all_contact -- 모든 연락처를 가지고 있는 딕셔너리
        key: 전화번호, value: 한명의 연락처 딕셔너리
    """
    _all_contact: dict

    def __init__(self):
        """_all_contact 초기화"""
        self._all_contact = dict()

    def set_all_contact(self, contact: dict):
        """_all_contact에 입력값 저장"""
        self._all_contact = contact

    def get_all_contact(self) -> dict:
        """_all_contact를 불러오는 메소드"""
        return self._all_contact

    def add_contact(self, contact: dict) -> bool:
        """_all_contact에 입력받은 한명의 연락처 추가
        추가 성공시 True 리턴,
        실패시 False 리턴(중복된 전화번호 존재)
        """
        if contact.get('phoneno') in self._all_contact:
            # 중복된 전화번호 존재했을 경우
            overlap = self._all_contact.get(contact.get('phoneno'))
            print('다음의 중복된 연락처가 존재합니다.')
            print(f"이름: {overlap['nm']}, "
                  f"전화번호: {overlap['phoneno']}, "
                  f"구분: {overlap['clfc']}")
            return False
        else:
            self._all_contact[contact['phoneno']] = contact

        return True

    def print_all_contact(self):
        """_all_contact에 저장된 모든 연락처를 화면에 출력"""
        print(f'총 {len(self._all_contact)}명의 연락처가 저장되어 있습니다.')

        for contact in self._all_contact.values():
            print(f"이름: {contact['nm']}, "
                  f"전화번호: {contact['phoneno']}, "
                  f"구분: {contact['clfc']}")

    def _modify(self, key: str) -> bool:
        """연락처 수정 관련 메소드(클래스 내부에서만 사용)"""
        print("수정할 정보를 입력하세요.")
        input_contact = input_one_contact()

        one_contact = self._all_contact[key]

        if key == input_contact['phoneno']:
            # 전화번호를 변경 안했을 경우
            one_contact['nm'] = input_contact['nm']
            one_contact['clfc'] = input_contact['clfc']
            print("연락처 수정이 완료되었습니다.")
        else:
            # 전화번호를 변경 했을 경우
            if self.add_contact(input_contact):
                del self._all_contact[key]
                print(f"연락처 수정이 완료되었습니다.")
            else:
                print(f"연락처 수정을 실패했습니다.\n")
                return False

        return True

    def _delete(self, key: str):
        """연락처 삭제 관련 메소드(클래스 내부에서만 사용)"""
        del self._all_contact[key]
        print("연락처 삭제가 완료되었습니다.")

    def edit_contact(self, mode: str):
        """이름을 입력받아 해당 연락처 정보 편집
        키워드 인수:
        mode:
            "수정" -- 연락처 수정
            "삭제" -- 연락처 삭제
        """
        print(f"{mode}할 연락처의 이름을 입력하세요.")
        while 1:
            try:
                name = get_name()
                break
            except InputNameError as e:
                print(e)

        # 이름이 같은 연락처의 키값을 리스트에 저장
        match_keys = [
            key for key, value
            in self._all_contact.items()
            if value['nm'] == name
        ]

        if match_keys:
            # 입력값과 중복된 연락처 존재할 경우
            while 1:
                print(f"\n총 {len(match_keys)}개의 목록이 검색되었습니다.")

                for i, key in enumerate(match_keys):
                    # 입력값과 중복된 연락처들 출력
                    contact = self._all_contact.get(key)
                    print(f"{i+1}. 이름: {contact['nm']}, "
                          f"전화번호: {contact['phoneno']}, "
                          f"구분: {contact['clfc']}")

                print(f"{mode}할 번호 입력(0: 종료)>>", end=' ')
                try:
                    num = get_integer(0, len(match_keys)+1)
                except InputNumberError as e:
                    print(e)
                    continue

                if num:
                    if mode == "수정":
                        if not self._modify(match_keys[num-1]):
                            # 연락처 수정을 실패했을 경우
                            continue
                    elif mode == "삭제":
                        self._delete(match_keys[num-1])
                    break
                else:
                    # 종료(0 입력)
                    break
        else:
            # 입력값과 중복된 연락처가 없을 경우
            print("해당하는 연락처 정보가 없습니다.\n")

```