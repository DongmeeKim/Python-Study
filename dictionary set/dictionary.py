# 딕셔너리

a = {1:"Hello!!!"}
print(a)

a = {"first":['a','b','c']}
print(a)

# 특정 값을 출력하고 싶을 때

sports = {"축구":"박지성","야구":"이대호","피겨":"김연아"}
print(sports["축구"])

# 변수에 키값을 추가하는 경우 

aa = {1:"안녕"}
aa[2] = "하이"

print(aa)

aa[3] = "방가"
print(aa)

aa["인사"] = "굿모닝"
print(aa)

aa[3] = [1,2,3]
print(aa)

aa["age"] = 20
print(aa)

aa[0] = "sdf"
print(aa)


# 변수에 키값을 삭제하는 경우 
del aa[0]
print(aa)

# 딕셔너리 관련 함수 

# 딕셔너리를 생성하는 함수 : dict()
bb = dict()
print(bb)

bb["one"] = "첫번째"
print(bb)

# 딕셔너리 내의 key 리스트를 만드는 함수 : keys()
cc = {"name":"홍길동","hp":12341234,"age":20}
keylist = cc.keys()

print(keylist) #리턴값은 dict_keys 객체이다

# key를 각각 출력할 때

for key in keylist:
    print(key)

# dict_key의 객체를 list로 변환
# list()함수는 list를 생성해주는 함수

keylist1 = list(cc.keys())
print(keylist1)

# value list를 만드는 함수 : values()
valuelist = cc.values()
print(valuelist) #리턴값은 dict_values 객체이다


# key와 value 한 쌍을 얻기 : items()
item = cc.items()
print(item)

# key:value 쌍을 모두 삭제하기 : clear()
#cc.clear()
#print(cc)

# key 값을 이용하여 value를 얻어오기 : get()
age = cc.get("age")
print(age)

age = cc["age"]
print(age)

# 딕셔너리 내에 키값이 없을 경우 디폴트 값을 주는 방법
gender = bb.get('gender', '없음')
print(gender)

# 딕셔너리 내에 해당 키가 존재하는지 알아보기
confirm_a = 'gender' in cc
print(confirm_a)

# pop() 함수를 이용하여 value 값 가져오기 -> pop함수로 사용된 값은 기존 딕셔너리에서 사라진다.
m = cc.pop("name")
print(m)

print(cc) # name 키값이 사라져있다.

m = cc.pop('gender','없음') # pop함수에서 디폴트값 주는 방법
print(m)

# 딕셔너리 항목 개수 
length = len(cc)
print(length)