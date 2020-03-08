```python
# View

from Domain import Domain


class View:
    def menu(self):
        """
        메인화면 문자열로 만들어서 main 변수에 저장
        """
        main = '''  
        =====================================
           다음 메뉴 중 하나를 선택하세요.
        =====================================
        1. 회원 추가
        2. 회원 목록 보기
        3. 회원 정보 수정하기
        4. 회원 삭제
        5. 종료
        '''
        print(main)
        select = input("입력 : ")
        return select

# head, end 메소드
    def main_end(self):
        """
        프로그램 종료시 문구
        """
        print('종료되었습니다.')

    def main_numerror(self):
        """
        예외처리
        :return: 1,2,3,4,5외의 숫자나 혹은 문자를 입력시에 1~5의 숫자를 입력하라는 문구
        """
        print('1~5의 숫자를 입력해주십시오.')

    def insert_head(self):
        """
        :return: 회원추가 시 head 문구
        """
        print("\n등록할 회원의 정보를 입력하세요.")

    def insert_end(self):
        """
        :return: 회원추가 시 end 문구
        """
        print("\n등록이 완료되었습니다.")

    def modify_head(self):
        """
        :return: 회원수정 시 head 문구
        """
        print(f'\n수정할 회원의 이름을 입력하세요.')

    def modify_end(self):
        """
        :return: 회원수정 시 end 문구
        """
        print("수정이 완료되었습니다.")

    def delete_head(self):
        """
        :return: 회원삭제 시 head 문구
        """
        print(f'\n삭제할 회원의 이름을 입력하세요.')

    def delete_end(self):
        """
        :return: 회원삭제 시 end 문구
        """
        print("삭제가 완료되었습니다.")


#input메소드
    def name_input(self):
        """
        :return: 이름 입력받기
        """
        return input("이름: ")

    def phone_input(self):
        """
        :return: 연락처 입력받기
        """
        return input("전화번호(ex.01012345678, 010-1234-5678): ")

    def email_input(self):
        """
        :return: 이메일 입력받기
        """
        return input("e-mail(ex.abcd@email.com) : ")

    def division_input(self):
        """
        :return: 구분 입력받기
        """
        return input("구분(ex.가족, 친구, 회사, 기타): ")

    def index_input(self):
        """
        :return: 선택번호 입력받기
        """
        return int(input('입력 : '))


# 2. 회원목록 출력
    def show_all(self, all_list):
        """
        모든 회원정보가 오브젝트로 담긴 리스트인 all_list 를 받아
        for in문 통해 각각의 각각의 오브젝트들을 추출하여 getter 를 이용해 요소들을 추출해서
        문자열 포멧팅을 이용해 회원정보 형식에 맞게 출력
        :param all_list: 모든 회원정보가 오브젝트로 담긴 리스트인 all_list
        :return: 회원정보 형식에 맞게 출력
        """
        for object in all_list:
            print(f"회원정보 : 이름 = {object.get_name()}, "
                  f"전화번호 = {object.get_phone()}, "
                  f"E_mail = {object.get_email()}, "
                  f"구분 = {object.get_division()}")


# 3. 회원정보 수정, 삭제
    def modify_show_inputname_list(self, inputname_list):
        """
        입력받은 이름과 매칭되는 row 의 튜플이 들어있는 리스트를 입력받아
        리스트 길이(총 회원 수)를 len 함수 이용해 출력하고,
        리스트 길이를 range 함수를 이용해 인덱스로 사용할 범위값 생성하여 for 문 실행
        :param inputname_list: 입력받은 이름과 매칭되는 row 의 튜플이 들어있는 리스트
        :return: 리스트 길이(총 회원 수)를 len 함수 이용해 출력,
        인덱싱을 중첩해 리스트안에있는 각각의 튜플에서 필요한 요소 추출하여 출력
        """
        print(f'\n총 {len(inputname_list)}개의 목록이 검색되었습니다.'
              f'\n다음 중 수정할 회원의 번호를 입력하세요.\n')
        for i in range(len(inputname_list)):
            print(f'{i + 1}. ' #인덱스 +1해서 번호부여
                  f'이름 = {inputname_list[i][1]}, ' 
                  f'전화번호 = {inputname_list[i][2]}, '
                  f'E_mail = {inputname_list[i][3]}, '
                  f'구분 = {inputname_list[i][4]}')

    def delete_show_inputname_list(self, inputname_list):
        """
        modify_show_inputname_list()의 delete 버전
        """
        print(f'\n총 {len(inputname_list)}개의 목록이 검색되었습니다.' 
              f'\n다음 중 삭제할 회원의 번호를 입력하세요.\n')
        for i in range(len(inputname_list)):
            print(f'{i + 1}. '
                  f'이름 = {inputname_list[i][1]}, '
                  f'전화번호 = {inputname_list[i][2]}, '
                  f'E_mail = {inputname_list[i][3]}, '
                  f'구분 = {inputname_list[i][4]}')



    def print_Error(self,e):
        """
        :param e: 에러 메세지
        :return: 에러 메세지 출력
        """
        print(e)

```