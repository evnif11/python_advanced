# 흐름제어, 병행처리(Concurrency)
# 제네레이터 : yield from
# 반복형 : for, collections, text file, List, Dict, Set, Tuple, unpacking, *args

# 1. for
t = 'ABCDEF'
for c in t:
    print('EX1-1 -', c)


# 2. while 사용
w = iter(t)

while True:
    try:
        print('EX1-2 -', next(w))
    except StopIteration:
        break

print()

# 3. collection 추상클래스
from collections import abc

# 반복형 확인
print('EX1-3 -', hasattr(t, '__iter__'))
print('EX1-4 -', isinstance(t, abc.Iterable))
print()
print()

# 제너레이터 없이 next로만
class WordSplitIter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        # print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stop! Stop!')
        self._idx += 1
        return word

    def __iter__(self):
        print('Called __iter__')
        return self

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)


wi = WordSplitIter('Who says the nights are for sleeping')

print('EX2-1 -', wi)
print('EX2-2 -', next(wi))
print('EX2-3 -', next(wi))
print('EX2-4 -', next(wi))
print('EX2-5 -', next(wi))
print('EX2-6 -', next(wi))
print('EX2-7 -', next(wi))
print('EX2-8 -', next(wi))
# print('EX2-9 -', next(wi))

print()
print()

# Generator 패턴
# 1.지능형 리스트, 딕셔너리, 집합 -> 데이터 셋이 증가 될 경우 메모리 사용량 증가 -> 제네레이터 완화
# 2.단위 실행 가능한 코루틴(Coroutine) 구현에 아주 중요
# 3.딕셔너리, 리스트 한 번 호출 할 때 마다 하나의 값만 리턴 -> 아주 작은 메모리 양을 필요로 함


class WordSplitGenerator():
    def __init__(self, text):
        self.text = text.split(' ')

    def __iter__(self):
        for word in self.text:
            yield word
        return

    def __repr__(self):
        return 'Word Split : {}' .format(self.text)


wg = WordSplitGenerator('Who is the sleeping beauty?')

wt = iter(wg)

print(wg)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))


# Generator 예제1
def generator_ex1():
    print('start')
    yield 'AAA'
    print('continue')
    yield 'BBB'
    print('end')


temp = iter(generator_ex1())

# print('EX4-1 -', next(temp))
# print('EX4-2 -', next(temp))

# 제너레이터는 포 문에서 진가를 발휘한다!
for v in generator_ex1():
    pass
    # print('EX4-3 -', v)

print()

# Generator 예제2

temp2 = [x * 3 for x in generator_ex1()]  # 이미 만들어서 메모리에 올림
temp3 = (x * 3 for x in generator_ex1())  # 제너레이터가 반환돼, 아직 만들지 않은 상태

print('EX5-1 -', temp2)
print('EX5-2 -', temp3)

for i in temp3:
    print('EX5-4 -', i)


# Generator 예제3(자주 사용하는 함수)
import itertools

gen1 = itertools.count(1, 2.5)

print('EX6-1 -', next(gen1))
print('EX6-2 -', next(gen1))
print('EX6-3 -', next(gen1))
print('EX6-4 -', next(gen1))
# ... 무한

print()

# 조건 동안만 반복
gen2 = itertools.takewhile(lambda n: n < 10, itertools.count(1, 2.5))  # 함수, itertools 받음
for v in gen2:
    print('ex6-5 -', v)
print()

# 필터반대 : 필터에 해당되지 않는 값만 출력
gen3 = itertools.filterfalse(lambda n: n < 3, [1, 2, 3, 4, 5])
for v in gen3:
    print('EX6-6 -', v)
print()

# 누적 합계 : 과정을 보여줌
gen4 = itertools.accumulate([x for x in range(1, 20)])
for v in gen4:
    print('EX6-7 -', v)
print()

# 연결1 : 반복 가능한 것들을 합쳐줌
gen5 = itertools.chain('ABCDE', range(1, 11, 2))
print('EX6-8 -', list(gen5))

# 연결2
gen6 = itertools.chain(enumerate('ABCDE', 1))
print('EX6-9 -', list(gen6))

# 개별로 쪼개줌
gen7 = itertools.product('ABCDE')
print('EX6-10 -', list(gen7))

# 모든 경우의 수를 조합해줌
gen8 = itertools.product('ABCDE', repeat=2)
print('EX6-11 -', list(gen8))

# 그룹화 : 정말 많은 연산이 필요하기 때문에 데이터 양을 고려하자
gen9 = itertools.groupby('AAABBCCCCDDEEE')

# print('EX6-12 -', list(gen9))

for chr, group in gen9:
    print('EX6-12 -', chr, ' : ', list(group))

print()
