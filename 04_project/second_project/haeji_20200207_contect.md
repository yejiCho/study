``` python

# Contect

# 출력할 메뉴화면 생성
def menu():
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
    # 입력받을 input()을 생성
    main = input('▶ ▶ ')
    # 메뉴화면을 리턴
    return main

# 회원 추가 함수 생성
def insert():
    print("등록할 회원의 정보를 입력하세요")
    # 입력받을 값들을 input()을 이용하여 입력할 수 있도록 생성
    name = input("이름 : ")
    telnum = input("전화번호(ex: 01012345678): ")
    sep = input("구분(ex.가족, 친구, 기타 ): ")

    # 안쪽 딕셔너리 생성
    inPhonebook = {'이름' : name, '전화번호' : telnum, '구분' : sep}
    # 바깥쪽 딕셔너리 생성
    Phonebook = {telnum : inPhonebook}

    # 바깥쪽 딕셔너리 리턴
    return Phonebook


# 회원 목록 보기 함수 생성
def allnum(Phonebook):
    # Phonebook의 key값 리스트를 만들어서 리스트로 변환한뒤 리스트 요소의 개수를 countlist에 저장
    countlist =  len(list(Phonebook.keys()))
    # countlist를 print와 함께 출력되게 지정
    print("총 %d 명의 회원이 저장되어 있습니다." % countlist )

    # 주소록에 저장된 모든 목록을 출력할 for문 생성. 
        # Phonebook의 key값들을 하나씩 all_key에 뽑아옴
    for all_key in Phonebook.keys():
        # 그 all_key에 뽑아진 Phonebook의 key들로 value값을 get하여 all_value에 저장
        all_value = Phonebook.get(all_key)
        # all_value에 저장된 value값들을 key로 출력
        print("회원정보 = 이름 : " + all_value.get('이름') + ", 전화번호 : " + all_value.get('전화번호') + ", 구분 : " + all_value.get('구분'))

# 회원 정보 수정하기 함수 생성
def modify(Phonebook):
    
    # key 값을 저장할 빈리스트 생성
    key_list = []

    print("수정할 회원의 이름을 입력하세요.")
    # input으로 입력 받을 값 지정
    del_name = input('이름 : ')

    # 입력받은 값이 주소록에 있는지 확인하기 위해 검색할 for문 작성
        # Phonebook의 key값들을 하나씩 all_key에 뽑아옴
    for all_key in Phonebook.keys():
        # 그 all_key에 뽑아진 Phonebook의 key들로 value값을 get하여 all_value에 저장
        all_value = Phonebook.get(all_key)

        # 입력 받은 값이 주소록에 저장된 '이름'이라는 key의 value와 같을 때 key_list에 그 key값을 순차적으로 저장
        if all_value.get('이름') == del_name:
            key_list.append(all_key)

    # 검색된 목록이 하나도 없을 경우(key_list에 저장된 요소가 하나도 없을 경우) 해당 문장 출력
    if len(key_list) == 0:
        print("해당하는 연락처가 없습니다.")
        
    # 그렇지 않으면 key_list안에 있는 요소의 개수를 문장과 함께 출력
    else :
        print('총 %d 개의 목록이 검색되었습니다.' % len(key_list))
        print('아래 목록 중 수정할 회원의 번호를 입력하세요')

        # 검색된 목록을 모두 출력할 for문 작성
            # key_list에 저장된 key값들을 sel_key에 하나씩 뽑아옴
        for sel_key in key_list:
            # 그 sel_key에 뽑아진 key 값들로 Phonebook에서 value값을 뽑아와서 sel_value에 저장
            sel_value = Phonebook.get(sel_key)

            # 출력할 때 index로 번호를 뽑기 위해 변수를 생성. sel_key의 값이 있는 위치를 key_list에서 int값으로 반환
            ind_num = int(key_list.index(sel_key))

            # 위에서 만든 변수와 sel_value에 저장된 value값들을 key로 출력
            print("%d. 회원정보 = 이름 : " % (ind_num + 1) + sel_value.get('이름') + ", 전화번호 : " + sel_value.get('전화번호') + ", 구분 : " + sel_value.get('구분'))

        # try로 오류가 났을 때 except가 출력되게 설정 (int형이 아닌 것들을 입력했을 때의 오류 해결)
        try :
            put_int = int(input())
            # 입력받은 put_int(index값)을 -1해서 실제 key_list의 index와 일치하는 요소가 Phonebook에서 삭제되게 설정
            del Phonebook[key_list[put_int-1]]

            # 수정받을 값들을 input()을 이용하여 입력할 수 있도록 생성
            name = input("이름 : ")
            telnum = input("전화번호(ex: 01012345678): ")
            sep = input("구분(ex.가족, 친구, 기타 ): ")

            print('수정이 완료 되었습니다.')

            # 안쪽 딕셔너리 생성
            inPhonebook = {'이름' : name, '전화번호' : telnum, '구분' : sep}

            # inPhonebook에 입력받은 key와 value를 각각 추가
            inPhonebook['이름'] = name
            inPhonebook['전화번호'] = telnum
            inPhonebook['구분'] = sep

            # 바깥쪽 딕셔너리 생성
            Phonebook = {telnum : inPhonebook}

        # try안에 있는 명령문을 실행하는 도중 오류가 났을 경우(int형이 아닌 것들을 입력했을 때) except의 출력되게 함
        except :
            print("목록에 없는 번호입니다.")

    # 바깥쪽 딕셔너리 리턴
    return Phonebook

# 회원 삭제 함수 생성
def delete(Phonebook):

    # key 값을 저장할 빈리스트 생성
    key_list = []

    print("삭제할 회원의 이름을 입력하세요.")
    # input으로 입력 받을 값 지정
    del_name = input('이름 : ')

    # 입력받은 값이 주소록에 있는지 확인하기 위해 검색할 for문 작성
       # Phonebook의 key값들을 하나씩 all_key에 뽑아옴
    for all_key in Phonebook.keys():
        # 그 all_key에 뽑아진 Phonebook의 key들로 value값을 get하여 all_value에 저장
        all_value = Phonebook.get(all_key)

        # 입력 받은 값이 주소록에 저장된 '이름'이라는 key의 value와 같을 때 key_list에 그 key값을 순차적으로 저장
        if all_value.get('이름') == del_name:
            key_list.append(all_key)

    # 검색된 목록이 하나도 없을 경우(key_list에 저장된 요소가 하나도 없을 경우) 해당 문장 출력
    if len(key_list) == 0:
        print("해당하는 연락처가 없습니다.")
    # 그렇지 않으면 key_list안에 있는 요소의 개수를 문장과 함께 출력
    else :
        print('총 %d 개의 목록이 검색되었습니다.' % len(key_list))
        print('아래 목록 중 삭제할 회원의 번호를 입력하세요')

        # 검색된 목록을 모두 출력할 for문 작성
            # key_list에 저장된 key값들을 sel_key에 하나씩 뽑아옴
        for sel_key in key_list:
            # 그 sel_key에 뽑아진 key 값들로 Phonebook에서 value값을 뽑아와서 sel_value에 저장
            sel_value = Phonebook.get(sel_key)

            # 출력할 때 index로 번호를 뽑기 위해 변수를 생성. sel_key의 값이 있는 위치를 key_list에서 int값으로 반환
            ind_num = int(key_list.index(sel_key))

            # 위에서 만든 변수와 sel_value에 저장된 value값들을 key로 출력
            print("%d. 회원정보 = 이름 : " % (ind_num + 1) + sel_value.get('이름') + ", 전화번호 : " + sel_value.get('전화번호') + ", 구분 : " + sel_value.get('구분'))
        
    # try로 오류가 났을 때 except가 출력되게 설정 (int형이 아닌 것들을 입력했을 때의 오류 해결)
    try :
        # input으로 int형을 입력받음
        put_int = int(input())
        # 입력받은 put_int(index값)을 -1해서 실제 key_list의 index와 일치하는 요소가 Phonebook에서 삭제되게 설정
        del Phonebook[key_list[put_int-1]]
        print('삭제가 완료 되었습니다.')

    # try안에 있는 명령문을 실행하는 도중 오류가 났을 경우(int형이 아닌 것들을 입력했을 때) except의 출력되게 함
    except :
        print("목록에 없는 번호입니다.")

# 실행 함수 생성
def run():
    # Phonebook이라는 딕셔너리 선언
    Phonebook = {}

    # 무한 반복 while문 
    while True:
        # p_menu에 만들어두었던 menu화면 입력
        p_menu = menu()

        # p_menu가 1일 때 insert 함수 실행. 주소록 값을 입력하니 update함수를 써서 다시 닥셔너리에 업데이트 해줌
        if p_menu == '1':
            p_insert = insert()
            Phonebook.update(p_insert)

        # p_menu가 2일 때 allnum 함수 실행
        elif p_menu == '2':
            allnum(Phonebook)

        # p_menu가 3일 때 modify 함수 실행. 주소록 값을 수정하여 다시 입력하니 update함수를 써서 다시 딕셔너리에 업데이트 해줌
        elif p_menu == '3':
            p_modify = modify(Phonebook)
            Phonebook.update(p_modify)

        # p_menu가 4일 때 delete 함수 실행
        elif p_menu == '4':
            delete(Phonebook)

        # p_menu가 5일 때 if while문 종료.
        elif p_menu == '5':
            print("종료되었습니다")
            break
        
        # 1부터 5까지의 값을 입력하지 않을 경우 아래 문장 출력
        else:
            print("1부터 5까지의 숫자를 입력하세요.")

# 실행
run()

```