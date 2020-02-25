```python

# 도움 주신 분 Ye_ji,Hyun_ji


class View:

    def yeji_menu(self):
        print(
        """
        =============================
        다음 메뉴 중 하나를 선택하시YO
        =============================
        1. 회원 추가 하기
        2. 회원 목록 보기
        3. 회원 수정 하기
        4. 회원 삭제 하기
        5. 프로그램 종료
        """
        )
        hyunji = input("번호를 입력하세요")
        return hyunji

    def selman(self):
        return input("해당 메뉴의 번호를 입력해주세요. : ")

    def name(self):
        return input('이름 : ')

    def phno(self):
        return input("전화번호 : ")

    def email(self):
        return input("email : ")

    def group(self):
        return input("관계가 어떻게 되시는지 : ")

    def show_man(self,list):
        for i, dto in enumerate(list):
            print(f"회원정보 {i+1}. 이름: {dto.name}, " 
                  f"전화번호 : {dto.phno}, " 
                  f"Email : {dto.email}, "
                  f"구분 : {dto.group}")

    def receive_man(self):
        return input("번호를 입력하세요.: ")

    def end_man(self):
        print("장비를 정지 합니다.")

    def error_man(self, error):
        print(error)
```