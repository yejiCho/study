import Contact_program
import pickle

num = ''
# public_info : 개인별 연락처 정보저장 딕셔너리
public_info = {}
# contact.txt 파일 load 
# contact.txt 파일이 empty하면 예외처리
try:
    with open('contact.txt','rb') as f:
        data = pickle.load(f)
        public_info = data
        # print(data)
except:
    pass

while True:
    Contact_program.main()

    num = input("번호를 입력하세요.")

    if num == '1':

        private_info =  Contact_program.contact_program()
        if private_info:
            public_info[private_info['phone_num']] = private_info
        else:
            print("정보가 없습니다.")

    elif num == '2':
        # 저장되어있는 회원정보 불러오기
        print("총 %d 명의 회원이 저장되어 있습니다." %len(public_info))

        for phone_key in public_info:
            print("이름= "+public_info[phone_key]['name'] + "  전화번호: " + public_info[phone_key]['phone_num'] +" 구분: "+ public_info[phone_key]['classification'])

    elif num == '3':

        print("수정할 회원의 이름을 입력하세요.")

        Contact_program.check_information(public_info)

        # print("수정할 회원의 번호를 입력하세요.")

        # Contact_program.del_information(public_info)

        private_info = Contact_program.contact_program()

        public_info[private_info['phone_num']] = private_info

        print("수정되었습니다.")

    elif num == '4':

        print("삭제할 회원의 이름을 입력하세요.")

        Contact_program.check_information(public_info)

        # print("삭제할 회원의 번호를 입력하세요.")

        # Contact_program.del_information(public_info)

        print("삭제되었습니다.")

    elif num == '5':
        # 파일에 내용저장
        with open('contact.txt','wb') as f:
            pickle.dump(public_info,f)
        print("종료합니다.")
        break

    else:

        print("없는 번호입니다 다시입력하세요")
