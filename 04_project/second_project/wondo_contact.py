
def menu():
    print(
        '''
        ==========================================
         다음 메뉴 중 하나를 입력하세요.
         =========================================
         1. 회원 추가
         2. 회원 목록 보기
         3. 회원 정보 수정하기
         4. 회원 삭제
         5. 종료
        ''')

def insert():
    print('등록할 회원의 정보를 입력하세요')
    name = input('이름 : ')
    try:
        num = int(input('전화번호(ex 01012345678): '))
    except:
         print('숫자를 입력하세요')
         return(insert())

    divlist = ['가족','친구','기타']
    div  = input('구분(ex.가족, 친구, 기타): ')
    if div not in divlist:
        print('다시 입력하세요')
        return (insert())

    all  = {'이름': name, '전화번호':num, '구분':div}

    dic[num] = all

def allprint():
    print('총 %s 명의 회원이 저장되어 있습니다.'%len(dic))
    for i in dic:
        print('회원정보 : 이름 = %s, 전화번호  : %011d, 구분 : %s'%(dic[i]['이름'] ,dic[i]['전화번호'] ,dic[i]['구분']))

def modify():
    print('수정할 회원의 이름을 입력하세요')
    name = input('이름 : \n')
    key = list(dic.keys())
    lists = []
    for key in dic:
        if name == dic[key]['이름']:
            lists.append(key)

    if lists:
        print('총 %s개의 목록이 검색되었습니다.' % len(lists))
        print('아래 목록 중 수정할 회원의 번호를 입력하세요')
    
        for i in range(len(lists)):
            print(i+1,'.','이름 = %s, 전화번호  : %011d, 구분 : %s'%(dic[lists[i]]['이름'] ,dic[lists[i]]['전화번호'] ,dic[lists[i]]['구분']) )
        for i in range(len(lists)):
            del dic[lists[int(input())-1]]
            insert()
            print('수정이 완료되었습니다.')
            break
    else:
        print('해당 이름이 없습니다.')

def dell():
    print('삭제할 회원의 이름을 입력하세요.')
    name = input('이름 : \n')
    key = list(dic.keys())
    lists = []
    for key in dic:
        if name == dic[key]['이름']:
            lists.append(key)
    if lists:
        for i in range(len(lists)):
            print(i+1,'.','이름 = %s, 전화번호  : %011d, 구분 : %s'%(dic[lists[i]]['이름'] ,dic[lists[i]]['전화번호'] ,dic[lists[i]]['구분']) )
        for i in range(len(lists)):
            del dic[lists[int(input())-1]]
            print('삭제가 되었습니다.')
            break
    else:
        print('등록회원이 없습니다.')

dic = {}
while True:
    menu()
    number = int(input())
    if number == 1:
        insert()
    elif number == 2:
        allprint()
    elif number == 3:
        modify()
    elif number == 4:
        dell()
    elif number == 5:
        break
    else:
        print('잘못된 값을 입력했습니다.')


