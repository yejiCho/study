from DTO import DTO

class View:

    # 메뉴
    def main(self):
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
        menu_num = input("번호를 입력하세요.").strip()
        return menu_num


    def insert_index(self):

        print("등록할 회원의 정보를 입력하세요.")
        # number = input("번호 : ")
        name = input("이름: ").strip()
        phone_number = input("전화번호(ex:01012345678): ").strip()
        email = input("이메일주소 : ").strip()
        classification = input("구분(ex: 1)가족 2)친구 3)회사 4)기타").strip()

        dto = DTO()
        dto.name = name
        dto.phone_number = phone_number
        dto.email = email
        dto.classification = classification
        
        return dto


    def select_index(self,list_dto):
        # contact_list = [dto for dto in list_dto]

        print(f"총{len(list_dto)}명의 회원이 검색되었습니다.")
        
        for dto in list_dto:
            print(
                f" 이름:{dto.name}"
                f" 전화번호:{dto.phone_number}"
                f" 이메일:{dto.email}"
                f" 구분:{dto.classification}")


    def delete_index(self,del_list):
        # print("삭제")
        if not del_list:
            print("일치하는 이름이 없습니다.")
            return self.main()
        else:
            for i,text in enumerate(del_list):
                print(
                    f"{i+1}.\t"\
                    f"이름 : {text.name},\t"\
                    f"전화번호 : {text.phone_number},\t"\
                    f"이메일 : {text.email},\t"\
                    f"구분: {text.classification}\t")

    def input_name(self):
        return input("이름을 입력하세요. :")

    def find_index(self):
        return int(input("번호를 입력하세요."))