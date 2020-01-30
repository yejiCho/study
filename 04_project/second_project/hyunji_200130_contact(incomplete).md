```python

def mainMenu():
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
def add(aOM):
    print("%s할 회원의 정보를 입력하세요." %aOM)
    name = input("이름: ")
    cellphone = input("전화번호: ")
    sort = input("구분: ")
    personal = {"이름":name, "전화번호":cellphone, "구분":sort}
    total[cellphone] = personal

def memList():
    print("총 %d명의 회원이 저장되어 있습니다." %len(total))
    for i in total:
        print("회원정보 : 이름 = %s, 전화번호 = %s, 구분 = %s" %(total[i]["이름"], total[i]["전화번호"], total[i]["구분"]))

def delOrMod(dOM):
    print("%s할 회원의 이름을 입력하세요."%dOM) 
    name = input("이름: ")
    repeatedMember = []
    totalKeys = list(total.keys())
    for key in totalKeys:
        if name == total[key]["이름"]:
            repeatedMember.append(key)
    if repeatedMember:
        print('총 %s개의 목록이 검색되었습니다.\n다음 중 %s할 회원의 번호를 입력하세요.'%(len(repeatedMember),dOM))
        for i in range(len(repeatedMember)):
            print(i+1, ".", total[repeatedMember[i]])
        del total[repeatedMember[int(input())-1]]
                  
    else:
        print("해당하는 회원의 정보가 없습니다.")


def mod():
    delOrMod("수정")
    add("수정")
    print("수정이 완료되었습니다.")

def delMem():
    delOrMod("삭제")
    
       

mark = True
total = {}
while(mark):
    mainMenu()
    num = input()
    # total = {}
    if num == '1':
        add("등록")
        print(total)
    elif num == '2':
        memList()
    elif num == '3':
        mod()
    elif num == '4':
        delMem()
    elif num == '5':
        mark = False
    else :
        print("유효하지 않은 입력입니다. 1~5까지의 숫자를 입력해주세요.")

    


```
