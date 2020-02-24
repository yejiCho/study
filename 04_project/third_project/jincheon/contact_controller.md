# contact_controller.py

```python
"""연락처 프로그램의 컨트롤러를 구현한 클래스"""
from contact_dto import ContactDTO

from contact_view import ContactView

from contact_model import ContactModel

from controller import Controller

import contact_error as e


class ContactController(Controller):
    """controller 모듈의 Controller 클래스를 상속 받아
    연락처 프로그램에 적합한 컨트롤러를 구현한 클래스
    """

    def __init__(self):
        """컨트롤러에서는 뷰와 모델을 계속 호출해야하기 때문에
        컨트롤러 오브젝트를 생성하면서 뷰와 모델 오브젝트를 함께 생성
        """
        self._view = ContactView()
        self._model = ContactModel()

    def __str__(self):
        return "run() 메소드를 호출하여 실행하세요."

    def run(self):
        """연락처 프로그램 실행 메소드

        1: 연락처 추가 -- add()
        2: 연락처 검색 -- search()
        3: 연락처 수정 -- modify()
        4: 연락처 삭제 -- delete()
        5: 종료 -- quit()
        """
        while True:
            menu_num = self._get_valid_integer('mn', 1, 6)
            if menu_num == 1:
                self.add()
            elif menu_num == 2:
                self.search()
            elif menu_num == 3:
                self.modify()
            elif menu_num == 4:
                self.delete()
            elif menu_num == 5:
                self.quit()
                break

    def add(self):
        """연락처 추가"""
        dto = ContactDTO()
        dto.name = self._get_valid_name()
        dto.phoneno = self._get_valid_phoneno()
        dto.email = self._get_valid_email()
        dto.group = self._get_valid_group()

        self._model.insert_data(dto)
        self._view.print_result("추가")

    def search(self):
        """연락처 검색"""
        cond_num = self._get_valid_integer('con', 0, 6)
        if not cond_num:
            # 0을 입력 받으면 메소드 종료
            return

        dto_list = self._condition_search(cond_num)
        if not dto_list:
            # 리스트에 값이 없을 경우 메시지 출력 후 메소드 종료
            self._view.print_empty()
            return

        self._view.print_cont_length(len(dto_list))
        for i, dto in enumerate(dto_list):
            self._view.print_contact(i+1, dto)

    def modify(self):
        """연락처 수정"""
        cond_num = self._get_valid_integer('con', 0, 6)
        if not cond_num:
            # 0을 입력받으면 메소드 종료
            return

        dto_list = self._condition_search(cond_num)
        if not dto_list:
            # 리스트에 값이 없을 경우 메시지 출력 후 메소드 종료
            self._view.print_empty()
            return

        self._view.print_cont_length(len(dto_list))
        for i, dto in enumerate(dto_list):
            self._view.print_contact(i+1, dto)

        mod_num = self._get_valid_integer('mod', 0, len(dto_list)+1)
        if not mod_num:
            # 0을 입력받으면 메소드 종료
            return

        dto = dto_list[mod_num-1]
        dto.name = self._get_valid_name()
        dto.phoneno = self._get_valid_phoneno()
        dto.email = self._get_valid_email()
        dto.group = self._get_valid_group()

        self._model.update_data(dto)
        self._view.print_result("수정")

    def delete(self):
        """연락처 삭제"""
        cond_num = self._get_valid_integer('con', 0, 6)
        if not cond_num:
            # 0을 입력받으면 메소드 종료
            return

        dto_list = self._condition_search(cond_num)
        if not dto_list:
            # 리스트에 값이 없을 경우 메시지 출력 후 메소드 종료
            self._view.print_empty()
            return

        self._view.print_cont_length(len(dto_list))
        for i, dto in enumerate(dto_list):
            self._view.print_contact(i+1, dto)

        del_num = self._get_valid_integer('del', 0, len(dto_list)+1)
        if not del_num:
            # 0을 입력받으면 메소드 종료
            return

        dto = dto_list[del_num-1]
        self._model.delete_data(dto)
        self._view.print_result("삭제")

    def quit(self):
        """연락처 종료
        구분에 속한 연락처가 존재하지 않는 구분들을 삭제하고
        메시지를 출력한다.
        """
        self._model.delete_unused_group()
        self._view.print_result("종료")

    def _condition_search(self, cond_num: int) -> list:
        # 조건 검색 메소드(해당 dto 리턴)
        # 1: 전체 연락처 검색, 2: 이름 검색, 3: 전화번호 검색
        # 4: 이메일 검색, 5: 구분 검색
        dto_list = list()
        if cond_num == 1:
            dto_list = self._model.select_all_data()
        elif cond_num == 2:
            name = self._get_valid_name()
            dto_list = self._model.select_name_match_data(name)
        elif cond_num == 3:
            phno = self._get_valid_phoneno()
            dto_list = self._model.select_phoneno_match_data(phno)
        elif cond_num == 4:
            email = self._get_valid_email()
            dto_list = self._model.select_email_match_data(email)
        elif cond_num == 5:
            grp = self._get_valid_group()
            dto_list = self._model.select_group_match_data(grp)

        return dto_list

    def _get_valid_integer(self, mode: str, start: int, stop: int) -> int:
        # 올바른 숫자를 입력받아 리턴
        while 1:
            num = ""
            if mode == 'mn':
                num = self._view.get_menu()
            elif mode == 'con':
                num = self._view.get_condition_search()
            elif mode == 'mod':
                num = self._view.input_seq("수정")
            elif mode == 'del':
                num = self._view.input_seq("삭제")

            try:
                result = e.valid_integer(num, start, stop)
                return result
            except e.InputNumberError as ine:
                self._view.print_error(ine)

    def _get_valid_name(self) -> str:
        # 올바른 이름을 입력받아 리턴
        while 1:
            name = self._view.input_name()
            try:
                e.valid_name(name)
                return name
            except e.InputNameError as ine:
                self._view.print_error(ine)

    def _get_valid_phoneno(self) -> str:
        # 올바른 전화번호를 입력받아 리턴
        while 1:
            phno = self._view.input_phoneno()
            try:
                result = e.valid_phoneno(phno)
                return result
            except e.InputPhoneNumberError as ipe:
                self._view.print_error(ipe)

    def _get_valid_email(self) -> str:
        # 올바른 이메일을 입력받아 리턴
        while 1:
            email = self._view.input_email()
            try:
                e.valid_email(email)
                return email
            except e.InputEmailError as ime:
                self._view.print_error(ime)

    def _get_valid_group(self) -> str:
        # 올바른 구분을 입력받아 리턴
        while 1:
            grp = self._view.input_group()
            try:
                e.valid_group(grp)
                return grp
            except e.InputGroupError as ige:
                self._view.print_error(ige)


```