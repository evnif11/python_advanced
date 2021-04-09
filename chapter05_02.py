# Chapter05-2
# 파이썬 심화
# 파이썬 클래스 특별 메소드 심화 활용 및 상속
# Special Method, Class ABC

# 1.
# class 선언
class VectorP(object):
    # private 선언
    def __init__(self, x, y):
        self.__x = float(x)  # 밑줄 두개(더블 스코어) 는 변수 직접 접근 못하게 감춰두는 것
        # if y < 30:  # 생성시에만 체크 가능하고 밖에서 직접 접근해서 값을 변경하면 체크 불가능해짐.
        #     raise ValueError('under 30 is not possible')
        self.__y = float(y)

    def __iter__(self):
        return (i for i in (self.__x, self.__y))  # Generator
    # Getter (읽기)
    @property
    def x(self):
        return self.__x

    # Setter(쓰기) 데코레이터
    @x.setter
    def x(self, v):
        self.__x = v

    @property
    def y(self):
        return self.__y
    # 생성시 뿐만 아니라 직접 접근시에도 조건 거는 것이 가능.
    # 유효성 검사를 통한 더 견고한 코딩
    @y.setter
    def y(self, v):
        if v < -273:
            raise ValueError("Temperature below -273 is not possible")
        self.__y = v


# 객체 선언
v5 = VectorP(20, 40)


# print('EX1-2 -', v5.__x, v5.__y)

print('EX1-3 -',dir(v5), v5.__dict__)
print('EX1-4 -', v5.x, v5.y) # 타 언어와 달리 근본적인 해결책 X, 파이썬 개발자 간의 암묵적 약속

# Iter 확인
for v in v5:
    print('EX1-5 -', v)

print()
print()


# 2.
# __slot__
# 파이선 인터프리터에게 통보
# 해당 클래스가 가지는 속성을 제한
# __dict__은 해시 테이블 생성으로 많은 메모리 필요
# 슬롯은 Set 형태로 다수 객체 생성시 메모리 사용(공간) 대폭 감소
# 머신러닝 등에 주로 사용

# 성능 비교 (클래스 2개 선언)
class TestA(object):
    __slots__ = ('a',)


class TestB(object):
    pass


use_slot = TestA()
no_slot = TestB()


print('EX2-1 -', use_slot)
# print('EX2-2 -', use_slot.__dict__)
print('EX2-3 -', no_slot)
print('EX2-4 -', no_slot.__dict__)

use_slot.a = 10
# use_slot.b = 10


# 메모리 사용량 비교
import timeit

# 측정을 위한 함수 선언
def repeat_outer(obj):
    def repeat_inner():
        obj.a = 'test'
        del obj.a
    return repeat_inner


print('EX3-1 -', min(timeit.repeat(repeat_outer(use_slot), number=10)))
print('EX3-2 -', min(timeit.repeat(repeat_outer(no_slot), number=10)))

print()
print()


# 3.
# 객체 슬라이싱
class ObjectS:
    def __init__(self):
        self._numbers = [n for n in range(1, 10000, 3)]

    # 길이 반환
    def __len__(self):
        return len(self._numbers)

    # 객체 슬라이싱
    def __getitem__(self, idx):
        return self._numbers[idx]

s = ObjectS()

print('EX3-1 -', s.__dict__)
print('EX3-2 -', len(s._numbers))
print('EX3-3 -', len(s))
print('EX3-4 -', s[1:10])
print('EX3-5 -', s[-1])
print('EX3-6 -', s[::10])

print()
print()

# 4.
# 파이썬 추상클래스(abstract class) :
# 추상 클래스에 미리 정의된 메소드, 필드는 반드시 사용해야해.
# 상속을 통해 자식 클래스에서 인스턴스 생성 가능, 자체 생성 불가능
# 참고 : https://docs.python.org/3/library/collections.abc.html

from collections.abc import Sequence


# ex 1
# Sequence 상속 받지 않았지만, 자동으로 __iter__, __contains__ 기능 포함 시켜줌
# 객체 전체를 자동으로 조사 -> 시퀀스 프로토콜
class IterTestA():
    def __getitem__(self, idx):
        return range(1, 50, 2)[idx]  # range(1, 50, 2)


i1 = IterTestA()

print('EX4-1 -', i1[4])
print('EX4-3 -', 3 in i1[1:10])  # __contains__
print('EX4-4 -', [i for i in i1[:10]])  # __iter__

print()
print()


# ex 2
# Sequence 상속
# 요구사항인 추상메소드 모두 구현해야 동작
class IterTestB(Sequence):
    def __getitem__(self, idx):
        return range(1, 50, 2)[idx] # range(1, 50, 2)

    def __len__(self, idx):
        return len(range(1, 50, 2)[idx])


i2 = IterTestB()

print('EX4-5 -', i2[4])
# print('EX4-6 -', len(i2[:]))
print('EX4-7 -', len(i2[1:6]))

print()
print()

# ex 3
# abc(abstract class) 활용 예제
import abc


class RandomMachine(abc.ABC):
    @abc.abstractmethod
    def load(self, iterobj):
        pass

    @abc.abstractmethod
    def pick(self, iterobj):
        pass

    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
            return tuple(sorted(items))

import random

class CraneMachine(RandomMachine):
    def __init__(self, items):
        self.randomizer = random.SystemRandom()
        self.items = []
        self.load(items)

    def load(self, items):
        self.items.extend(items)
        self.randomizer.shuffle(self.items)

    def pick(self):
        try:
            return self.items.pop()
        except IndexError:
            raise LookupError('Empty box')

    def __call__(self):
        return self.pick()


# 서브 클래스 확인, 상속 구조 확인
print(issubclass(CraneMachine, RandomMachine))
print(CraneMachine.__mro__)

cm = CraneMachine(range(1, 100))
print(cm.items)
print(cm.pick())
print(cm())  # __call__
print(cm.inspect())  # 부모 클래스의 메소드 호출 가능
