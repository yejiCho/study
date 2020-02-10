# 전화번호에 문자나 기호가 들어가는 경우
# 수정이나 삭제할 회원에서 번호를 매겼을 때, 입력받은 번호 값이 범위를 넘는 경우
# 수정할 시 삭제 후 contact_program함수를 다시 실행하는 것으로 보이는데
# 이 때 오류 발생시 삭제만 되고 메인메뉴로 돌아가짐
# if hyun: 삭제만 되고 메인메뉴로 돌아가짐
# while문 써서 수정 후 등록할 때 이름이나 연락처나 구분에 오류가 생기면
# 반드시 다시 입력하게끔 해놓음
# 예외처리
class ContentError(Exception):
    def __str__(self):
        return "허용되지 않는 입력입니다."
def input_content(content):
    if content == "":
        raise ContentError()
def input_classification(classification,classifications):
    if classification not in classifications:
        raise ContentError()
# class NumError(Exception):
#     def __str__(self):
#         return "숫자 1~5번만 입력하실 수 있습니다."
# def input_num(self,num):
#     if num.isdigit() is False:
#         raise NumError()

# 메뉴
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
def input_contact(public_information):
    print("등록할 회원의 정보를 입력하세요.")
    name = input("이름: ").strip()
    try:
        input_content(name)
    except ContentError as error_message:
        print(error_message)
        return {}
    phone_number = input("전화번호(ex:01012345678): ").strip()
    try:
        input_content(phone_number)
    except ContentError as error_message:
        print(error_message)
        return {}
    classification = input("구분(ex:가족,친구,회사,기타):").strip()
    classifications = ("가족","친구","회사","기타")

    try:
        input_classification(classification, classifications)
    except ContentError as error_message:
        print(error_message)
        return {}

    private_information = {
        'name':name,
        'phone_number':phone_number,
        'classification':classification
    }
    if private_information:
        public_information[private_information['phone_number']] = private_information
    else:
        print("정보가 없습니다.")
    # return public_information
    
    return private_information


# 2번. 연락처 목록조회
def member_list(public_information):

    print(f"총 {len(public_information)}명의 회원이 저장되어 있습니다.")
    for phone_key in public_information.keys():
        # print(phone_key)
        print(f"이름={public_information[phone_key]['name']},"
                f"전화번호={public_information[phone_key]['phone_number']},"
                f"구분={public_information[phone_key]['classification']}")


# 3,4번. 수정,삭제
def check_information(public_information,correct_comment):

    input_name = input(f"{correct_comment}이름을 입력하세요.")

    keys = list(public_information.keys())
    list_input_name = []
    for key in keys:
        if input_name == public_information[key]['name']:
            list_input_name.append(key)
    print(f'총{len(list_input_name)}개의 목록이 검색되었습니다.')
    # 이름이 같은 애들의 목록을 전체 조회해준다.
    for key in keys:
        if input_name == public_information[key]['name']:
            print(f"{str(keys.index(key)+1)}."
                f"이름={public_information[key]['name']},"
                f"전화번호={public_information[key]['phone_number']},"
                f"구분={public_information[key]['classification']}")
            print(key)

    input_num = input(f"{correct_comment}할 번호를 입력하세요")
    del public_information[list_input_name[int(input_num)-1]]
    # print(public_information)

    if correct_comment == "삭제":
        print(f"{correct_comment}가 완료되었습니다.")
    else:
        input_contact(public_information)
        print(f"{correct_comment}이 완료되었습니다.")