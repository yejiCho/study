# study

스터디 진행방식 및 회고 입니다.


#### ⏱ 시간

- 학원 방과후 7:00 ~ 9:30

#### ✏️ 스터디 방식

- github을 통해 코드 공유 / 피드백

- 프로그래머스, 선생님이 공유해주신 문제 문제 풀이

- 프로젝트

### ⭐️자격증 시험 일정⭐️

- ADsP        :   2020년 02월 29일 >> 2020년04월 04일(연기)

- 정보처리기사 :   2020년 03월 22일 

- SQLD        :   2020년 03월 07일     

### 문제 사이트


> SQL : <https://programmers.co.kr/>  <br/>
        <https://www.hackerrank.com/?utm_expid=2u09ecQTSny1HV02SEVoCg.0&utm_referrer=https%3A%2F%2Fwww.google.com%2F>

# schedule

## 2020/01/20

- 1/23일 까지 개인별로 프로그래머스 SQL문제 풀어오기

- __업로드 폴더__: __practice/sql__

- 사이트 : 프로그래머스 <https://programmers.co.kr/>




### GitHub 사용법

```

--(*작업시 필수사항)

1. (master 브랜치)  git pull origin master -- 원격저장소에서 내용이 변경되었는지 pull 받아와서 수시로 확인
2. (개인 브랜치)    git pull origin (개인브랜치) -- master 브랜치 변경사항 확인후 내 브랜치에도 반영


```

```

-- 재시작 했을 경우

1. 현재 로컬저장소(개인 PC)의 repo삭제
2. 원격저장소(GitHub)에서 다시 url 복사
3. git clone url주소
4. cd study
5. git checkout -t origin/[개인 브랜치 이름] 
- 원격저장소에 각자 이름 브랜치 올려놔서 그대로 받아오면 됨
- 원격저장소에서 있는 브랜치를 로컬저장소에 가져오면서 자동으로 브랜치 변경시켜줌
6. git pull origin master - master내용 내브랜치에 반영해줘야함
7. git add .
8. git commit -m "커밋할내용"
9. git push origin [브랜치 이름]
10. pull request에서 내 요청이 보내졌는지 확인
11. merge 하지말 것 merge는 추후에 할 예정


```

## 회고록

### 파이썬 코드 작성 규칙


#### 네이밍 스타일(이름 잡기)

- 함수, 변수 이름
```
1.함수나 변수 이름은 소문자로 구성되고 언더스코어(_)로 구분
2.비슷한 이름은 피하기
3.특히! key, keys나 member, members 이렇게 두개 사용하는거 가독성 X
ex) python: contact_information
4.너무 긴 이름은 피하는게 좋음
```
- 클래스 이름
```
1. 클래스는 자바와 통일(CapWords 작성규칙)
2. 대문자 시작, 대문자 구분
3. 클래스, 예외는 풀네임을 써주는게 좋다!
ex) class ContactInformation, class GetContactError 등
```

#### 나머지 자세한 부분은 03_practice/python/coding_convention.md 참고
[파이썬코드 작성규칙](https://github.com/yejiCho/study/blob/master/03_practice/python/coding_convention.md)