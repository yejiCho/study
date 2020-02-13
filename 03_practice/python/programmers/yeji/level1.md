# [프로그래머스 - 문자열 다루기 기본](https://programmers.co.kr/learn/courses/30/lessons/12918)

```python

# testcase 7 실패

def solution(s):
    answer = True
    ss = ['1','2','3','4','5','6','7','8','9','0']
    sss = []
    s = list(s)
    for i in s:
        if i not in ss:
            del i
        else:
            sss.append(i)
            
    # print(sss)
               
    if len(sss) == 4 or len(sss) == 6 :
        
        return answer
    
    else:
        
        return False
    
    
# .isdigit()
# 문자열이 숫자인지 아닌지를 True, False로 리턴해줌
# isalpha()
# 문자열이 문자인지 아닌지를 True, False로 리턴해줌


def solution(s):

    return s.isdigit() and (len(s) == 4 or len(s) == 6)


# try/except
# 파이썬으로 프로그래밍 중에 다양한 에러가 발생할 수 있다.
# 이 에러가 발생하는 예외상황은 유연하게 프로그래밍을 할 수 있는 도구가 되기도 한다.

# VlaueError, IndexError, ImportError

def solution(s):
    
    if len(s) == 4 or len(s) == 6:
        try:
            int(s)
        except ValueError: 
            result = False
        else:
            result = True
            
    else:
        result = False
    return result

```

# [프로그래머스-문자열 정수로 바꾸기](https://programmers.co.kr/learn/courses/30/lessons/12925)


```python
#(+,-) int형으로 취급가능

def solution(s):
    answer = int(s)

    return answer

# 다른사람 풀이 1

def strToInt(str):
    result = 0

    int(str)
    return int(str)

# test
print(strToInt("-1234"))

# 다른사람 풀이 2
    # str[::-1]: 주어진 스트링을 거꾸로 만듦
    # enumerate :한 글자당 인덱스를 배정해서 각 자리의 10의 지수만큼 곱해서 더해줌
    # "-1234" str[::-1] -> "4321-"
    #  4 * (10 ** 0) + 3 * (10 ** 1) + 2 * (10 **2) + 1 * (10 ** 3)를 한 이후에 "-" 는 이 숫자를 마이너스로 만들어 버립니다.
def strToInt(str):
    result = 0

    for idx, number in enumerate(str[::-1]):

        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)

    return result


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(strToInt("-1234"));

```
# [문자열 내 p와 y의 개수](https://programmers.co.kr/learn/courses/30/lessons/12916)

```python

def solution(s):
    answer = True
    p_list = []
    y_list = []
    for i in s:
        if i == 'p':
            p_list.append(i)
        elif i == 'P':
            p_list.append(i)
        elif i == 'y':
            y_list.append(i)
        elif i == 'Y':
            y_list.append(i)
    if len(p_list) == len(y_list):
        return True
    else:
        return False
    # print(p_list)
    # print(y_list)

# 다른사람풀이

def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( numPY("pPoooyY") )
print( numPY("Pyy") )


```

# [프로그래머스 - 가운데 글자 가져오기](https://programmers.co.kr/learn/courses/30/lessons/12903)


```python

def solution(s):
    answer = ''
    mok = len(s)/2
    mok = int(mok)
    if len(s) % 2 == 0:
        answer = s[mok-1:mok+1]
    else:
        answer = s[mok]
    return answer


# 다른사람 풀이

# /  : 나누기
# // : 몫
def string_middle(str):

    return str[(len(str)-1)//2:len(str)//2+1]


print(string_middle("power"))
```

# [프로그래머스 - 문자열 내 마음대로 정렬하기](https://programmers.co.kr/learn/courses/30/lessons/12915)


```python

# 1차실패

def solution(strings, n):
    answer = []
    answers = []
    # for i,list_string in enumerate(strings):
    #     print(i,list_string)
    for i,list_string in enumerate(strings):
        answers.append(strings[i][n])
        answers.sort()
        if strings[i][n] == answers[n]:
            answer.append(list_string)
    print(answers)
    print(answer)
    return answer


```


# [프로그래머스 - 서울에서 김서방 찾기](https://programmers.co.kr/learn/courses/30/lessons/12919)

```python

def solution(seoul):
    answer = ''
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            answer = f'김서방은 {i}에 있다'
    return answer

# 다른사람풀이
# index : 'kim'있는 index위치 반환
def solution(seoul):

    return "김서방은 {}에 있다".format(seoul.index('Kim'))

print(solution(['Jane','Kim']))

# 응용
def solution(seoul):

    return f"김서방은 {seoul.index('Kim')}에 있다"

print(solution(['Jane','Kim']))

```

# [프로그래머스 - 나누어 떨어지는 숫자배열](https://programmers.co.kr/learn/courses/30/lessons/12910)

```python

def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
            answer.sort()
    if answer == []: return [-1]
    return answer

```

# [프로그래머스 - 같은숫자는 싫어](https://programmers.co.kr/learn/courses/30/lessons/12906)

```python

def solution(arr):
    answer = []                # 빈 리스트 생성
    for i in arr:              # arr안의 성분을 하나씩 돌면서
        if answer[-1:] == [i]: # 마지막 원소와 i가 같으면
            continue           # continue를 
        else:                  # 마지막 원소와 i가 다르면 answer에 i를 넣어준다.
            answer.append(i)
    return answer


# 다른 사람 풀이
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a

print(no_continuos("133303"))

```

