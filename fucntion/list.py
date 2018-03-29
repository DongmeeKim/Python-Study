#리스트 함수

#리스트에 값을 추가하는 함수 
li = [10,100,1000]
li.append(11)
print(li)

li.append("ab")
print(li)

li.append(['a','b'])
print(li)

#리스트 정렬 함수 : 기본적으로 오름차순 정렬
li = [1,5,2,7,10]
li.sort()
print(li)

li = ['b','a','f','c']
li.sort()
print(li)

#리스트 역으로 정렬
#sort 함수 적용 후 reverse 함수 적용하면 내림차순 리턴값이 나옴
li.reverse()
print(li)

#reverse만 적용했을 때
li = ['b','a','f','c']
li.reverse()
print(li)

#list 상에서 요소의 위치를 반환하는 함수
aa = li.index('a')
print(aa)

#aa = li.index(1)
#print(aa)

#요소를 삽입하는 함수
aa = [1,2,3,4]
aa.insert(2,5)
print(aa)

#요소를 제거하는 함수
cc = [23,12,3,6,5,3]
cc.remove(3)
print(cc) #값이 리스트 안에 여러개 있을 경우, 첫 번째 값만 삭제됨

cc.remove(3)
print(cc)

#요소를 빼내는 함수 
#pop 함수는 요소(값)을 빼내고, 빼내어진 요소는 기존 list상에서 삭제된다.

dd = [23,12,3,6,5,3]
aa = dd.pop()
print(dd)
print(aa)

bb = dd.pop(1)
print(dd)
print(bb)

#요소의 갯수를 파악하는 함수 
dd = [23,12,3,6,5,3]
cnt = dd.count(3)
print(cnt)

#리스트 확장함수
a = [1,2,3]
a.extend([2,3,4,5])
print(a)

a.extend(5,6,7,)
print(a)