class Contact:
    pass
def run():
    person_list = []
    while 1:
        menu = mainmenu()
        if menu == 0:
            pass
            print("1 ~ 5 번만 입력하세요")
        elif menu == 1:
            add_contact()
        elif menu == 2:
            print_contact()
        elif menu == 3:
            update_contact()
            add_contact()
        elif menu == 4:
            delete_contact()
        elif menu == 5 :
            print("종료")
            break
        else:
            print("1 ~ 5 번만 입력하세요")

def mainmenu():
    print("""
    =====================================
        다음 메뉴 중 하나를 선택하세요.
    =====================================
    1. 회원 추가
    2. 회원 목록 보기
    3. 회원 정보 수정하기
    4. 회원 삭제
    5. 종료
    """)
    try:
        menu = int(input(" choose : "))
    except:
        print("숫자만 입력하세요")
        menu = int(input(" choose : "))
    return int(menu)

def add_contact():
    name = input("이름 : ")
    phone_number = input("전화번호 : ")
    division_list = ['가족', '친구', '회사', '기타']
    division = input("구분(ex: 가족, 친구, 회사, 기타) : ")
    if division not in division_list:
        print("가족, 친구, 회사, 기타 만 입력 가능 합니다.")
        return add_contact()
    person = {"이름": name, "전화번호": phone_number, "구분": division}
    phone_book[phone_number] = person

def print_contact():
    print("총 %d명의 회원이 저장되어 있습니다." %len(phone_book))
    for i in phone_book :
        print("회원정보 : 이름 = %s, 전화번호 = %s, 구분 = %s" %(phone_book[i]["이름"], phone_book[i]["전화번호"], phone_book[i]["구분"]))

def update_contact():
    print("수정할 회원의 이름을 입력하세요" )
    name = input("이름 : \n")
    del_name = []
    check_name = list(phone_book.keys())
    for key in phone_book:
        if name == phone_book[key]["이름"]:
            del_name.append(key)
    if del_name:
        print("총 %s 개의 목록이 검색되었습니다. 수정할 회원의 번호를 입력하세요" % (len(del_name)))
        for i in range(len(del_name)):
            print(i + 1, ".", phone_book[del_name[i]])
        del phone_book[del_name[int(input())-1]]
    else:
        print("해당 없음")

def delete_contact():
    print("삭제할 회원의 이름을 입력하세요")
    name = input("이름 : \n")
    del_name = []
    check_name = list(phone_book.keys())
    for key in phone_book:
        if name == phone_book[key]["이름"]:
            del_name.append(key)
    if del_name:
        print("총 %s 개의 목록이 검색되었습니다. 삭제할 회원의 번호를 입력하세요" % (len(del_name)))
        for i in range(len(del_name)):
            print(i + 1, ".", phone_book[del_name[i]])
        del phone_book[del_name[int(input()) - 1]]
    else:
        print("해당 없음")

phone_book = {}
try:
    run()
except:
    pass