# [프로그래머스 - 하샤드 수](https://programmers.co.kr/learn/courses/30/lessons/12947)


```python

# 첫번째 시도
# x가 1이상, 1000이하인 정수인 제한조건을 확인 못함
def solution(x):
    answer = True
    a = x // 10
    b = x % 10
    if x % (a+b) == 0: return answer
    else: return False
    # return answer if x % (a+b) == 0 return False

```

# [프로그래머스 - 하샤드 수](https://programmers.co.kr/learn/courses/30/lessons/12947)

```python

def solution(x):
    answer = True
    x = str(x)
    a = 0
    for i in range(len(x)):
        a = a + int(x[i])
    if int(x) % a == 0: return answer
    else: return False

# 다른사람풀이

def Harshad(n):
    return n % sum([int(c) for c in str(n)]) == 0

```

# [프로그래머스 - 2016년](https://programmers.co.kr/learn/courses/30/lessons/12901)


```python
# datetime 모듈
# datetime 패키지 에서는 날짜와 시간을 함께 저장하는 datetime클래스
# 날짜만 저장하는 date클래스, 시간만 저장하는 time클래스
# 시간 구간 정보를 저장하는 timedelta클래스 등을 제공
# 날짜만을 관리할때 : datetime.date
# d = datetime.date(2015,4,15)
# weekday():요일 반환(0:월,1:화,2:수,3:목,4:금,5:토,6:일)
import datetime
def solution(a, b):

    return ['MON','TUE','WED','THU','FRI','SAT','SUN'][datetime.date(2016,a,b).weekday()]

# print(datetime.date(2016,a,b).weekday()) => 1
# print(datetime.date(2016,a,b)) => 2016-05-24
```

# [프로그래머스 - 문자열 내림차순으로 배치하기]()

```python
def solution(s):
    answers = []
    answer = []
    for i in range(len(sorted(s))):
        if s[i].isupper():
            answers.append(s[i])
        else:
            answer.append(s[i])
    return "".join(sorted(answer, reverse=True) + sorted(answers,reverse=True))

def solution(s):
    
    return "".join(sorted(list(s),reverse = True))

# testcase
print(solution('Zbcdefg'))
print(solution('ZdksnFdkAfj'))
print(solution('AacBDdBCeWdD'))
# output    "gfebdcZ"
# output    "snkkjfddZFA"
# output    "eddcaWDDCBBA"

```

# [프로그래머스 - 문자열 내 마음대로 정렬하기](https://programmers.co.kr/learn/courses/30/lessons/12915)

```python
# operator 모듈 함수
# itemgetter(), attrgetter()및 mathodcaller()함수가 존재
from operator import itemgetter
def solution(strings, n):
    
    strings.sort()
    return sorted(strings, key=itemgetter(n))

# shotcoding
from operator import itemgetter
def solution(strings, n):
    
    return sorted(sorted(strings), key=itemgetter(n))

# 다른사람풀이
def strange_sort(strings, n):

    return sorted(strings, key=lambda x:x[n])
# print
strings = ["sun","bed","car"]
print(strange_sort(strings, 1))

```

# [프로그래머스 - 제일 작은 수 제거하기](https://programmers.co.kr/learn/courses/30/lessons/12935)

```python
# 1차 실패
# arr가 비어있거다 [10]일경우 answer에 -1 append함
# 아닐경우에는 arr역순으로 정렬해서 마지막값 제외하고 return
def solution(arr):
    answer = []
    if not arr or arr[0] == 10:
        answer.append(-1)
    else:
        answer = sorted(arr, reverse=True)[0:-1]
    return answer

```

# [프로그래머스 - x만큼 간격이 있는 n개의 숫자](https://programmers.co.kr/learn/courses/30/lessons/12954)


```python

def solution(x, n):

    return [x * (i+1) for i in range(n)]

# 다른사람 풀이1
def number_generator(x,n):

    return [i*x+x for i in range(n)]

print(number_generator(2,5))

# 다른사람 풀이2
def number_generator(x,n):

    return [i for i in range(x, x*n+1, x)]

print(number_generator(2,5))

```

# [프로그래머스 - 제일 작은 수 제거하기](https://programmers.co.kr/learn/courses/30/lessons/12935)


```python

def solution(arr):
    if arr[0] == 10 or []:
        return [-1]
    else:
        del arr[arr.index(min(arr))]
        return arr

# 다른사람풀이
def rm_small(mylist):
    return  [i for i in mylist if i > min(mylist)]
    #  제일 작은 수 보다 큰 것들은 return

```

# [프로그래머스 - 정수 제곱근 판별](https://programmers.co.kr/learn/courses/30/lessons/12934)

```python

import math
def solution(n):
    sqrt_n = int(math.sqrt(n))
    if n == sqrt_n**2:
        return  (sqrt_n+1)**2
    else:
        return -1

# shotcoding
import math
def solution(n):
    sqrt_n = int(math.sqrt(n))

    return (sqrt_n+1)**2 if n == sqrt_n**2 else -1
    
    
```

# [프로그래머스 - 최대공약수와 최소공배수](https://programmers.co.kr/learn/courses/30/lessons/12940)

```python

import math
def solution(n, m):

    return [math.gcd(n,m), n*m//math.gcd(n,m)]

#  다른사람풀이
#  유클리드 호제법

def gcdlcm(a,b):
    c,d = max(a,b), min(a,b)
    t = 1
    while t > 0:
        t = c % d
        c,d = d,b
    answer = [c, int(a*b/c)]

    return answer

print(gcdlcm(3,12))

```