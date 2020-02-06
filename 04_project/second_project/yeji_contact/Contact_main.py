
import Contact_program

num = ''
public_info = {}
while True:

    Contact_program.main()

    num = str(input("번호를 입력하세요."))

    if num == '1':

        phone_num, private_info = Contact_program.contact_program()
        public_info[phone_num] = private_info
        # print(public_info)

    elif num == '2':

        print("총 %d 명의 회원이 저장되어 있습니다." %len(public_info))

        for phone_key in public_info:
            print("이름= "+public_info[phone_key]['name'] + " 전화번호: " + public_info[phone_key]['phone_num'] +" 구분: "+ public_info[phone_key]['classification'])

    elif num == '3':
        
        print("수정할 회원의 이름을 입력하세요.")

        Contact_program.check_information(public_info)

        print("수정할 회원의 번호를 입력하세요.")

        Contact_program.del_information(public_info)

        phone_num, private_info = Contact_program.contact_program()

        public_info[phone_num] = private_info


    elif num == '4':

        print("삭제할 회원의 이름을 입력하세요.")

        Contact_program.check_information(public_info)

        print("삭제할 회원의 번호를 입력하세요.")

        Contact_program.del_information(public_info)

        print("삭제되었습니다.")

    elif num == '5':

        print("종료합니다.")
        break

    else:
        
        print("없는 번호입니다 다시입력하세요")