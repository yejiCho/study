import pickle


def main():

    prompt = """
    ===========================
    다음 메뉴 중 하나를 선택하세요.
    ============================
    1. 회원 추가
    2. 회원 목록 보기
    3. 회원 목록 수정하기
    4. 회원 삭제하기
    5. 종료하기

    """
    print(prompt)


def contact_program():

    # f =

    print("등록할 회원의 정보를 입력하세요.")
    name = str(input("이름: "))
    phone_number = str(input("전화번호 (ex: 01012345678):"))
    classification = str(input("구분 (ex: 가족, 친구, 기타):"))


    private_information = { 'name' : name , 'phone_num' : phone_number , 'classification': classification}

    return phone_number, private_information


def check_information(public_info):

    # phone_number , private_information = contact_program()
    input_name = str(input())

    keys = list(public_info.keys())
    list_input_name = []
    for key in keys:

        if input_name == public_info[key]['name']:
            list_input_name.append(input_name)

    print("총 %d 개의목록이 검색되었습니다." %len(list_input_name))

    for key in keys:

        if input_name == public_info[key]['name']:
            # print("총 %d 개의 목록이 검색되었습니다." % len(input_name))
            print(str(keys.index(key) + 1) + "." + "이름 = " +
                public_info[key]['name'] + "전화번호 : " + public_info[key]['phone_num'] +" 구분: " +public_info[key]['classification'])

    if input_name != public_info[key]['name']:

        print("해당하는 회원의 정보가 없습니다.")


def del_information(public_info):

    renum = str(input())

    keys = list(public_info.keys())

    for key in keys:

        if int(renum) - 1 == (keys.index(key)):

            del public_info[key]











