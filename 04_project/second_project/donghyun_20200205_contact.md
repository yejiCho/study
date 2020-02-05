# contact.py

``` python

prompt = '''
============================
다음 메뉴 중 하나를 선택하세요.
============================
1. 회원 추가
2. 회원 목록 보기
3. 회원 정보 수정하기
4. 회원 삭제
5. 종료
'''
MenuNumber = 0
members = {}
while MenuNumber <= 5:
    print(prompt)
    MenuNumber = int(input())
    if MenuNumber > 5:
        print("1~5 사이의 숫자를 입력해주세요. 프로그램이 종료 됩니다.")

    if MenuNumber == 1:
        member = {}
        print("등록할 회원의 정보를 입력하세요.")
        print("주의 : 중복 되는 전화번호 입력시 가장 최근에 입력된 번호만 저장됩니다.")

        member["이름"] = input("이름: ")
        pn = int(input("전화번호(ex: 01012345678) : "))
        member["전화번호"] = pn
        member["구분"] = input("구분(ex: 가족, 친구, 기타) : ")
        members[pn] = member

    if MenuNumber == 2:
        print("총 %d 명의 회원이 저장되어 있습니다." % len(members))
        for lists in members:
            print("이름: %s, 전화번호: %s, 구분: %s" % (members[lists]["이름"], members[lists]["전화번호"], members[lists]["구분"]))

# 도움 주신 분들 yeji, jinchun
    if MenuNumber == 3:
        member = {}
        print("수정할 회원의 이름을 입력하세요.")
        YjNm = input("이름: ")
        YjList = []
        for key, value in members.items():
            if YjNm == value["이름"]:
                YjList.append(key)
        for Jc in YjList:
            i = YjList.index(Jc)
            print(i+1, "이름: %s, 전화번호: %s, 구분: %s" % (members[Jc]["이름"], members[Jc]["전화번호"], members[Jc]["구분"]))
        IDN = int(input("수정 할 회원의 번호를 선택해 주세요."))
        del members[YjList[IDN-1]]

        print("새로 등록할 회원의 정보를 입력하세요.")
        print("주의 : 중복 되는 전화번호 입력시 가장 최근에 입력된 번호만 저장됩니다.")

        member["이름"] = input("이름: ")
        pn = int(input("전화번호(ex 01012345678): "))
        member["전화번호"] = pn
        member["구분"] = input("구분(ex 가족, 친구, 기타): ")
        members[pn] = member

# 도움 주신분 hunji
    if MenuNumber == 4:
        print("삭제 할 회원의 이름을 입력하세요.")
        HjNm = input("이름: ")
        HjList = []
        for key, value in members.items():
            if HjNm == value["이름"]:
                HjList.append(key)
        for Jc in HjList:
            i = HjList.index(Jc)
            print(i+1, "이름: %s, 전화번호: %s, 구분: %s" % (members[Jc]["이름"], members[Jc]["전화번호"], members[Jc]["구분"]))
        IDN = int(input("삭제 할 회원의 번호를 선택해 주세요."))
        del members[HjList[IDN-1]]

    if MenuNumber == 5:
        print("종료되었습니다.")
        break


```