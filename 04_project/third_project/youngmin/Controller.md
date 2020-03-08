```python
# Controller

from Model import Model
from View import View
from Domain import Domain
import Error


class Contact:
    def insert(self):
        """
        1. 회원 추가 메소드
        """
        View.insert_head()
        while 1:
            # while 문 사용해 에러가 발생할 경우 다시 입력하게끔 하였다.(에러 발생 안할 시 break)
            try:
                name = View.name_input()
                Error.not_name(name)
                break
            except Error.NameError as e:
                View.print_Error(e)
        while 1:
            try:
                phone = View.phone_input()
                phone = Error.not_reg_phone(phone)  # 정규식에 맞게 연락처 형식 수정
                break
            except Error.PhoneRegError as e:
                View.print_Error(e)
        while 1:
            try:
                email = View.email_input()
                Error.not_reg_email(email)
                break
            except Error.EmailError as e:
                View.print_Error(e)
        while 1:
            try:
                division_input = View.division_input()
                Error.not_division(division_input)
                break
            except Error.DivisionError as e:
                View.print_Error(e)

        division_id = Model.division_id_create(division_input)
        id = Model.contact_id_create()

        do = Domain(id, name, phone, email, division_id)  # Domain 클래스의 생성자 형식지정으로 바로 값 넣기
        Model.insert_db(do)

        View.insert_end()




    def show(self):
        """
        2. 회원 목록 보기 메소드
        """
        all_list = Model.show()
        View.show_all(all_list)


    def modify(self):
        """
        3. 회원 정보 수정 메소드
        """
        View.modify_head()
        inputname = View.name_input()
        inputname_objectlist = Model.search_inputname_matching(inputname)
        inputname_list = Model.object_list_disassemble(inputname_objectlist)

        if inputname_list:
            # 리스트에 요소가 있을 경우(검색한 이름과 매칭되는 이름이 있을경우)
            View.modify_show_inputname_list(inputname_list)
            while 1:
                try:
                    # 입력받은 번호가 범위 외 일때의 예외처리
                    input_id = View.index_input()
                    update_id = inputname_list[input_id - 1][0]
                    break
                except ValueError:
                    Error.wrong_number()
                except IndexError:
                    Error.wrong_number()
            while 1:
                try:
                    name = View.name_input()
                    Error.not_name(name)
                    break
                except Error.NameError as e:
                    View.print_Error(e)
            while 1:
                try:
                    phone = View.phone_input()
                    phone = Error.not_reg_phone(phone)  # 정규식에 맞게 연락처 형식 수정
                    break
                except Error.PhoneRegError as e:
                    View.print_Error(e)
            while 1:
                try:
                    email = View.email_input()
                    Error.not_reg_email(email)
                    break
                except Error.EmailError as e:
                    View.print_Error(e)
            while 1:
                try:
                    division_input = View.division_input()
                    Error.not_division(division_input)
                    break
                except Error.DivisionError as e:
                    View.print_Error(e)

            division_id = Model.division_id_create(division_input)
            do = Domain(update_id, name, phone, email, division_id)

            Model.modify_run(do)
            View.modify_end()

        else:
            # 리스트가 비어있으면(db에 입력된 이름과 매칭되는 이름이 없다면)
            Error.wrong_name()


    def delete(self):
        """
        4. 회원 삭제 메소드
        """
        View.delete_head()
        inputname = View.name_input()
        inputname_objectlist = Model.search_inputname_matching(inputname)
        inputname_list = Model.object_list_disassemble(inputname_objectlist)

        if inputname_list:
            View.delete_show_inputname_list(inputname_list)
            while 1:
                try:
                    input_id = View.index_input()
                    delete_id = inputname_list[input_id - 1][0]
                    break
                except ValueError:
                    Error.wrong_number()
                except IndexError:
                    Error.wrong_number()

            Model.delete_run(delete_id)
            View.delete_end()
        else:  # 리스트가 비어있으면
            Error.wrong_name()


Model = Model()  # Model Class new
View = View()  # View Class new
Contact = Contact()  # Contact Class new

while 1:
    run_menu = View.menu()
    if run_menu == '1':  # 입력받은 번호가 '1'일 경우
        Contact.insert()

    elif run_menu == '2':  # 입력받은 번호가 '2'일 경우
        Contact.show()

    elif run_menu == '3':  # 입력받은 번호가 '3'일 경우
        Contact.modify()

    elif run_menu == '4':  # 입력받은 번호가 '4'일 경우
        Contact.delete()

    elif run_menu == '5':  # 입력받은 번호가 '5'일 경우
        Model.delete_exit()
        View.main_end()
        break  # 프로그램을 종료
    else:
        View.main_numerror()  # 예외처리
```