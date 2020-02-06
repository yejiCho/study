```python
#파이썬 연락처 프로그램

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
    select = input('입력 : ') #선택값 받을 select변수 선언 및 입력값 삽입
    return select #select의 객체 리턴



def Insert():  #회원 추가에 대한 Insert()메소드 선언
    print()  #한칸 띄기
    print('등록할 회원의 정보를 입력하세요.')  
    name = input('이름 : ')
    phone = input('전화번호(ex: 01012345678): ')
    division = input('구분(ex.가족, 친구, 회사. 기타): ')
    # 이름, 전화번호, 구분을 입력받아 각각 name, phone, division변수에 저장

    person = {'이름':name, '전화번호':phone, '구분':division}  #입력받은 값들을 안쪽 딕셔너리인 person에 저장
    allperson = {phone:person}  #바깥쪽 딕셔너리인 allperson에 person딕셔너리를 입력받은 phone(전화번호)를 KEY로 하여 저장
    return allperson  #바깥쪽 딕셔너리인 allperson의 객체를 리턴




def Show(allperson):  #전체 회원 목록을 보여주는 Show()메소드 선언 및 바깥쪽 딕셔너리인 allperson 받아오기
    n = len(list(allperson.keys()))  #바깥쪽 딕셔너리의 KEY값들을 List에 저장하고 그 List의 길이(요소 갯수)를 n이라는 변수에 저장
    print('총 %d명의 회원이 저장되어 있습니다.'% n)  #n이라는 변수를 이용하여 입력된 총 회원 수 출력

    for akeys in allperson.keys():  #for in 문 - 바깥쪽 딕셔너리의 KEY값들의 List를 뽑아서 akeys라는 변수에 하나씩 저장하여 반복문 시작
        avalues = allperson.get(akeys)  #바깥쪽 딕셔너리에 akeys에 저장된 KEY값과 매칭되는 VALUE값인 안쪽 딕셔너리를 avalues변수에 저장
        print('회원정보 : 이름 = '+avalues.get('이름')+', 전화번호 = '+avalues.get('전화번호')+', 구분 = '+avalues.get('구분'))
        #안쪽 딕셔너리인 avalues에서 '이름', '전화번호', '구분' 각각에 매칭되는 VALUE값 출력




def Modify(allperson):  #회원정보 수정을 위한 Modify()메소드 선언 및 바깥쪽 딕셔너리인 allperson 받아오기
    keylist = []  #입력받은 이름과 매칭되는 KEY값 저장할 keylist라는 빈 List선언
    print('수정할 회원의 이름을 입력하세요.')  
    inputname = input('이름 : ')  #입력받은 이름을 inputname변수에 저장

    for akeys in allperson.keys():  #for in 문 - 바깥쪽 딕셔너리의 KEY값들의 List를 뽑아서 akeys라는 변수에 하나씩 저장하여 반복문 시작
        avalues = allperson.get(akeys)  #바깥쪽 딕셔너리에 akeys에 저장된 KEY값과 매칭되는 VALUE값인 안쪽 딕셔너리를 avalues변수에 저장
        if inputname == avalues.get('이름'):  #입력받은 이름이 안쪽 딕셔너리에 '이름'이라는 KEY값에 매칭되는 VALUE와 일치할 경우
            keylist.append(akeys)  #해당 바깥쪽 KEY값을 keylist라는 빈 List에 저장
            #for문으로 반복되면서 keylist에는 입력받은 이름과 매칭되는 안쪽 딕셔너리의 KEY값들이 저장됨

    n = len(keylist)  #keylist의 길이를 n변수에 저장

    if  n == 0:  #keylist의 길이가 0이면(keylist가 비어있다면)
        print('해당하는 회원 정보가 없습니다.')  #입력받은 이름에 매칭되는 회원의 정보가 없다는 문구 출력        
    else:  #keylist의 길이가 0이 아니라면(keylist에 요소가 있다면)
        print('총 %d개의 목록이 검색되었습니다.'% n)  #keylist의 길이를 저장하고 있는 n변수로 검색된 총 목록의 수 출력
        print('아래 목록 중 수정할 회원의 번호를 입력하세요.')
        for key in keylist:  #for in 문 - keylist의 요소(바깥쪽 KEY값들) 뽑아서 key라는 변수에 하나씩 저장하여 반복문 시작
            num = int(keylist.index(key))  #keylist에서 해당 요소의 index를 int형으로 추출하여 num변수에 저장
            inputvalue = allperson.get(key)  #바깥쪽 딕셔너리에서 keylist의 해당 요소(바깥쪽 KEY값)으로 매칭되는 안쪽 딕셔너리를 inputvalue변수에 저장
            print('%d. 이름 = '% (num+1) +inputvalue.get('이름')+', 전화번호 = '+inputvalue.get('전화번호')+', 구분 = '+inputvalue.get('구분'))
            #keylist의 index+1하여 번호를 부여하고 inputvalue(안쪽 딕셔너리)에서 '이름', '전화번호', '구분' 각각에 매칭되는 VALUE값 출력

        inputnum = input('번호 : ')  # 입력한 이름과 매칭되는 목록 중에 수정할 목록을 선택받을 변수 선언 및 입력받기
        inputnum=int(inputnum) if inputnum.isdigit() else -1  
        #예외처리 방법 1 - isdigit함수 사용해서 inputnum변수가 숫자이면 inputnum을 int형으로 변환하고 숫자가 아니면 -1을 저장하는 조건문
        if 0<inputnum<=len(keylist):  #위의 예외처리 후 inputnum이 0보다 크고 keylist의 길이보다 작을경우에만 다음단계를 진행하고 
            del allperson[keylist[inputnum-1]]  #바깥쪽 딕셔너리에서 keylist(입력받은 이름과 매칭되는 바깥쪽 딕셔너리의 KEY값들)에 입력받은 inputnum-1 과 매칭되는 요소(안쪽 딕셔너리) 삭제
            print()
            print('수정할 정보를 입력하세요.')
            name = input('이름 : ')
            phone = input('전화번호(ex: 01012345678): ')
            division = input('구분(ex.가족, 친구, 기타): ')
            #수정할 정보를 받을 변수 선언 및 저장

            person = {'이름':name, '전화번호':phone, '구분':division}  #입력받은 정보를 person딕셔너리에 저장
            allperson = {phone:person}  #위의 person 딕셔너리를 바깥쪽 딕셔너리로 사용할 allperson에 저장
            print('수정이 완료되었습니다.')
            

        else :
            print()
            print('올바른 번호를 입력해주십시오.')  #inputnum이 if문 범위 밖에 있을 경우 올바른번호를 입력해달라는 문구 출력
            
    return allperson  #allperson의 객체(수정된 딕셔너리)를 리턴
        



def Delete(allperson):  #회원정보 삭제를 위한 Delete()메소드 선언 및 바깥쪽 딕셔너리인 allperson 받아오기
    keylist = []  #입력받은 이름과 매칭되는 KEY값 저장할 keylist라는 빈 List선언
    print('삭제할 회원의 이름을 입력하세요.')
    inputname = input('이름 : ')  #입력받은 이름을 inputname변수에 저장

    for akeys in allperson.keys():  #for in 문 - 바깥쪽 딕셔너리의 KEY값들의 List를 뽑아서 akeys라는 변수에 하나씩 저장하여 반복문 시작
        avalues = allperson.get(akeys)  #바깥쪽 딕셔너리에 akeys에 저장된 KEY값과 매칭되는 VALUE값인 안쪽 딕셔너리를 avalues변수에 저장
        if inputname == avalues.get('이름'):  #입력받은 이름이 안쪽 딕셔너리에 '이름'이라는 KEY값에 매칭되는 VALUE와 일치할 경우
            keylist.append(akeys)  #해당 바깥쪽 KEY값을 keylist라는 빈 List에 저장

    n = len(keylist)  #keylist의 길이를 n변수에 저장

    if  n == 0:  #keylist의 길이가 0이면(keylist가 비어있다면)
        print('해당하는 회원 정보가 없습니다.')  #입력받은 이름에 매칭되는 회원의 정보가 없다는 문구 출력   
    else:  #keylist의 길이가 0이 아니라면(keylist에 요소가 있다면)
        print('총 %d개의 목록이 검색되었습니다.'% n)  #keylist의 길이를 저장하고 있는 n변수로 검색된 총 목록의 수 출력
        print('아래 목록 중 삭제할 회원의 번호를 입력하세요.')
        for key in keylist:  #for in 문 - keylist의 요소(바깥쪽 KEY값들) 뽑아서 key라는 변수에 하나씩 저장하여 반복문 시작
            num = int(keylist.index(key))  #keylist에서 해당 요소의 index를 int형으로 추출하여 num변수에 저장
            inputvalue = allperson.get(key)  #바깥쪽 딕셔너리에서 keylist의 해당 요소(바깥쪽 KEY값)으로 매칭되는 안쪽 딕셔너리를 inputvalue변수에 저장
            print('%d. 이름 = '% (num+1) +inputvalue.get('이름')+', 전화번호 = '+inputvalue.get('전화번호')+', 구분 = '+inputvalue.get('구분'))
            #keylist의 index+1하여 번호를 부여하고 inputvalue(안쪽 딕셔너리)에서 '이름', '전화번호', '구분' 각각에 매칭되는 VALUE값 출력

        #예외처리 방법 2 - try문 사용
        try :  #int형인 inputnum에 숫자가 아닌 다른것을 입력받았을 경우를 예외처리하기 위한 try문
            inputnum = int(input('번호 : ')) # 입력한 이름과 매칭되는 목록 중에 수정할 목록을 선택받을 변수 선언 및 입력받기
            del allperson[keylist[inputnum-1]]  #바깥쪽 딕셔너리에서 keylist(입력받은 이름과 매칭되는 바깥쪽 딕셔너리의 KEY값들)에 입력받은 inputnum-1 과 매칭되는 요소(안쪽 딕셔너리) 삭제
            print()
            print('삭제가 완료되었습니다.')
        except:
            print()
            print('올바른 번호를 입력해주십시오.')  #올바른번호를 입력해달라는 문구 출력
              
        
        
                      
def run():  #실행할 run메소드 선언
    allperson = {}  #바깥쪽 딕셔너리를 받을 allperson이라는 빈 딕셔너리 선언
    while 1 :  #while문 무한반복 시작
        run_menu = menu()  #menu()메소드에서 리턴한 객체(메인메뉴에서 입력받은 번호)를 run_menu변수에 저장
        if run_menu == '1':  #입력받은 번호가 '1'일 경우
            run_Insert = Insert()  #Insert()메소드를 실행하고 리턴한 객체를 run_Insert변수에 저장
            allperson.update(run_Insert) #Insert()메소드에서 리턴한 객체(바깥쪽 딕셔너리)를 빈 딕셔너리인 allperson에 update
        elif run_menu == '2':  #입력받은 번호가 '2'일 경우
            Show(allperson)  #Show()메소드를 allperson을 삽입하여 실행
        elif run_menu == '3':  #입력받은 번호가 '3'일 경우
            run_Modify = Modify(allperson)  #Modify()메소드를 allperson을 삽입하여 실행한 후 해당 메소드에서 리턴한 객체를 run_Modify변수에 저장
            allperson.update(run_Modify)  #Modify()메소드에서 리턴한 객체(수정된 딕셔너리)를 allperson에 update
        elif run_menu == '4':  #입력받은 번호가 '4'일 경우
            Delete(allperson)  #Delete()메소드를 allperson을 삽입하여 실행
        elif run_menu == '5':  #입력받은 번호가 '5'일 경우
            print('종료되었습니다.') 
            break  #프로그램을 종료
        else:
            print('1~5의 숫자를 입력해주십시오.')  #예외처리 - 1,2,3,4,5외의 숫자나 혹은 문자를 입력시에 1~5의 숫자를 입력하라는 문구 출력


run()  #run함수 실행
```