# Chapter04-2
# 파이썬 심화
# 일급 함수(일급 객체)
# Decorator & Closure

# 파이썬 변수 범위(global)

# 예제1 : 없는 변수 참조하면 에러(예외) 발생
def func_v1(a):
    print(a)
    print(b)
# func_v1(5)


# 예제2 : 전역 변수를 참조해버림
b = 10
def func_v2(a):
    print(a)
    print(b)

func_v2(5)


# 예제3 : 변수 할당 전에 참조해버림, 예외 발생 , 전역변수 참조 안해
b = 10
def func_v3(a):
    # global b
    print(a)
    print(b)
    b = 20

# func_v3(5)

# 바이트 코드대로 흐름 볼 수 있는 패키지
from dis import dis

print('EX1-1 -')
print(dis(func_v3))

print()
print()


# Closure(클로저)

a = 10

print('EX2-1 -', a + 10)
print('EX2-2 -', a + 100)

# 결과를 누적 할 수 없을까?
print('EX2-3 -', sum(range(1, 51)))
print('EX2-3 -', sum(range(51, 101)))

print()
print()


# 클로저 없이 클래스 형태로 이용
class Averager():
    def __init__(self):
        self._series = []

    def __call__(self, v):
        self._series.append(v)
        print('class >>> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)


# 인스턴스 생성

avg_cls = Averager()

# 누적 확인
print('EX3-1 -', avg_cls(15))
print('EX3-2 -', avg_cls(35))
print('EX3-3 -', avg_cls(40))

print()
print()


# 클로저(Closure) 사용 : 내부 함수에서 외부 변수 사용 가능한 것

# 반환되는 내부 함수에 대해 연결 정보를 가지고 참조하는 방식
# 반환할 때 유효범위를 넘어선 값 접근 가능
# 전역 변수 사용 감소 시키고, 디자인 패턴 적용 가능, 은닉화도 가능

def closure_avg1():
    # 클로저 영역(자유 변수 영역)
    series = []  # 리소스 낭비 우려있음

    def averager(v):
        series.append(v)
        print('def >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)

    return averager  # 내부함수만 반환해줌. averager() 이거는 실행이 되어버림!


closure1 = closure_avg1()

print('EX4-1 -', closure1(15))
print('EX4-2 -', closure1(35))
print('EX4-3 -', closure1(40))

print()
print()

# # function inspection
# print('EX5-1 -', dir(avg_closure1))
# print()
# print('EX5-2 -', dir(avg_closure1.__code__))
# print()
# print('EX5-3 -', avg_closure1.__code__.co_freevars)
# print()
# print('EX5-4 -', dir(avg_closure1.__closure__[0]))
# print()
# print('EX5-4 -', avg_closure1.__closure__[0].cell_contents)


# 잘못된 클로저 사용 예
def closure_avg2():
    cnt = 0
    total = 0

    def averager(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt

    return averager


closure2 = closure_avg2()

print('EX5-1 -', closure2(15))


# 데코레이터
# 1. 중복 제거, 코드 간결
# 2. 클로저보다 문법이 간결하다
# 3. 조합해서 사용하기 용이하다
# 단점
# 디버깅 어려움, 에러 발생 지점 추적 어려움

import time


def perf_clock(func):
    def perf_clocked(*args):
        # 시작 시간
        st = time.perf_counter()
        result = func(*args)
        # 종료 시간
        et = time.perf_counter() - st
        # 함수명
        name = func.__name__
        # 매개변수
        arg_str = ', '.join(repr(arg) for arg in args)
        # 출력
        print('[%0.9fs] %s(%s) -> %r' % (et, name, arg_str, result))
        return result
    return perf_clocked

@perf_clock
def time_func(seconds):
    time.sleep(seconds)

@perf_clock
def sum_func(*numbers):
    return sum(numbers)

@perf_clock
def fact_func(n):
    return 1 if n < 2 else n * fact_func(n-1)


# 데코레이터 미사용
# non_deco1 = perf_clock(time_func)
# non_deco2 = perf_clock(sum_func)
# non_deco3 = perf_clock(fact_func)

# print('EX7-1 -', non_deco1, non_deco1.__code__.co_freevars)
# print('EX7-2 -', non_deco2, non_deco2.__code__.co_freevars)
# print('EX7-3 -', non_deco3, non_deco3.__code__.co_freevars)

# print('*' * 40, 'Called Non Deco -> time_func')
# print('EX7-4 -')
# non_deco1(0.5)
# print('*' * 40, 'Called Non Deco -> sum_func')
# print('EX7-5 -')
# non_deco2(10, 15, 25, 30, 35)
# print('*' * 40, 'Called Non Deco -> fact_func')
# print('EX7-6 -')
# non_deco3(10)

# print()
# print()


# 데코레이터 사용
# @functools.lru_cache() -> 추가 학습 권장

print('*' * 40, 'Called Deco -> time_func')
print('EX8-1 -')
time_func(0.5)
print('*' * 40, 'Called Deco -> sum_func')
print('EX8-2 -')
sum_func(10, 15, 25, 30, 35)
print('*' * 40, 'Called Deco -> fact_func')
print('EX8-3 -')
fact_func(10)