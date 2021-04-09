# 흐름제어, 병행처리(Concurrency)
# yeild
# 코루틴(Coroutine)

# yield : 메인루틴 <-> 서브 루틴
# 코루틴 제어, 코루틴 상태, 양방향 값 전송
# yield from

# 서브루틴 : 메인루틴에서 -> 리턴에 의해 호출 부분으로 돌아와 다시 프로세스
# 코루틴 : 루틴 실행 중 멈추고 다시 원래 위치로 돌아와 수행 가능 -> 동시성 프로그래밍 가능
# 쓰레드 : 멀티쓰레드는 공유되는 자원에 대해 교착 상태 발생 가능성, 컨텍스트 스위칭 비용 발생, 자원 소비 가능성 증가

# 1.
# Coroutine
# 순차 실행이 아닌 비동기적으로 흐름제어 가능하기 때문에 동시성 프로그래밍 가능함
# 스케쥴링 오버헤드 매우 적다.

def coroutine1():
    print('>>> coroutine started.')
    i = yield  # 메인 루틴에서 값 전달해야 실행, 양방향 전송
    print('>>> coroutine received : {}'.format(i))
    yield


# 제네레이터 선언
c1 = coroutine1()

print('EX1-1 -', c1, type(c1))
next(c1)

# 값 전송
c1.send(100)

# 2. 예제
from inspect import getgeneratorstate  # 상태 값 보여주는 패키지
# GEN_CREATED : 처음 대기 상태
# GEN_RUNNING : 실행 상태
# GEN_SUSPENDED : yield 대기 상태
# GEN_CLOSED : 실행 완료 상태


def coroutine2(x):
    print('>>> coroutine started : {}'.format(x))
    y = yield x
    print('>>> coroutine received : {}'.format(y))
    z = yield x + y
    print('>>> coroutine received : {}'.format(z))


c3 = coroutine2(10)

print('EX1-2 -', getgeneratorstate(c3))
print(next(c3))

print('EX1-3 -', getgeneratorstate(c3))
print(c3.send(15))

# print(c3.send(20)) # 예외

print()
print()


# 3. next 없이 제너레이터 실행할 수 있는 데코레이터 패턴
from functools import wraps

# 클로저 형태
def coroutine(func):
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer

# 데코레이터
@coroutine
def sumer():
    total = 0
    term = 0
    while True:
        term = yield total
        total += term


su = sumer()
print('예제 ~!', su.send(20))
print('예제 ~!', su.send(100))
print('예제 ~!', su.send(50))


# 4. 예외처리, 코루틴 닫고 싶을 때
class SampleException(Exception):
    '''설명에 사용할 예외 유형'''


def coroutine_except():
    print('>> coroutine stated.')
    try:
        while True:
            try:
                x = yield
            except SampleException:
                print('-> SampleException handled. Continuing..')
            else:
                print('-> coroutine received : {}'.format(x))
    finally:
        print('-> coroutine ending')


exe_co = coroutine_except()

print('EX3-1 -', next(exe_co))
print('EX3-2 -', exe_co.send(10))
print('EX3-3 -', exe_co.send(100))
print('EX3-4 -', exe_co.throw(SampleException))  # 1) 강제 예외처리
print('EX3-5 -', exe_co.send(1000))  # 또 실행 가능
print('EX3-6 -', exe_co.close())  # 2) 아예 GEN_CLOSED

print()
print()


# 5. 마지막 리턴 값은 예외처리를 통해 출력 가능하다
def averager_re():
    total = 0.0
    cnt = 0
    avg = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        cnt += 1
        avg = total / cnt
    return 'Average : {}'.format(avg)


avger2 = averager_re()

next(avger2)

avger2.send(10)
avger2.send(30)
avger2.send(50)


try:
    avger2.send(None)
except StopIteration as e:
    print('EX4-1 -', e.value)  # 마지막 리턴 값 출력해줌


# 6. yield from (3.7 -> await)
# StopIteration 자동 처리
# 중첩 코루틴 처리

def gen1():
    for x in 'AB':
        yield x
    for y in range(1, 4):
        yield y


# 위와 같은 내용임
def gen2():
    yield from 'AB'
    yield from range(1, 4)


t3 = gen2()

print('EX6-1 -', next(t3))
print('EX6-2 -', next(t3))
print('EX6-3 -', next(t3))
print('EX6-4 -', next(t3))
print('EX6-5 -', next(t3))
# print('EX6-6 -', next(t3))


# 서브루틴
def gen3_sub():
    print('Sub coroutine.')
    x = yield 10
    print('Recv : ', str(x))
    x = yield 100
    print('Recv : ', str(x))


# 메인루틴
def gen4_main():
    yield from gen3_sub()
    # yield from gen3_sub()
    # yield from gen3_sub()
    # yield from gen3_sub()  # 여러 코루틴을 양방향 통신 가능

t5 = gen4_main()

print('EX7-1 -', next(t5))
print('EX7-2 -', t5.send(7))
print('EX7-2 -', t5.send(77))
