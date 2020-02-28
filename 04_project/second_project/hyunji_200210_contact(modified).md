# Done list (2020.02.10)
## enumerate 사용해봄
## tuple 변수명을 대문자로 변경해봄
## while 문 안에 주석을 닥스트링이 아닌 블록 주석으로 변경해봄

# To do list
## private 변수 선언해보기 (언더스코어 써서)
## 연락처 접근 시 get, set 사용해보기
## 모듈 나눠보기.

```python

import pickle


def main_menu():
    '''메인 메뉴를 프린트하는 함수이다.'''
    print(
    """
    =======================================
    다음 메뉴의 번호 중 하나를  선택하세요.
    =======================================
    1. 회원 추가
    2. 회원 목록 보기
    3. 회원 정보 수정하기
    4. 회원 삭제
    5. 종료
    """
    )

class CellPhoneError(Exception):
    '''전화번호에 문자나 기호, 공백이 들어올 수 없게 하였다.
       등록하는 회원이 외국인일 경우를 고려해 길이 제한은 두지 않았다.
    '''
    def __str__(self):
        return "\n*전화번호는 문자나 기호를 제외한 0부터 9까지의 숫자만 입력 가능합니다."

class SortError(Exception):
    '''DEFINED_SORT라는 tuple내의 값만 구분으로 사용할 수 있으며 공백또한 불가능하게 하였다.'''
    def __str__(self):
        return "\n*구분은 (가족, 친구, 회사, 기타) 내의 값만 입력 가능합니다."

class InsertNameError(Exception):
    '''이름에 공백이 입력될 경우 발생하는 오류이다.'''
    def __str__(self):
        return "\n*이름을 입력하세요"
class File:
    '''파일을 직접 로드, 저장하는 클래스이다.'''
    def __init__(self,file_name):
        '''파일명을 범용적으로 사용 가능하도록 파일명 파라미터를 따로 받게 하였다.'''
        self.file_name = file_name

    def pic_load(self):
        '''이미 만들어진 연락처가 존재할 경우 연락처 파일을 total이라는 전체 연락처 딕셔너리에 담았다.
        이미 만들어진 연락처가 존재하지 않는 경우 total을 빈 딕셔너리로 선언하였다.
        '''
        try:
            with open(self.file_name,"rb") as contact:
                data = pickle.load(contact)
                total = data
        except FileNotFoundError as e:
             total = {}

        return total

    def pic_write(self):
        '''정상적으로 종료될 시 연락처가 저장되도록 하는 함수이다.'''
        with open(self.file_name,"wb") as contact:
            data = total
            pickle.dump(data, contact)


class FileManager:
    '''파일을 직접 관리하는 클래스이다.'''
    def add(self, aom):
        '''등록과 관련있는 함수이다.'''
        DEFINED_SORT = ("가족","친구","회사","기타")
        print(f"{aom}할 회원의 정보를 입력하세요.")
        flag = True
        while(flag):
            #수정은 다시말해 삭제 후 등록이다.
            #하지만 삭제가 이루어진 후 등록이 정상적으로 이루어지지 않을 시
            #삭제만 수행되고 등록은 되지 않은 상태로 메인메뉴로 돌아가게 되므로
            #등록에서 오류가 발생하는 경우 while문을 통해 등록을 마무리하게 만들었다.

            try:
                name = input("이름: ")
                if not name:
                    raise InsertNameError()
                cellphone = input("전화번호(ex. 01012345678): ")
                if not cellphone.isdigit():
                    '''전화번호가 숫자 이외의 값일 경우이다.'''
                    raise CellPhoneError()

                sort = input("구분(ex. 가족, 친구, 회사, 기타): ")
                if sort not in DEFINED_SORT:
                    '''DEFINED_SORT 이외의 값을 입력하는 경우이다.'''
                    raise SortError()

                personal = {"이름":name, "전화번호":cellphone, "구분":sort}
                total[cellphone] = personal
                print(f"{aom}이 완료되었습니다.")

                flag = False    
                '''여기까지 실행되었다는 것은 고려된 모든 예외가 발생하지 않은 것이다.
                메인으로 돌아간다.
                '''
            except InsertNameError as e:
                print(e)
            except CellPhoneError as e:
                print(e)
            except SortError as e:
                print(e)



    def mem_list(self):
        '''저장된 회원의 목록을 보여주는 함수이다.'''
        print("총 %d명의 회원이 저장되어 있습니다." %len(total))
        for key, value in total.items():
            print(f'회원정보 : 이름 = {value["이름"]}, '
                  f'전화번호 = {value["전화번호"]}, '
                  f'구분 = {value["구분"]}')

    def del_or_mod(self, dom):
        '''수정하거나 삭제할 때만 호출되어야하는 함수이다.'''
        print(f"\n{dom}할 회원의 이름을 입력하세요.")
        name = input("이름: ")
        repeated_member = [key for key, value in total.items() if name == value['이름']]
        '''입력받은 이름이 존재할 경우 회원의 전화번호를 추가하는 리스트를 만든다.'''
        if repeated_member:
            try:
                print(f'\n총 {len(repeated_member)}개의 목록이 검색되었습니다.'
                      f'\n다음 중 {dom}할 회원의 번호를 입력하세요.\n')
                for i, cellphone in enumerate(repeated_member):
                    print(f'{i+1}. '
                          f'이름 = {total[cellphone]["이름"]}, '
                          f'전화번호 : {total[cellphone]["전화번호"]}, '
                          f'구분 : {total[cellphone]["구분"]}')

                del total[repeated_member[int(input())-1]]
                if dom == "삭제":
                    '''삭제시에는 별도의 등록이 필요하지 않기 때문에 메인메뉴로 돌아간다.'''
                    print("삭제가 완료되었습니다.")
                else:
                    self.add("수정")
                    '''수정시 새로운 회원정보를 입력하게 하는 것이다.
                    add함수는 수정에 오류가 생길 시 메인메뉴로 돌아가지 않고
                    while문을 통해 등록을 완료하도록 하였다.
                    '''
            except IndexError:
                '''수정할 회원의 번호를 입력받을 때 주어진 번호 외의값을 입력하는 경우 발생하는 오류이다.'''
                print(f"*번호를 잘못 입력하였습니다. 검색된 회원만 {dom}가능합니다.")

            except ValueError:
                '''수정할 회원의 번호를 입력받을 때 문자나 기호 입력시 발생하는 오류이다.'''
                print("*주어진 번호 외의 문자나 기호는 입력할 수 없습니다.")
        else:
            print("해당하는 회원의 정보가 없습니다.\n")

file_name = "contact.txt"   # 사용자가 원하는 파일명을 사용하여도 좋다.
File = File(file_name)
FileManager = FileManager()
total = File.pic_load()
mark = True
while(mark):
    main_menu()
    num = input()
    if num == '1':
        FileManager.add("등록")

    elif num == '2':
        FileManager.mem_list()

    elif num == '3':
        FileManager.del_or_mod("수정")

    elif num == '4':
        FileManager.del_or_mod("삭제")

    elif num == '5':
        File.pic_write()
        mark = False

    else :
        print("*유효하지 않은 입력입니다. 1~5까지의 숫자를 입력해주세요.")

    


```