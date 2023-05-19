# 함수
### 특정한 용도의 코드를 모아 놓은 것
### 코드 용도 구분 / 코드 재사용 / 실수 줄이기


## 함수 기본
### 함수 선언: def, 함수명, 파라미터, 실행코드, 반환값(여러개 가능)
### 함수 호출
### 함수 docstrings: func_name.__doc__ / help(func_name)
'''
def func_name(parameter1, parameter2, ...):
    code
    return value
func_name(argument1, ...)     
''' 


## 위치인수, 키워드 인수
### 위치인수(positional argument): 인수의 위치가 정해짐
### unpacking: 함수(*리스트), 함수(*튜플)
### 가변인수(varialbe argument): 고정인수와 함께 사용시 고정변수 먼저 사용
'''
def func_name(*args):
    for arg in args:
        code 
'''
### 키워드 인수(keyword argument): 함수(키워드=값), 함수(**딕셔너리), 순서 무관, 고정인수와 함께 사용시 고정변수 먼저 사용
'''
def func_name(**kwargs):
    for k, v in kwargs.items():
        code
'''
### 고정인수, 위치인수, 키워드인수 순서
### 매개변수 초기값 지정(우측부터 시작)
### 매개변수는 고정 인수 최대 255까지 지정


## 재귀호출(recursive call)
### python에서는 maximum recursion depth가 1,000으로 지정
### sys.getrecursionlimit(num)으로 depth 수정
### 종료조건 필수! ex) factorial


## 람다식(lambda expression) == anonymous function
### lambda 매개변수들: 식
'''
func_name = lambda arg1, arg2 : expression
func_name(arg1, arg2)
'''
### 자체 호출: (lambda 매개변수들: 식)(인수들)
### 람다식 안에서 새로운 변수 생성 불가
### 조건부 표현식: lambda 매개변수들: 식1 if 조건식 else 식2, elif는 사용 불가
'''
lambda x: str(x) if x % 3 == 9 else x
'''
### map: map(함수, 인자1, ...), 인자가 여러개일 경우, 함수의 매개변수와 개수 일치해야함
### filter: filter(함수, iterable 객체), 조건이 참인 객체만 가져옴
### reduce: import functools import reduce(함수, iterable 객체), 이전 결과와 누적해서 반환하는 함수


## 클로저
### global varialbe, global scope, local variable, local scope
### 전역 변수 선언: global 변수명
'''
x = 10
def sayNum():
    global x
    x = 20
    print(x)
sayNum()
print(x)
'''
### python에서 변수는 namespace에 저장, locals()로 확인
### 함수내 함수에서 nonlocal로 지정해야 바깥쪽 함수의 지역변수 사용 가능
### nonlocal은 가까운 함수의 지역변수부터 찾음
'''
def A():
    x = 10
    def B():
        nonlocal x
        x = 20
    B()
    print(x)
A()
'''
### closure: 함수를 둘러싼 환경을 계속 유지하다가 호출시 다시 꺼내서 사용, 값 누적 가능
'''
def calc():
    a = 10
    b = 1
    def mul_add(x):
        return a*x + b
    return mul_add
c = calc()
print(c(1))
'''