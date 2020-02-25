# 3차과제

```sql

# DB 쿼리

-- PHONEBOOK 테이블 생성
CREATE TABLE PHONEBOOK (
	p_id number(35),
	pname VARCHAR2(50) NOT NULL,
	telnum	varchar2(50) not null,
	email varchar2(50) not null,
	sepno number(35) not null
);

-- PHONEBOOK에서 p_id를 PK로 설정
alter table PHONEBOOK
add constraints PHONEBOOK_p_id_pk
primary key(p_id);

-- SEPARATION 테이블 생성
CREATE TABLE SEPARATION (
	sepno number(35),
	sep varchar2(50) NOT NULL
);

-- SEPARATION에 sepno를 PK로 설정
alter table SEPARATION
add constraints SEPARATION_sepno_pk
primary key(sepno);

-- PHONEBOOK에서 SEPARATION의 sepno를 FK로 참조
alter table PHONEBOOK
add constraints PHONEBOOK_sepno_fk
foreign key(sepno)
references SEPARATION(sepno);

```

```python

# python 

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
                Error.name_check(pname)
                break
            except Error.NameError as e:
                self._view.print_e(e)
        while 1:
            telnum = self._view.input_telnum()
            try:
                telnum = Error.telnum_check(telnum)
                break
            except Error.TelnumError as e:
                self._view.print_e(e)
        while 1:
            email = self._view.input_email()
            try:
                Error.email_check(email)
                break
            except Error.EmailError as e:
                self._view.print_e(e)
        while 1:
            sep_name = self._view.input_sep_name()
            
            try:
                Error.sep_name_check(sep_name)
                break
            except Error.SepNameError as e:
                self._view.print_e(e)

        p_id = self._model.select_maxid()
        sepno = self._model.get_sepno(sep_name)

        DTO = Domain(p_id, pname, telnum, email, sepno)
        
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
                Error.name_check(name)
                break
            except Error.NameError as e:
                self._view.print_e(e)
        mod_list = self._model.search_modify_list(name)

        if mod_list:
            self._view.modi_search_command(mod_list)

            for row in mod_list:
                mod_ind = mod_list.index(row)
                self._view.modi_print(mod_ind, row)

            while 1:
                try:
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
                    Error.name_check(pname)
                    break
                except Error.NameError as e:
                    self._view.print_e(e)
            while 1:
                telnum = self._view.input_telnum()
                try:
                    telnum = Error.telnum_check(telnum)
                    break
                except Error.TelnumError as e:
                    self._view.print_e(e)
            while 1:
                email = self._view.input_email()
                try:
                    Error.email_check(email)
                    break
                except Error.EmailError as e:
                    self._view.print_e(e)
            while 1:
                sep_name = self._view.input_sep_name()

                try:
                    Error.sep_name_check(sep_name)
                    break
                except Error.SepNameError as e:
                    self._view.print_e(e)

            mod_domain.set_pname(pname)
            mod_domain.set_telnum(telnum)
            mod_domain.set_email(email)
            
            sepno = self._model.get_sepno(sep_name)
            mod_domain.set_sep_no(sepno)
            
            self._model.update_db(mod_domain)
            self._view.modi_complete()

            self._model.sep_delete_all()
        
        else:
            self._view.not_agree()

    # 회원 목록 삭제 함수
    def delete(self):
        self._view.del_command()
        
        while 1:
            name = self._view.input_pname()
            try:
                Error.name_check(name)
                break

            except Error.NameError as e:
                self._view.print_e(e)

        del_list = self._model.search_delete_list(name)

        if del_list:
            self._view.del_search_command(del_list)

            for row in del_list:
                del_ind = del_list.index(row)
                self._view.del_print(del_ind, row)

            while 1:
                try:
                    put_ind = self._view.put_ind()
                    del_domain = del_list[put_ind-1]
                    break

                except IndexError:
                    self._view.not_find_num()

                except ValueError:
                    self._view.not_find_num()

            self._model.delete_db(del_domain)
            self._view.del_complete()

            self._model.sep_delete_all()

        else:
            self._view.not_agree()

    def run(self):

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

----------------------------------------------------------------------------

# Model
import cx_Oracle
from Domain import Domain

class Model:

    # 모든 검색 결과를 불러오는 sql 실행함수 생성
    def sel_all(self, sql):
        conn = cx_Oracle.connect("haeji/1234@localhost:1521/xe")
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()

        cursor.close()
        conn.close()
        return data

    # 하나의 검색 결과를 불러오는 sql 실행함수 생성
    def sel_one(self, sql):
        conn = cx_Oracle.connect("haeji/1234@localhost:1521/xe")
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()

        cursor.close()
        conn.close()
        return data

    # delete, update에 쓸 sql 함수 생성
    def dml(self, sql, data):
        conn = cx_Oracle.connect("haeji/1234@localhost:1521/xe")
        cursor = conn.cursor()
        cursor.execute(sql, data)
        cursor.close()
        conn.commit()
        conn.close()

    # delete, update에 쓸 sql 함수 생성(data 없는 버전)
    def dml_one(self, sql):
        conn = cx_Oracle.connect("haeji/1234@localhost:1521/xe")
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()

    """
    phonebook에 있는 p_id(pk) 중 max 값을 검색해서 sel_id에 저장한 다음
    p_id가 없을 경우 1로 시작하며, 있을 경우 max p_id에서 +1을 해서 저장
    """
    def select_maxid(self):
        sql = "select max(p_id) from PHONEBOOK"
        sel_id = self.sel_one(sql)[0]
        p_id = sel_id + 1 if sel_id else 1
        return p_id
    
    #입력한 구분(sep)과 같은 구분을 SEPARATION 테이블에서 검색해서 sepno(구분ID)를 뽑아와서 get_sepno에 저장
    def get_sepno(self, sep_name):
        sql = f"select sepno from separation where sep = '{sep_name}'"
        get_sepno = self.sel_one(sql)

        if get_sepno:
            # get_sepno의 값이 있을 경우 get_sepno를 리턴
            get_sepno = get_sepno[0]
            return get_sepno

        else:
            """
            get_sepno의 값이 없을 경우 sepno(구분)의 max를 검색한다음 
            sepno가 하나도 없으면 1부터 시작하고 아니면 max sepno에서 +1해서 저장
            그리고 새로 추가된 sep(구분)과 sepno(구분ID)를 insert해서 구분 테이블에 저장
            """
            sql_1 = "select max(sepno) from SEPARATION"
            max_sep = self.sel_one(sql_1)[0]
            get_sepno = max_sep + 1 if max_sep else 1

            sql_2 = "insert into SEPARATION values(:1, :2)"
            data = (get_sepno, sep_name)
            self.dml(sql_2, data)
            return get_sepno

    # 생성한 DTO에 입력한 값들을 담아와서 데이터베이스에 삽입함
    def insert_db(self, DTO):
        sql = "insert into PHONEBOOK values(:1, :2, :3, :4, :5)"
        p_id = DTO.get_p_id()
        pname = DTO.get_pname()
        telnum = DTO.get_telnum()
        email = DTO.get_email()
        sepno = DTO.get_sepno()
        data = (p_id, pname, telnum, email, sepno)
        self.dml(sql, data)

    """
    PHONEBOOK에 저장된 id(pk)와 pname(이름), telnum(연락처), email(이메일), 
    그리고 SEPARATION(구분테이블)에 있는 sep(구분)을 검색해서 모두 all_list에 저장
    """
    def output(self):
        sql = "select a.p_id, a.pname, a.telnum, a.email, b.sep " \
              "from PHONEBOOK a, SEPARATION b " \
              " where a.sepno  = b.sepno"
        
        all_list = self.sel_all(sql)
        return all_list

    """
    입력받은 수정할 회원 이름과 같은 PHONEBOOK에 저장된 id(pk)와 pname(이름), telnum(연락처), email(이메일), 
    그리고 SEPARATION(구분테이블)에 있는 sep(구분)을 검색해서 모두 mod_data에 저장
    그리고 mod_data를 리스트 내포를 써서 Domain에 저장함. 그리고 그 Domain은 mod_list에 저장
    """
    def search_modify_list(self, name):
        sql = f"select a.p_id, a.pname, a.telnum, a.email, b.sep " \
                f"  from PHONEBOOK a, SEPARATION b " \
                f" where a.sepno = b.sepno " \
                f"   AND pname = '{name}'"

        mod_data = self.sel_all(sql)
        mod_list = [Domain(row[0], row[1], row[2], row[3], row[4])
                    for row in mod_data]
        return mod_list

    # 생성한 DTO에 입력한 값들을 담아와서 데이터베이스에 업데이트함
    def update_db(self, DTO):
        p_id = DTO.get_p_id()
        pname = DTO.get_pname()
        telnum = DTO.get_telnum()
        email = DTO.get_email()
        sepno = DTO.get_sepno()
        sql = f"update PHONEBOOK set pname = '{pname}', " \
              f"telnum = '{telnum}', email = '{email}', " \
              f" sepno = '{sepno}' where  p_id = '{p_id}'"
        self.dml_one(sql)

    """
    입력받은 삭제할 회원 이름과 같은 PHONEBOOK에 저장된 id와 pname(이름), telnum(연락처), email(이메일), 
    그리고 SEPARATION(구분테이블)에 있는 sep(구분)을 검색해서 모두 del_data에 저장
    그리고 del_data를 리스트 내포를 써서 Domain에 저장함. 그리고 그 Domain은 del_list에 저장
    """
    def search_delete_list(self, name):
        sql = f"select a.p_id, a.pname, a.telnum, a.email, b.sep " \
              f"  from PHONEBOOK a, SEPARATION b " \
              f" where a.sepno = b.sepno AND pname = '{name}'"
        del_data = self.sel_all(sql)
        del_list = [Domain(row[0], row[1], row[2], row[3], row[4])
                    for row in del_data]
        return del_list

    # 생성한 DTO에서 p_id를 받아와서 p_id(PK)와 같은 p_id를 가지고 있는 데이터를 PHONEBOOK에서 삭제함
    def delete_db(self, DTO):
        p_id = DTO.get_p_id()
        sql = f"delete from PHONEBOOK where p_id = '{p_id}'"
        self.dml_one(sql)
    
    # SEPARATION(구분) 테이블을 검색해서 PHONEBOOK에서 참조하고 있지 않은 구분들을 전체 삭제
    def sep_delete_all(self):
        sql = "delete from SEPARATION " \
              "where sepno in (select b.sepno " \
                               "from PHONEBOOK a, SEPARATION b " \
                               "where a.sepno(+) = b.sepno " \
                               "group by b.sepno " \
                               "having count(a.sepno) = 0)"
        self.dml_one(sql)


----------------------------------------------------------------------------

# View

from Domain import Domain

class View:
    
    # 연락처 프로그램 메뉴화면
    def menu(self):
        pmenu = '''
        ==================================
           다음 메뉴 중 하나를 선택하세요
        ==================================
        1. 회원 추가
        2. 회원 목록 보기
        3. 회원 정보 수정하기
        4. 회원 삭제
        5. 종료
        '''

        print(pmenu)
        main = input('▶ ▶ ')
        return main

    # 회원 정보 입력창 헤드 문구
    def ins_command(self):
        return print("등록할 회원의 정보를 입력하세요")

    # 회원 정보 이름 입력 문구
    def input_pname(self):
        return input("이름 : ")

    # 회원 정보 연락처 입력 문구
    def input_telnum(self):
        return input("전화번호(ex. 01012345678): ")

    # 회원 정보 이메일 입력 문구
    def input_email(self):
        return input("이메일 : ")

    # 회원 정보 구분 입력 문구
    def input_sep_name(self):
        return input("구분(ex.가족, 친구, 회사, 기타 등): ")
    
    # 모든 회원목록이 저장된 all_list를 for문을 돌려서 출력
    def view_allnum(self, all_list):
        if not all_list:
            print("회원 목록이 비어있습니다.")
        else:
            print('총 %d 명의 회원목록이 검색되었습니다.' % len(all_list))

            for row in all_list:
                print(f'회원정보 = 이름 : {row[1]}, ' 
                      f'전화번호 : {row[2]}, '
                      f'이메일 : {row[3]}, '
                      f'구분 : {row[4]}')

    # 회원 정보 수정 이름 입력 문구
    def modi_command(self):
        return print("수정할 회원의 이름을 입력하세요.")

    # 수정할 회원 검색 문구
    def modi_search_command(self, mod_list):
        print('총 %d 개의 목록이 검색되었습니다.' % len(mod_list))
        print('아래 목록 중 수정할 회원의 번호를 입력하세요')

    # 수정할 회원목록이 저장된 row를 index와 함께 for문을 돌려서 출력
    def modi_print(self, mod_ind, row):
        print(f'{mod_ind + 1}. 회원정보 = '
              f'이름 : {row.get_pname()}, '
              f'전화번호 : {row.get_telnum()}, '
              f'이메일 : {row.get_email()}, '
              f'구분 : {row.get_sepno()}')

    # 입력 창
    def put_ind(self):
        return int(input('▶ ▶ '))

    # 수정 완료 문구
    def modi_complete(self):
        return print('수정이 완료 되었습니다.')

    # 해당하는 연락처 검색 에러 출력 문구
    def not_agree(self):
        return print("해당하는 연락처가 없습니다.")

    # 회원 삭제 문구
    def del_command(self):
        return print("삭제할 회원의 이름을 입력하세요.")

    # 삭제할 회원 검색 문구
    def del_search_command(self, del_list):
        print('총 %d 개의 목록이 검색되었습니다.' % len(del_list))
        print('아래 목록 중 삭제할 회원의 번호를 입력하세요')

    # 삭제할 회원목록이 저장된 row를 index와 함께 for문을 돌려서 출력
    def del_print(self, del_ind, row):
        print(f'{del_ind+1}. 회원정보 = '
              f'이름 : {row.get_pname()}, '
              f'전화번호 : {row.get_telnum()}, '
              f'이메일 : {row.get_email()}, '
              f'구분 : {row.get_sepno()}')
    
    # 삭제 완료 문구
    def del_complete(self):
        return print('삭제가 완료 되었습니다.')
    
    # 인덱스 에러 처리 문구
    def not_find_num(self):
        return print("목록에 없는 번호입니다.")
    
    # 연락처 프로그램 종료 문구
    def print_end(self):
        return print("종료되었습니다")

    # 연락처 메뉴화면 입력 범위 에러 문구
    def not_range(self):
        return print("1부터 5까지의 숫자를 입력하세요.")

    # error 문구 출력
    def print_e(self, e):
        return print(e)

Domain = Domain()

----------------------------------------------------------------------------

# Error

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


----------------------------------------------------------------------------

#Domain

class Domain:
    # 생성자 선언 및 초기화
    def __init__(self, p_id=0, pname="", telnum="", email="", sepno=""):

        self._p_id = p_id
        self._pname = pname
        self._telnum = telnum
        self._email = email
        self._sepno = sepno

    def get_p_id(self):
        return self._p_id

    def set_p_id(self, p_id):
        self._p_id = p_id

    def get_pname(self):
        return self._pname

    def set_pname(self, pname):
        self._pname = pname

    def get_telnum(self):
        return self._telnum

    def set_telnum(self, telnum):
        self._telnum = telnum

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_sepno(self):
        return self._sepno

    def set_sep_no(self, sepno):
        self._sepno = sepno


```
