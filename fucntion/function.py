#함수 (fucntion)

#문자열 포맷팅 함수 format()
print("You've {0} a friend".format("got"))

str = "{2} {0} {1}".format("a",100,200)
print(str)

number = 100
day = "sunday"

print("오늘은 우리가 사귄지 {0}일째 되는 날이야. {1}이야.".format(number,day)) 

#인덱스와 이름을 혼용해서 사용하기 
print("오늘은 우리가 사귄지 {0}일째 되는 날이다. {day}이야".format(100,day = "sunday"))

#좌측정렬
name = "다니엘라"
print("{0:<10}".format(name))

#우측정렬
print("{0:>10}".format(name))

#가운데정렬
#예시 1
print("{0:^10}".format(name))
#예시 2
print("{0:-^20}".format(name))

#소문자를 대문자로 바꾸는 함수 
aa = "hello"
aa1 = aa.upper()

print(aa1)

#대문자를 소문자로 바꾸는 함수 : lower()

#문자의 갯수를 리턴하는 함수
aa = "abcde"
cnt = aa.count('d')

print(cnt)

#문자의 길이를 구하는 함수 
cnt = len(aa)
print(cnt)

#문자의 위치 찾기 함수 : 문자열에서 찾고자하는 문자의 첫번째 위치 리턴
bb = "cafrdifff"
loc = bb.find("f")

print(loc) # 찾고자하는 함수가 없는 경우에는 -1 값을 반환한다

#공백지우기 함수 (strip/lstrip/rstrip) 
aa = "   good   "
print(aa.lstrip()+"morning")
print(aa.rstrip()+"morning")
print(aa.strip()+"morning")

#문자열 대체함수(replace) : 문자열 내의 특정 값을 다른 값으로 교체
aa = "good morning Daniela"
print(aa.replace("morning","night")) #(바뀔 대상, 바뀐 결과값)

#문자열 나누기(split)
str = "good morning Daniela"
str_split = str.split()

print(str_split)

str = "홍길동/28/서울시 강남구/010-1234-5667"
print(str.split('/'))