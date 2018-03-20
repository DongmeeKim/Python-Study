#변수 - Variable
#변수는 객체를 가리키고 있는 것. 참조변수라고 한다.

aa = 100
bb = 100

#is 파이썬 내장함수를 이용하여 aa와 bb 변수가 같은 값을 가지고 있는지 알 수 있다.
#같은 값인 경우 : true / 다른 값인 경우 : false

print(aa is bb)

cc = 100

#reference count : 객체를 가리키고 있는 변수의 갯수 (이 경우에는 aa,bb,cc 3개이다.)\


#변수 삭제하기
del(aa)

#변수 선언 및 초기화
cc=dd=100
cc,dd = "해리포터","플립"

print(cc)

#튜플형
(cc,dd) = ("aa","bb")
print(cc)

#리스트형
[cc,dd] = ["하이","파이썬"]
print(cc)
print(dd)

#데이터를 복사하는데 있어 혼동하기 쉬운 예
aa = ["a","b","c"]
bb = aa

aa[2] = "d"
print(aa)
print(bb)

#리스트의 복사
aa = ["a","b","c"]
bb = aa[:] #aa의 리스트를 처음부터 끝까지 슬라이싱

aa[2] = "d"
print(aa)
print(bb)