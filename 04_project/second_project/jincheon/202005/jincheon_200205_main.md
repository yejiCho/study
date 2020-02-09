# main.py

```python
from file import get_contact_from_file
from file import update_contact_file

from contact import get_menu
from contact import input_one_contact
from contact import Contact
"""연락처 프로그램을 실행하는 main 모듈"""

# 파일에서 연락처 불러오기
FILE_NAME = 'contact.txt'
file_contact = get_contact_from_file(FILE_NAME)

# 파일에서 불러온 연락처 딕셔너리를
# Contact 클래스 멤버변수에 저장
contact = Contact()
contact.set_all_contact(file_contact)

while 1:
    menu_num = get_menu()

    if not menu_num:
        # 입력값 오류(menu_num=0)
        print("1~5 사이의 숫자를 입력하세요.")
    elif menu_num == 1:
        # 연락처 추가
        print("등록할 연락처의 정보를 입력하세요.")
        input_contact = input_one_contact()
        if contact.add_contact(input_contact):
            print("연락처 추가가 완료되었습니다.")
        else:
            print("연락처 추가를 실패했습니다.")
    elif menu_num == 2:
        # 연락처 목록 보기
        contact.print_all_contact()
    elif menu_num == 3:
        # 연락처 정보 수정하기
        contact.edit_contact('수정')
    elif menu_num == 4:
        # 연락처 삭제
        contact.edit_contact('삭제')
    elif menu_num == 5:
        # 종료(종료시 파일에 변경된 내용 저장)
        save_contact = contact.get_all_contact()
        update_contact_file(save_contact, FILE_NAME)
        print("종료되었습니다.")
        break


```