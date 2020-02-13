```python
#파이썬 연락처 프로그램
import pickle


def menu():  #메인화면 출력할 menu()메소드 선언
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
#메인화면 문자열로 만들어서 main변수에 저장
    print(main)  #메인화면 출력
    select = input() #선택값 받을 select변수 선언 및 입력값 삽입
    return select #select의 객체 리턴


class File: #파일 입출력 클래스
    def __init__(self, file_name):
        self.file_name = file_name
    
    def load(self):
        try:
            with open(self.file_name, 'rb') as contact:
                allperson = pickle.load(contact)

        except FileNotFoundError as e:
            allperson = {}

        return allperson

    def write(self):
        with open(self.file_name, 'wb')as contact:
            pickle.dump(allperson, contact)


class Contact:

    def Insert(self, aom):  #회원 추가에 대한 Insert()메소드 선언
        print(f'\n{aom}할 회원의 정보를 입력하세요.')  
        name = input('이름 : ')
        phone = input('전화번호(ex: 01012345678): ')
        division = input('구분(ex.가족, 친구, 회사. 기타): ')
        # 이름, 전화번호, 구분을 입력받아 각각 name, phone, division변수에 저장

        person = {'이름':name, '전화번호':phone, '구분':division}  #입력받은 값들을 안쪽 딕셔너리인 person에 저장
        allperson[phone]=person  #바깥쪽 딕셔너리인 allperson에 person딕셔너리를 입력받은 phone(전화번호)를 KEY로 하여 저장


    def Show(self):    
        print('총 %d명의 회원이 저장되어 있습니다.'% len(allperson)) 

        for key in allperson.keys():
            print(f"회원정보 : 이름 = {allperson[key]['이름']}, "
                  f"전화번호 = {allperson[key]['전화번호']}, "
                  f"구분 = {allperson[key]['구분']}")
            
                
            
    def Modify_or_Delete(self, dom):  
        print(f'\n{dom}할 회원의 이름을 입력하세요.')  
        inputname = input('이름 : ')  #입력받은 이름을 inputname변수에 저장
        #allperson.items()로 key, value를 가져온다음 거기서 key만 저장 (if문에서 true일때만)
        repeated_member = [key for key, value in allperson.items() if inputname == value['이름']]
    
        if repeated_member:
            
            print(f'\n총 {len(repeated_member)}개의 목록이 검색되었습니다.'
                  f'\n다음 중 {dom}할 회원의 번호를 입력하세요.\n')
            for i in range(len(repeated_member)):
                print(f'{i+1}. '
                      f'이름 = {allperson[repeated_member[i]]["이름"]}, '
                      f'전화번호 : {allperson[repeated_member[i]]["전화번호"]}, '
                      f'구분 : {allperson[repeated_member[i]]["구분"]}')

            del allperson[repeated_member[int(input())-1]]
            if dom == "삭제":
                print("삭제가 완료되었습니다.")
            else:
                self.Insert("수정")
                 
        else:
            print("해당하는 회원의 정보가 없습니다.\n")


                
file_name = 'Contact.pickle'
File = File(file_name)
Contact = Contact()
allperson=File.load() #파일 로드       
                      
while 1 :  #while문 무한반복 시작
    run_menu = menu()  
    if run_menu == '1':  #입력받은 번호가 '1'일 경우
        Contact.Insert('등록')

    elif run_menu == '2':  #입력받은 번호가 '2'일 경우
        Contact.Show()

    elif run_menu == '3':  #입력받은 번호가 '3'일 경우
        Contact.Modify_or_Delete('수정')

    elif run_menu == '4':  #입력받은 번호가 '4'일 경우
        Contact.Modify_or_Delete('삭제')

    elif run_menu == '5':  #입력받은 번호가 '5'일 경우
        File.write() #종료시에 파일 덮어쓰기
        print('종료되었습니다.') 
        break  #프로그램을 종료
    else:
        print('1~5의 숫자를 입력해주십시오.')  #예외처리 - 1,2,3,4,5외의 숫자나 혹은 문자를 입력시에 1~5의 숫자를 입력하라는 문구 출력


```