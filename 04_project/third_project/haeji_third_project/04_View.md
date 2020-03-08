```python

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

```
