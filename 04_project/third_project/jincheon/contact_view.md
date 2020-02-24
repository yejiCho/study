# contact_view.py

```python
"""연락처 프로그램의 뷰를 정의한 모듈"""
from contact_dto import ContactDTO


class ContactView(object):
    """연락처 프로그램에 적합한 뷰를 구현한 클래스"""

    @staticmethod
    def get_menu() -> str:
        """메뉴를 출력하고 메뉴번호 입력받아 리턴"""
        print("""
        ==============================
         다음 메뉴 중 하나를 선택하세요.
        ==============================
        1. 연락처 추가
        2. 연락처 목록 검색
        3. 연락처 정보 수정
        4. 연락처 삭제
        5. 종료""")
        menu_num = input("메뉴 번호 입력>> ").strip()

        return menu_num

    @staticmethod
    def get_condition_search() -> str:
        """조건 검색 메뉴를 출력하고 조건 번호 입력받아 리턴"""
        print("""
        1. 전체 연락처 검색
        2. 이름 검색
        3. 전화번호 검색
        4. 이메일 검색
        5. 구분 검색""")
        cond = input("조건 번호 입력(0: 종료)>> ").strip()

        return cond

    @staticmethod
    def input_name() -> str:
        """이름 입력받아 리턴"""
        return input("이름: ").strip()

    @staticmethod
    def input_phoneno() -> str:
        """전화번호 입력받아 리턴"""
        return input("전화번호: ").strip()

    @staticmethod
    def input_email() -> str:
        """이메일 입력받아 리턴"""
        return input("이메일: ").strip()

    @staticmethod
    def input_group() -> str:
        """구분 입력받아 리턴"""
        return input("구분: ").strip()

    @staticmethod
    def input_seq(mode: str) -> str:
        """번호를 입력받고 리턴
        
        :param mode: 출력 메시지 모드(수정, 삭제)
        """
        return input(f"{mode}할 번호 입력(0: 종료)>> ")

    @staticmethod
    def print_error(error):
        """에러 메시지 출력"""
        print(error)

    @staticmethod
    def print_result(result):
        """결과 메시지 출력"""
        print(f"{result}됐습니다.")

    @staticmethod
    def print_empty():
        """연락처가 비었을 경우 메시지 출력"""
        print("해당하는 연락처가 없습니다.")

    @staticmethod
    def print_contact(i: int, dto: ContactDTO):
        """연락처를 양식에 맞게 출력

        :param i: 순서 번호
        :param dto: 연락처가 저장된 domain object
        """
        print(f"{i}. 이름: {dto.name} "
              f"전화번호: {dto.phoneno} "
              f"이메일: {dto.email} "
              f"구분: {dto.group}")

    @staticmethod
    def print_cont_length(leng: int):
        """길이 메시지 출력"""
        print(f"총 {leng}개의 목록이 검색됐습니다.")

```