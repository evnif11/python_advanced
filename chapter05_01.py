# 깊은 복사 , 얕은 복사

# 얕은 복사
x = {'name': 'kim', 'age': 33, 'city': 'Seoul'}
y = x

print('EX2-1 -', id(x), id(y))
print('EX2-2 -', x == y)
print('EX2-3 -', x is y)
print('EX2-4 -', x, y)

x['class'] = 10
print('EX2-5 -', x, y)

print()
print()

z = {'name': 'kim', 'age': 33, 'city': 'Seoul', 'class': 10}

# is 로 먼저 검사해서 아이디 값이 같은지 확인 후에 == 기호로 같은지 확인해보면 선판단으로 좋음
print('EX2-6 -', id(x), id(z))
print('EX2-7 -', x is z)  # 같은 객체
print('EX2-8 -', x is not z)
print('EX2-9 -', x == z)  # 값이 같다

print()
print()

# 튜플 불변형의 비교
tuple1 = (10, 15, [100, 1000])
tuple2 = (10, 15, [100, 1000])

print('EX3-1 -', id(tuple1), id(tuple2))
print('EX3-2 -', tuple1 is tuple2)
print('EX3-3 -', tuple1 == tuple2)
print('EX3-4 -', tuple1.__eq__(tuple2))

print()
print()

# Copy, Deepcopy(깊은 복사, 얕은 복사)

# Copy , 리스트 안에 튜플은 위험하다
tl1 = [10, [100, 105], (5, 10, 15)]
tl2 = tl1
tl3 = list(tl1)

print('EX4-1 -', tl1 == tl2)
print('EX4-2 -', tl1 is tl2)
print('EX4-3 -', tl1 == tl3)
print('EX4-4 -', tl1 is tl3)

# 증명
tl1.append(1000)
tl1[1].remove(105)

print('EX4-5 -', tl1)
print('EX4-6 -', tl2)
print('EX4-7 -', tl3)

print()

# print(id(tl1[2]))
tl1[1] += [110, 120]
tl1[2] += (110, 120)

print('EX4-8 -', tl1)
print('EX4-9 -', tl2)  # 튜플 재 할당(객체 새로 생성)
print('EX4-10 -', tl3)
# print(id(tl1[2]))

print()
print()

# Deep Copy


# 장바구니
class Basket:
    def __init__(self, products=None):
        if products is None:
            self._products = []
        else:
            self._products = list(products)

    def put_prod(self, prod_name):
        self._products.append(prod_name)

    def del_prod(self, prod_name):
        self._products.remove(prod_name)


# 원본 유지하는 카피 등 유용하게 사용가능한 패키지
import copy

basket1 = Basket(['Apple', 'Bag', 'TV', 'Snack', 'Water'])
basket2 = copy.copy(basket1)
basket3 = copy.deepcopy(basket1)

# 객체 id는 다 다르지만, products id는 같음
print('EX5-1 -', id(basket1), id(basket2), id(basket3))
print('EX5-2 -', id(basket1._products), id(basket2._products), id(basket3._products))

print()


# 같이 바뀐다 *주의*
basket1.put_prod('Orange')
basket2.del_prod('Snack')

print('EX5-3 -', basket1._products)
print('EX5-4 -', basket2._products)
print('EX5-5 -', basket3._products)

print()
print()

# 함수 매개변수 전달 사용법

def mul(x, y):
    x += y
    return x

x = 10
y = 5

# 일반 데이터는 변경이 안된다
print('EX6-1 -', mul(x, y), x, y)
print()

# 리스트는 더하면 확장된다
a = [10, 100]
b = [5, 10]

# 리스트는 원본 데이터 변형
print('EX6-2 -', mul(a, b), a, b)

c = (10, 100)
d = (5, 10)

# 튜플은 원본 데이터 불변
print('EX6-2 -', mul(c, d), c, d)


# 불변형이기 때문에 참조 반환함 (사본 생성 X)
# str, bytes, frozenset, Tuple
tt1 = (1, 2, 3, 4, 5)
tt2 = tuple(tt1)
tt3 = tt1[:]

print('EX7-1 -', tt1 is tt2, id(tt1), id(tt2))
print('EX7-2 -', tt3 is tt1, id(tt3), id(tt1))

# id 값 똑같다.
# tt4 = (10, 20, 30, 40, 50)
tt5 = (10, 20, 30, 40, 50)
ss1 = 'Apple'
ss2 = 'Apple'

print('EX7-3 -', tt4 is tt5, tt4 == tt5, id(tt4), id(tt5))
print('EX7-4 -', ss1 is ss2, ss1 == ss2, id(ss1), id(ss2))
