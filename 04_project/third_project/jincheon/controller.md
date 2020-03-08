# controller.py

```python
"""컨트롤러를 위한
추상화 클래스를 정의한 모듈
"""
from abc import *


class Controller(metaclass=ABCMeta):
    """컨트롤러 추상화 클래스

    기본기능:
    run(): 실행
    add(): 추가
    delete(): 삭제
    search(): 검색/조회
    modify(): 수정
    quit(): 종료
    """

    @abstractmethod
    def run(self):
        """실행 구현"""
        pass

    @abstractmethod
    def add(self):
        """추가 구현"""
        pass

    @abstractmethod
    def search(self):
        """검색 구현"""
        pass

    @abstractmethod
    def modify(self):
        """수정 구현"""
        pass

    @abstractmethod
    def delete(self):
        """삭제 구현"""
        pass

    @abstractmethod
    def quit(self):
        """종료 구현"""
        pass


```