from arepl_dump import dump

#연락처 프로그램 dirtinary를 사용하여 만들어라

# 메뉴 - 연락처 생성 , 저장된 연락처 목록 , 연락처 수정 , 삭제 ,프로그램 종료 
# while 문에 전체 딕셔너리(catalog_dict)을 만들고
# if num == 1 시 연락처 추가 되는 함수 실행
# 함수 만들 시 add_dict라고 지정했으며 파라미터는 없고 
# insert_dict 라는 변수에 입력값 이름 , 연락처 , 구분이 들어가게끔 설정
# catalog_dict에 입력받은 연락처와 insert_dict를 밸류로 받는다.
# return catalog_dict로 입력받은걸 추가할 수 있게 리턴해준다.
# while문 1번조건에 변수(diction) = add_dict()를 지정하여 함수가 실행 될 수 있게끔 한다.
# update 메소드 새로운 값을 등록하면 catalog_dict에 추가할 수 있게함.

menu = """
===========================================
        연락처 프로그램 입니다.

        1. 연락처 추가
        2. 저장된 연락처 목록
        3. 연락처 삭제
        4. 연락처 수정
        5. 연락처 프로그램 종료
=========================================== 
Enter >>> """

def runtime () : # 실행구문 runtime() 지정.
    
    number = 0      # 메뉴 입력값.
    catalog_dict={} # 전체 딕셔너리

    while number <= 5 :
        try :       # 숫자 입력값에 문자열 입력시 입력값 올바르지않다고 출력.
            print(menu)
            number = int(input())
            
            if number == 1 :
                diction = add()
                catalog_dict.update(diction)        #저장된 입력값을 update 함수를 사용하여 추가해준다.
            if number == 2 :
                list_dict(catalog_dict)
            if number == 3 :
                delete_dict(catalog_dict)
            if number == 4 :
                updating = update_dict(catalog_dict) #수정된 내용을 저장하기위해 지정.
                catalog_dict.update(updating)
            if number == 5 :
                print('프로그램이 종료 됩니다.')
                break
            elif number > 6 :
                print('다시입력하세요.')
        except ValueError :
            print('입력한 값은 올바르지 않습니다.')
            print()



def add() :                         #전체 딕셔너리에 입력값을 저장하는 함수 선언

    print("저장할 이름을 입력하세요.")
    name = input('이름 : ')
    add_cotact = input('연락처 : ') 
    part = input('구분 : ')

    insert_dict={                   #작은 딕셔너리 입력값 삽입. 
        "name":name ,
        "contact" :add_cotact ,
        "part": part }

    catalog_dict = {add_cotact:insert_dict} #전체 딕셔너리에 연락처 입력값을 key로 작은 딕셔너리를 value로 지정

    return catalog_dict            #runtime에서 사용하기위해 전체 딕셔너리 return

def list_dict(catalog_dict) :

    if str(len(catalog_dict)) != 0 :

        print("저장된 연락처는 총 " + str(len(catalog_dict)) + "개 입니다.")

    else :
        print('검색된 연락처가 없습니다.')
   
    for list_contact  in catalog_dict :         #저장된 내용 출력

        print('이름 :' , catalog_dict[list_contact]['name'] ,
            ', 연락처 :' , catalog_dict[list_contact]['contact'] ,
              ', 구분 : ' , catalog_dict[list_contact]['part'] )

def delete_dict(catalog_dict) :
    
    delete = []
    print()
    name =input("삭제할 연락처의 이름을 입력하세요. \n 이름 : \n")
    num = 0

    for overlap_name in catalog_dict.keys() :               ## 카탈로그의 키를 받아와서 삭제 키(변수) 에 집어넣겠다.
        delete_values = catalog_dict.get(overlap_name)        ## 카탈로그키 안에 딜리트키를 입력받아 대응하는 value를 delete_value에 집어넣겠다.

        if delete_values.get('name') == name :              ## 만약 가져온delete_value에 'name'이라는 키가 입력값(name)과 같으면
            delete.append(overlap_name)                       ## 그것은 중복되는 키값이니 만들어놓은 delete list에 키값들을 넣어라
        
    if len(delete) == 0 :                                   ## 만약 delete list에 길익 0이면 (아무것도 없으면) = 중복되는 이름이없다.
        print('검색한 이름이 없습니다.')                     ## = 검색되는 이름이 없다.
        
    else :
        for overlap_contact in delete :                    ## 중복된 이름 출력
            
            deletevalues = catalog_dict.get(overlap_contact)
            print(num+1,'.이름 : ' , deletevalues['name'])
            print('연락처 :' , deletevalues['contact'])
            print('구분 : ' , deletevalues['part'])
            print()
            num +=1

        num = int(input('삭제할 번호를 입력하세요.'))       ## 번호를 입력받으면 catalog_dict의 키값을 가진 delete<list>의 index - 1에 해당하는 값 삭제
        del catalog_dict[delete[num-1]]


    
def update_dict(catalog_dict) :                            ##수정하는 함수
    updatename = input('수정할 연락처를 입력하세요.')

    integer = 0
    update = []
    updating_contact = {}

    for dict_update in catalog_dict.keys() :                    #전체 딕셔너리의 키값을 dict_update에 저장
        update_values = catalog_dict.get(dict_update)           #key값에 대응하는 value(작은 딕셔너리) 값을 update_value에 저장

        if update_values.get('name') == updatename :            #중복된 이름 update list에 입력.
            update.append(dict_update)

    if len(update) == 0 :                                       # 중복된 이름이 없으면 문구 출력
        print('저장된 연락처가 없습니다.')
        

    for upname in update :                                      # update list에 입력된 key 값을 upname 에 저장
        update_values = catalog_dict.get(upname)                # 전체 딕셔너리 키값에 해당하는 밸류값을 update_values에 저장

        print(integer +1,'.이름 : '                             # 중복된 이름을 가진 dict값 출력
            ,update_values['name'] ,'연락처 :'
            ,update_values['contact'],  '구분 : ' 
            ,update_values['part']
            )
        
        integer += 1

    print('수정할 연락처의 번호를 입력하세요.')
    integer = int(input())                                      #연락처앞에 번호를 입력받으면
    del catalog_dict[update[integer-1]]                         # 전체딕셔너리의 키값을 가진 (update <list>의 인덱스 -1)에 해당하는 키값 삭제


    print('수정 정보를 입력하세요.')                             # 수정값 입력 후 전체 딕셔너리에 저장
    uname = input('이름 : ')
    contact = input('연락처 : ')
    upart = input('구분 : ')

    updating_contact = {'name' : uname , 'contact' : contact , 'part' : upart}

    catalog_dict = {contact:updating_contact}

    return catalog_dict #추가가 되면 return catalog_dict을 리턴하면 수정된 객체가 밖으로 나감 => update를해줘서 새로 반영한다.


runtime()





