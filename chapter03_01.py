# 시퀀스 형
# 컨테이너(Container) : list, tuple, collections.deque 서로다른 자료형
# 플랫(Flat) : str, bytes, bytearray, array.array, memoryview 한 개의 자료형 -> 퍼포먼스 훨씬 좋아

# 가변 : list, bytearray, array.array, memoryview, deque
# 불변 : tuple, str, bytes

import array

# 리스트 및 튜플 심화
# Non Comprehending Lists
chars = '!@#$%^&*()_+'
codes1 = []

for s in chars:
    # 특수문자 유니코드
    codes1.append(ord(s))

# Comprehending Lists
codes2 = [ord(s) for s in chars]

# Comprehending Lists + Map, Filter
# 속도 약간 우세
codes3 = [ord(s) for s in chars if ord(s) > 40]
codes4 = list(filter(lambda x: x > 40, map(ord, chars)))  # map은 원형형태로 넣어줘야해

# 전체 출력
print('EX1-1 -', codes1)
print('EX1-2 -', codes2)
print('EX1-3 -', codes3)
print('EX1-4 -', codes4)
print('EX1-5 -', [chr(s) for s in codes1])  # 캐릭터 형 변환
print('EX1-6 -', [chr(s) for s in codes2])
print('EX1-7 -', [chr(s) for s in codes3])
print('EX1-8 -', [chr(s) for s in codes4])

print()
print()


# Generator : 일괄 생성하지 않고 한 번에 한 개의 항목을 생성하기 때문에 성능 훨씬 좋아 (메모리에 일괄 적재 X)
tuple_g = (ord(s) for s in chars)
# Array : 하나의 자료형만 사용할 때, 앞에 자료형 써주고
array_g = array.array('I',  (ord(s) for s in chars))

print('EX2-1 -', type(tuple_g))
print('EX2-2 -', next(tuple_g))
print('EX2-3 -', type(array_g))
print('EX2-4 -', array_g.tolist())  # 리스트로 변환해서 사용 가능

print()
print()

# 제네레이터 예제
# next 나 for 문 사용하기 전까진 첫번째 값이 나오지 않아
# 실행 시점에 값을 반환하기 때문에
print('EX3-1 -', ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 11)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)):
    print('EX3-2 -', s)


print()
print()

# 리스트 주의 할 점
# 두 개 정말 다른 코딩임 !
marks1 = [['~'] * 3 for n in range(3)]
marks2 = [['~'] * 3] * 3

print('EX4-1 -', marks1)
print('EX4-2 -', marks2)

print()

# 수정
marks1[0][1] = 'X'
marks2[0][1] = 'X'

print('EX4-3 -', marks1)
print('EX4-4 -', marks2)

# 정말 많이 하는 실수..
print('EX4-5 -', [id(i) for i in marks1])
print('EX4-6 -', [id(i) for i in marks2])


# Tuple Advanced
# Unpacking

# b, a = a, b

print('EX5-1 -', divmod(100, 9))
print('EX5-2 -', divmod(*(100, 9)))  # 언팩킹돼서 인자값 하나지만 알아서 할당함
print('EX5-3 -', *(divmod(100, 9)))

print()

x, y, *rest = range(10)
print('EX5-4 -', x, y, rest)
x, y, *rest = range(2)
print('EX5-5 -', x, y, rest)
x, y, *rest = 1, 2, 3, 4, 5
print('EX5-6 -', x, y, rest)

# *args 언팩
# **args 딕셔너리 형태

print()
print()

# Mutable(가변) vs Immutable(불변)
# 깊은 복사, 얕은 복사
# 튜플은 값 변경 안되고 추가만 됨

l = (10, 15, 20)
m = [10, 15, 20]

print('EX6-1 -', l, id(l))
print('EX6-2 -', m, id(m))

# 아이디값 달라
l = l * 2
m = m * 2

print('EX6-3 -', l, id(l))
print('EX6-4 -', m, id(m))
# 리스트는 아이디값 같고
# 튜플은 아이디값 제각각 달라
l *= 2
m *= 2

print('EX6-5 -', l, id(l))
print('EX6-6 -', m, id(m))

print()
print()

# 정렬
# sort vs sorted
# reverse, key=len, key=str.lower, key=func..

f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']
# sorted() : 정렬 후 새로운 객체로 반환, 원본은 그대로임

print('EX7-1 -', sorted(f_list))
print('EX7-2 -', sorted(f_list, reverse=True))
print('EX7-3 -', sorted(f_list, key=len))  # 문자의 길이 순서대로 정렬해줌
print('EX7-4 -', sorted(f_list, key=lambda x: x[-1]))  # 문자 마지막 글자를 기준으로 정렬, 함수 받을 수 있음
print('EX7-5 -', sorted(f_list, key=lambda x: x[-1], reverse=True))
print()

print('EX7-6 -', f_list)

print()

# sort() : 정렬 후 원본 객체를 직접 변경함
# 함수 반환 값이 없음을 None으로 표현 , 값만 변경된 거라.

print('EX7-7 -', f_list.sort(), f_list)
print('EX7-8 -', f_list.sort(reverse=True), f_list)
print('EX7-9 -', f_list.sort(key=len), f_list)
print('EX7-10 -', f_list.sort(key=lambda x: x[-1]), f_list)
print('EX7-11 -', f_list.sort(key=lambda x: x[-1], reverse=True), f_list)

# List vs Array 적합 한 사용법 설명
# 리스트 기반 : 융통성, 다양한 자료형, 범용적 사용
# 숫자 기반 : 배열(리스트의 거의 모든 연산 지원)
