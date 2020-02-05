# file.py

```python
import pickle
"""파일 입출력 관련 모듈"""


def get_contact_from_file(file_name: str = "contact.txt") -> dict:
    """파일에 저장된 모든 연락처 딕셔너리를 입력받아 리턴
    파일이 존재하지 않으면 이 함수에서 파일을 생성하지는 않지만
    종료시 해당 파일을 생성하기 때문에 먼저 파일 생성 메시지 출력

    키워드 인수:
    file_name -- 파일 경로 (default contact.txt)
    """
    all_contact = dict()

    try:
        with open(file_name, 'rb') as f:
            while 1:
                try:
                    temp_dict = pickle.load(f)
                except EOFError:
                    break
                all_contact.update(temp_dict)
    except FileNotFoundError:
        print(f"{file_name} 파일이 존재하지 않습니다.\n"
              f"{file_name} 파일을 생성합니다.")

    return all_contact


def update_contact_file(contact: dict,
                        file_name: str = "contact.txt"):
    """file_name 파일에 all_contact 객체 저장
    키워드 인수:
    contact -- 파일에 저장할 딕셔너리
    file_name -- 파일 경로 (default contact.txt)
    """
    with open(file_name, 'wb') as f:
        pickle.dump(contact, f)


```