```python

#Controller

from Model import Model
from View import View
from Domain import Domain
import Error

# controller 클래스
class Controller:
    def __init__(self):
        self._view = View()
        self._model = Model()
    
    # 회원 목록 추가 함수
    def insert(self):
        
        self._view.ins_command()
        
        while 1:
            pname = self._view.input_pname()
            try:
                """
                이름을 입력하지 않았는지 검사
                이름을 입력했을 경우 때 while문 벗어남
                """
                Error.name_check(pname)
                break
            except Error.NameError as e:
                self._view.print_e(e)
        while 1:
            telnum = self._view.input_telnum()
            try:
                """
                연락처 에러 정규식 검사함수에 입력한 이름을 넣어서 검사
                에러가 나지 않았을 때 while문 벗어남
                """
                telnum = Error.telnum_check(telnum)
                break
            except Error.TelnumError as e:
                self._view.print_e(e)
        while 1:
            email = self._view.input_email()
            try:
                """
                이메일 에러 정규식 검사함수에 입력한 이름을 넣어서 검사
                에러가 나지 않았을 때 while문 벗어남
                """
                Error.email_check(email)
                break
            except Error.EmailError as e:
                self._view.print_e(e)
        while 1:
            sep_name = self._view.input_sep_name()
            
            try:
                """
                구분을 입력하지 않았는지 검사
                구분을 입력했을 경우 때 while문 벗어남
                """
                Error.sep_name_check(sep_name)
                break
            except Error.SepNameError as e:
                self._view.print_e(e)

        p_id = self._model.select_maxid()
        sepno = self._model.get_sepno(sep_name)

        DTO = Domain(p_id, pname, telnum, email, sepno)
        
        # model의 insert 함수를 써서 데이터베이스에 입력값을 적재
        self._model.insert_db(DTO)

    # 회원 목록 출력 함수
    def allnum(self):
        all_list = self._model.output()
        self._view.view_allnum(all_list)

    # 회원 목록 수정 함수
    def modify(self):

        self._view.modi_command()

        while 1:
            name = self._view.input_pname()
            try:
                """
                이름을 입력하지 않았는지 검사
                이름을 입력했을 경우 때 while문 벗어남
                """
                Error.name_check(name)
                break
            except Error.NameError as e:
                self._view.print_e(e)
        mod_list = self._model.search_modify_list(name)

        if mod_list:
            """
            mod_list의 값이 있을 경우 for문으로 model의 함수를 써서
            mod_list의 index를 저장한 다음 저장된 index와 함께 출력
            """
            self._view.modi_search_command(mod_list)

            for row in mod_list:
                mod_ind = mod_list.index(row)
                self._view.modi_print(mod_ind, row)

            while 1:
                try:
                    """
                    pk에 접근하는데에 필요한 p_id를 찾기위해 사용자가 
                    입력한 수정할 번호에 -1을 해서 mod_list에서 index로 찾고
                    그 값을 mod_domain으로 받음
                    """
                    put_ind = self._view.put_ind()
                    mod_domain = mod_list[put_ind-1]
                    break

                except IndexError:
                    self._view.not_find_num()

                except ValueError:
                    self._view.not_find_num()

            while 1:
                pname = self._view.input_pname()
                try:
                    """
                    이름을 입력하지 않았는지 검사
                    이름을 입력했을 경우 때 while문 벗어남
                    """
                    Error.name_check(pname)
                    break
                except Error.NameError as e:
                    self._view.print_e(e)
            while 1:
                telnum = self._view.input_telnum()
                try:
                    """
                    연락처 에러 정규식 검사함수에 입력한 이름을 넣어서 검사
                    에러가 나지 않았을 때 while문 벗어남
                    """
                    telnum = Error.telnum_check(telnum)
                    break
                except Error.TelnumError as e:
                    self._view.print_e(e)
            while 1:
                email = self._view.input_email()
                try:
                    """
                    이메일 에러 정규식 검사함수에 입력한 이름을 넣어서 검사
                    에러가 나지 않았을 때 while문 벗어남
                    """
                    Error.email_check(email)
                    break
                except Error.EmailError as e:
                    self._view.print_e(e)
            while 1:
                sep_name = self._view.input_sep_name()

                try:
                    """
                    구분을 입력하지 않았는지 검사
                    구분을 입력했을 경우 때 while문 벗어남
                    """
                    Error.sep_name_check(sep_name)
                    break
                except Error.SepNameError as e:
                    self._view.print_e(e)

            # mod_domain에 입력받은 값들을 지정
            mod_domain.set_pname(pname)
            mod_domain.set_telnum(telnum)
            mod_domain.set_email(email)
            
            sepno = self._model.get_sepno(sep_name)
            mod_domain.set_sep_no(sepno)
            
            # model에 있는 update함수를 써서 데이터베이스에 업데이트
            self._model.update_db(mod_domain)
            self._view.modi_complete()

            # model에 있는 함수를 써서 구분 테이블을 검사. 참조된 구분이 없을 경우 구분 삭제
            self._model.sep_delete_all()
        
        # mod_list의 값이 없을경우 아래 문구 출력
        else:
            self._view.not_agree()

    # 회원 목록 삭제 함수
    def delete(self):
        self._view.del_command()
        
        while 1:
            name = self._view.input_pname()
            try:
                """
                이름을 입력하지 않았는지 검사
                이름을 입력했을 경우 때 while문 벗어남
                """
                Error.name_check(name)
                break

            except Error.NameError as e:
                self._view.print_e(e)

        # model의 함수를 써서 del_list라는 리스트로 받아옴
        del_list = self._model.search_delete_list(name)

        if del_list:
            """
            del_list의 값이 있을 경우 for문으로 model의 함수를 써서
            del_list의 index를 저장한 다음 저장된 index와 함께 출력
            """
            self._view.del_search_command(del_list)

            for row in del_list:
                del_ind = del_list.index(row)
                self._view.del_print(del_ind, row)

            while 1:
                try:
                    """
                    pk에 접근하는데에 필요한 p_id를 찾기위해 사용자가 
                    입력한 수정할 번호에 -1을 해서 mod_list에서 index로 찾고
                    그 값을 mod_domain으로 받음
                    """
                    put_ind = self._view.put_ind()
                    del_domain = del_list[put_ind-1]
                    break

                except IndexError:
                    # 사용자가 입력한 번호가 인덱스를 넘어갈 경우 에러발생
                    self._view.not_find_num()

                except ValueError:
                    # 사용자가 아무것도 입력하지 않았을 경우 에러발생
                    self._view.not_find_num()

            # model에 있는 delete함수를 써서 데이터베이스에서 삭제
            self._model.delete_db(del_domain)
            self._view.del_complete()

            # model에 있는 함수를 써서 구분 테이블을 검사. 참조된 구분이 없을 경우 구분 삭제
            self._model.sep_delete_all()

        else:
            # mod_list의 값이 없을경우 아래 문구 출력
            self._view.not_agree()

    def run(self):

        # 연락처 프로그램 실행 무한 루프 while문
        while 1:
            p_menu = self._view.menu()

            if p_menu == '1':
                self.insert()

            elif p_menu == '2':
                self.allnum()

            elif p_menu == '3':
                self.modify()

            elif p_menu == '4':
                self.delete()

            elif p_menu == '5':
                self._view.print_end()
                break

            else:
                self._view.not_range()

# controller 실행
Controller = Controller()
Controller.run()

```