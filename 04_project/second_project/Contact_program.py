# 예외처리
class ContentError(Exception):
    def __str__(self):
        return "허용되지 않는 입력입니다."


# 빈값이 들어올경우 예외처리
def input_content(content):
    if content == "":
        raise ContentError()


# 회사,가족,기타,친구 아니면 예외처리 발생
def input_classification(classification,classifications):
    if classification not in classifications:
        raise ContentError()

# def input_num(num, key):
#
#     if int(renum) - 1 == (keys.index(key)):
#         del public_info[key]


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


# 1번. 연락처 정보등록
def contact_program():

    # with open('contact.txt','wb') as f:
    # 이름, 전화번호, 구분 입력받아서 양쪽 공백제거한다
    print("등록할 회원의 정보를 입력하세요.")
    name = input("이름: ").strip()
    phone_number = input("전화번호 (ex: 01012345678):").strip()
    classification = input("구분 (ex: 가족, 친구,회사, 기타):").strip()

    classifications = ['가족','친구','회사','기타']
    # 전화번호랑, 이름이 공백일경우 예외처리한다
    try:
        input_content(name)
    except ContentError as error_message:
        print(error_message)
        return {}
    try:
        input_content(phone_number)
    except ContentError as error_message:
        print(error_message)
        return {}
    # classifications안에 해당하는 값이 없으면 반환하지않는다
    try:
        input_classification(classification,classifications)
    except ContentError as error_message:
        print(error_message)
        return {}
    # 입력받은 개인정보를 private_information 딕셔너리에 저장한다
    private_information = { 'name' : name , 'phone_num' : phone_number , 'classification': classification}

    return private_information


# 2번. 해당하는 이름의 연락처 불러오기
def check_information(public_information):
    # 찾을 이름을 입력받음
    input_name = input()
    # 전화번호의 key를 list에 넣어준다
    keys = list(public_information.keys())
    list_input_name = []
    #입력받은 이름과 private_information의 이름이 같으면 list에 append해준다
    for key in keys:
        if input_name == public_information[key]['name']:
            list_input_name.append(input_name)
    # 이름이 같았던 애들의 list의 길이 많큼 출력해준다.
    print("총 %d 개의목록이 검색되었습니다." %len(list_input_name))

    # 이름이 같은 애들의 목록을 전체 조회해준다.
    for key in keys:
        if input_name == public_information[key]['name']:
            # print("총 %d 개의 목록이 검색되었습니다." % len(input_name))
            print(str(keys.index(key) + 1) + "." + "이름 = " +
                public_information[key]['name'] + "전화번호 : " + public_information[key]['phone_num'] +" 구분: "
                +public_information[key]['classification'])


    #if input_name != public_information[key]['name']:

     #   print("해당하는 회원의 정보가 없습니다.")
    
        # 숫자를 입력받는다.
    renum = input()
    # 전화번호를 list에 넣어준다.
    keys = list(public_information.keys())
    # 입력받은 숫자와 key의 인덱스 번호가 일치하면 정보를 삭제해준다.
        # print("없는번호입니다.")
        # pass
    for key in keys:
        if int(renum)-1 == (keys.index(key)):
            del public_information[key]


# # 3,4번 공통: 삭제하기
# def del_information(public_info):
#     # 숫자를 입력받는다.
#     renum = input()
#     # 전화번호를 list에 넣어준다.
#     keys = list(public_info.keys())
#     # 입력받은 숫자와 key의 인덱스 번호가 일치하면 정보를 삭제해준다.
#         # print("없는번호입니다.")
#         # pass
#     for key in keys:
#         if int(renum)-1 == (keys.index(key)):
#             del public_info[key]
#         else:
#             print("해당하는 번호가 없습니다.")
            # return {}


        # try:
        #     if int(renum) - 1 == (keys.index(key)):
        #         del public_info[key]
        # except:
        #     print("존재하는 번호가 없습니다.")
        # else:
        #     print("존재하는 번호가 없습니다.")
    # if int(renum)-1 != (keys.index(key)):
    #     print("존재하는 번호가 없습니다.")











