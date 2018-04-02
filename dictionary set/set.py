# 집합 (Sets)

ss = set(['a','b','c'])
print(ss)

ss = set([1,2,3])
print(ss)

ss = set("Good Morning")
print(ss)

# 집합을 인덱싱하기 -> list 사용
ss1 = set([1,2,3])
li = list(ss1)

print(li[2])

# 교집합, 합집합, 차집합

s1 = set([1,2,3,4,5,6,7])
s2 = set([3,5,6,8,9])

# 교집합 : &

print(s1 & s2)

# 합집합 :| or .union()

print(s1 | s2)
print(s1.union(s2))

# 차집합 : - or .difference()

print(s1-s2)
print(s1.difference(s2))

# 집합에 값을 추가하기
# 1개 일 때 : .add()

s1 = set([1,3,4])
s1.add(100)
print(s1)

# 여러개를 동시에 추가할 때 : .update()

s1 = set([1,2,3,4])
s1.update([10,100,1000])
print(s1)

# 집합에서 값을 삭제하기 : .remove() / .discard()
# .remove() : 집합 내에 없는 요소를 제거요청하면 에러 메세지가 뜸
s1 = set([1,2,3,4,5])
s1.remove(5)
print(s1)

# .discard() : 집합 내에 없는 요소를 제거요청해도 에러가 뜨지 않음

s1.discard(6)
s1.discard(2)
print(s1)

# 대칭차집합 : ^
# 두 집합이 있을 때, 둘 중 한 집합에만 있는 요소(항목)을 나타냄

s = set("Good Morning")
t = set("Good Night")
print(s ^ t)

# 집합 내 요소의 개수를 구하는 방법 : len()

length = len(t)
print(length)
