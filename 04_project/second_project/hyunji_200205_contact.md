```python


import pickle


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

class CellPhoneError(Exception):        ## 전화번호는 문자나 기호가 들어올 수 없게 함
    def __str__(self):                  ## 등록하는 회원이 내국인이 아닐 경우를 고려해 길이 제한은 두지않음
        return "\n*전화번호는 문자나 기호를 제외한 0부터 9까지의 숫자만 입력 가능합니다."

class SortError(Exception):             ## definedSort라는 tuple내의 값만 구분으로 사용가능하게 함
    def __str__(self):
        return "\n*구분은 (가족, 친구, 회사, 기타) 내의 값만 입력 가능합니다."

class InsertNameError(Exception):
    def __str__(self):
        return "\n*이름을 입력하세요"
def picLoad():
    try:                                ## 이미 만들어진 연락처를 로드하는 경우: 연락처 파일을 total에 담음
        with open("contact.txt","rb") as contact:
            data = pickle.load(contact)
            total = data
            return total
    except FileNotFoundError as e:      ## 연락처에 아무것도 저장되어있지 않은 경우: total은 빈 딕셔너리로 선언
         total = {}
         return total    

def picWrite():         
    with open("contact.txt","wb") as contact:
        data = total
        pickle.dump(data, contact)


    
def add(aOM):
    definedSort = ("가족","친구","회사","기타")
    print(f"{aOM}할 회원의 정보를 입력하세요.")
    flag = True     
    while(flag):        ## 오류가 발생하게 되면 메인메뉴로 돌아가지 않고 등록과 수정을 마무리 해야하게 만듦.
        try:            ## 오류 발생해 메인메뉴로 돌아가게 되면 수정할 회원은 삭제만 되고 새로운 정보가 입력되지 않음.
            name = input("이름: ")
            if not name:
                raise InsertNameError()
            cellphone = input("전화번호(ex. 01012345678): ")
            if not cellphone.isdigit(): ## 전화번호에 문자나 기호가 들어올 경우 오류 발생시킴
                raise CellPhoneError()
            
            sort = input("구분(ex. 가족, 친구, 회사, 기타): ")
            if sort not in definedSort: ## definedSort 외의 값 입력시 오류 발생시킴
                raise SortError()
            
            personal = {"이름":name, "전화번호":cellphone, "구분":sort}
            total[cellphone] = personal
            print(f"{aOM}이 완료되었습니다.")

            flag = False    ## 여기까지 실행되었다는 것은 고려된 모든 예외가 발생되지 않았음을 의미. 메인으로 돌아감
        except InsertNameError as e:
            print(e)
        except CellPhoneError as e:
            print(e)
        except SortError as e:
            print(e)

 

def memList():
    print("총 %d명의 회원이 저장되어 있습니다." %len(total))
    for i in total:
        print(f'회원정보 : 이름 = {total[i]["이름"]}, '
              f'전화번호 = {total[i]["전화번호"]}, '
              f'구분 = {total[i]["구분"]}')

def delOrMod(dOM):
    print(f"\n{dOM}할 회원의 이름을 입력하세요.") 
    name = input("이름: ")
    repeatedMember = []
    totalKeys = list(total.keys())
    for key in totalKeys:
        if name == total[key]["이름"]:
            repeatedMember.append(key)
    if repeatedMember:
        try:
            print(f'\n총 {len(repeatedMember)}개의 목록이 검색되었습니다.'
                  f'\n다음 중 {dOM}할 회원의 번호를 입력하세요.\n')
            for i in range(len(repeatedMember)):
                print(f'{i+1}. '
                      f'이름 = {total[repeatedMember[i]]["이름"]}, '
                      f'전화번호 : {total[repeatedMember[i]]["전화번호"]}, '
                      f'구분 : {total[repeatedMember[i]]["구분"]}')
                    
            del total[repeatedMember[int(input())-1]]  
            if dOM == "삭제":
                print("삭제가 완료되었습니다.")       ## 삭제시에는 삭제만 하고 마무리 되지만 
            else:                                     ## 수정시에는 삭제 후 새로운 연락처 입력해야함.
                add("수정")
        except IndexError:      ## 수정할 회원의 번호가 범위를 넘을 시 해당구문 출력 후 메인메뉴로 돌아가게함
            print(f"*번호를 잘못 입력하였습니다. 검색된 회원만 {dOM}가능합니다.")
            
        except ValueError:      ## 문자나 기호 입력할 시 해당구문 출력 후 메인메뉴로 돌아가게함
            print("*주어진 번호 외의 문자나 기호는 입력할 수 없습니다.")
    else:
        print("해당하는 회원의 정보가 없습니다.\n")




total = picLoad()
mark = True
while(mark):
    mainMenu()
    num = input()

    if num == '1':
        add("등록")

    elif num == '2':
        memList()

    elif num == '3':
        delOrMod("수정")

    elif num == '4':
        delOrMod("삭제")

    elif num == '5':
        picWrite()
        mark = False

    else :
        print("유효하지 않은 입력입니다. 1~5까지의 숫자를 입력해주세요.")

    



    


```
