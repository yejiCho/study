# Contact 모듈에서 main,input_contact,member_list,check_information함수를 불러온다.
# from Contact import main,input_contact,member_list,check_information
from Contact import ContactProgram
from Contact import main
import pickle
# 초기 파일load시에 빈 텍스트파일일 경우에는 에러가 발생함
# 그래서 예외처리를해줘야함
try:
    with open('contact.txt','rb') as file:
        data = pickle.load(file)
        public_info = data
except:
    pass
# main_num = 입력받을 번호 정의해줌
main_num = ''
public_info = {}
contact = ContactProgram()
while True:
    main()
    main_num = input("번호를 입력하세요. ")
    # try:
    #     main_num.isdigit()
    # except:
    #     print("1~5까지의 숫자만 입력하실수 있습니다.")
    if main_num == '1':
        private_info = contact.input_contact()
    elif main_num == '2':
        contact.member_list()
    elif main_num == '3':
        contact.check_information("수정")
    elif main_num == '4':
        contact.check_information("삭제")
    elif main_num == '5':
# 마지막에 최종으로 남은 연락처가 txt파일에 저장되게 해놓음
        with open('contact.txt','wb') as file:
            pickle.dump(public_info,file)
        print("종료합니다.")
        break
    else:
        print("없는 번호입니다. 다시입력하세요.")
