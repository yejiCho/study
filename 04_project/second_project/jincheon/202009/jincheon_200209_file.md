# file.py

``` python
"""파일 입출력 관련 모듈"""
import pickle


class File(object):
    """파일 입출력 처리를 하는 클래스

    멤버 변수:
    _file -- 파일 이름

    멤버 메소드:
    get_contact_from_file() -- 파일에서 입력된 연락처 정보를 얻음
    update_contact_file() -- 파일에 연락처 정보를 저장함
    """
    _file: str

    def __init__(self, file_path: str = "temp.pickle"):
        """_file에 입력받은 파일 경로 초기화
        키워드 인수:
        file_path -- 파일 경로 (default temp.pickle)
        """
        self._file = file_path

    def get_contact_from_file(self) -> dict:
        """파일에 저장된 모든 연락처 딕셔너리를 입력받아 리턴
        파일이 존재하지 않으면 이 함수에서 파일을 생성하지는 않지만
        종료시 해당 파일을 생성하기 때문에 먼저 파일 생성 메시지 출력
        """
        all_contact = {}

        try:
            with open(self._file, 'rb') as f:
                temp_dict = pickle.load(f)
                all_contact.update(temp_dict)
        except FileNotFoundError:
            print(f"{self._file} 파일이 존재하지 않습니다.")

        return all_contact

    def update_contact_file(self, contact: dict,):
        """_file 파일에 all_contact 객체 저장
        키워드 인수:
        contact -- 파일에 저장할 딕셔너리
        """
        with open(self._file, 'wb') as f:
            pickle.dump(contact, f)
            print(f"{self._file} 파일을 생성합니다.")


```