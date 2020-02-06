# 파이썬 코드 작성 규칙

```
- 네이밍 스타일(이름 잡기)
[함수, 변수 이름]
*****함수나 변수 이름은 소문자로 구성되고 언더스코어(_)로 구분
비슷한 이름은 피하는게 좋음
특히 key, keys나 member, members 이렇게 두개 사용하는거 가독성에 별로 좋지 않음
만약 연락처 정보를 받아 오는 변수를 선언한다면
(Java) contactInfromation
(Python) contact_infromation
이렇게 잡거나 더 간결하게
contact_info, cont_info 정도로 잡아주는게 좋음(너무 긴 이름은 피하는게 좋음)
함수도 마찬가지로 연락처 정보를 받아오는 함수라면
def get_contact_info() 정도로 간결하게 잡아주는게 좋음
메소드도 마찬가지

[클래스 이름]
클래스는 자바와 동일(CapWords 작성규칙)
대문자 시작, 대문자 구분
클래스는 풀네임을 써주는게 좋다. 예외 만들때도 예외도 클래스이니 동일한 규칙을 따름
ex) class ContactInformation, class GetContactError 등

[튜플, 상수 이름]
튜플과 상수는 final하기 때문에 모두 대문자로 작성하고 언더스코어로 구분
ex) FILE_NAME


- 파이썬에서 언더스코어(_)에 대하여
파이썬에서 언더스코어는 좀 특별함
더 있는데 몇가지만 설명하겠음

1. 값 무시
x, _, y = (1, 2, 3) 하면
x=1, y=3이 됨

2. 문법적 요소
private 걸때 사용
클래스에서 멤버 변수를 private하게 만들고 싶으면
변수명 맨 앞에 언더스코어를 입력
ex) _all_contact
private 메서드도 마찬가지
def _modify()로 선언하면 private 메소드가 됨
하지만 파이썬은 자바와 다르게 진정한 의미의 private은 아님
그말은 private을 강제할 수 없다는 것
직접 접근으로 가져올 수 있음
그래서 weak private이라 불림
파이썬에서 private을 걸면 해당 모듈을 import할 때 그 부분은 제외하고 import함

3. __더블 언더스코어(언더스코어 2개)는 맹글링이라고 하는데 이건 오버라이딩 안하겠다는 것을 의미
별로 쓰지는 않을듯
class A:
      def _single_method(self):
          pass

      def __double_method(self): # 맹글링을 위한 메서드
          pass

  class B(A):
      def __double_method(self): # 맹글링을 위한 메서드
          pass
print(dir(A())) # ['_A_double_method', ..., '_single_method']
print(dir(B())) # ['_A_double_method', '_B_double_method', ..., '_single_method']

4. 매직 메서드
더블언더스코어 시작 더블언더스코어 종료
__init__, __str__ 등등
이런 변수나 메서드는 모두 각 기능이 있음
직접 만들 수도 있는데 그런 경우는 거의 없음
따라서 존재하는 것들에 대해 숙지할 필요가 있음

5. 자리구분
숫자 리터럴값 자리 구분에 사용 가능
dec = 1_000_000
print(dec)
1000000


- 주석
1. 함수 주석
함수 시그니처에 쓰이며 파라미터나 리턴값의 type을 알려줌
다른 type이 들어와도 실행엔 문제가 없음
써놓으면 editor에서 알려줌.
자바의 제네릭과 비슷한데 파이썬은 강제가 아님
사용법:
def get_information(contact: dict, num: int) -> dict:
이런식으로 작성하면 contact 파라미터는 dict, num은 int로 받고
리턴값은 dict라는 표시
문자열: str, 리스트: list 등
변수에도 주석을 달 수 있음
num: int = 0
name: str = 'kim'

2. 블럭 주석, 인라인 주석 pep8 참조

3. 닥스트링(Documentation String, DocString)
"""주석""" 구성
모든 public 모듈, 함수, 클래스, 메소드에 대해 닥스트링 작성
한줄 닥스트링은 """내용"""으로 하지만 여러줄 주석은
"""내용
내용
"""
혹은
"""
내용
내용
"""
으로 작성(마지막 """은 항상 맨 아래줄에 오게 하도록)
위치는 함수 시그니처 바로 아래에 작성
블록 안의 코드와 마찬가지로 같은 위치에서 들여쓰기
내용 작성법: ex)
(1)
def function(a: str, b: int = 0) -> int:
    """어떤 기능을 하고 어떤 값을 리턴한다.

    파라미터:
    a -- 뭘 입력받는지
    b -- 뭘 입력받는지 (default 0)
    """
    코드
(2)
def function(a: str, b: int = 0) -> int:
    """어떤 기능을 한다.

    a -- 뭘 입력받는지
    b -- 뭘 입력받는지 (default 0)
    return -- 뭘 리턴하는지
    """
    코드

클래스나 메소드도 마찬가지

- 마무리
자주 쓰고 알아두면 좋을 것들 적어놨는데 이 밖에도 많이 있음
특히 띄어쓰기나 하는 부분들 많은데 링크 걸어둔 pep8 참고하길
pep257은 docstring에 대해 나오는 문서이니 이것도 참고하면 좋을 듯
함수 주석 부분은 pep484 참조. 그런데 좀 길어서 저 위에정도 알아두면 될듯
```