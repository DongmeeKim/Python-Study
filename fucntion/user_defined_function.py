# 사용자 정의 함수 
# 일반적인 함수의 구조
def show_max(a,b):
    if a > b:
        print(a, "는 최대값이다.")
    elif a == b:
        print(a,"와", b,"는 같다.")
    else:
        print(b, "는 최대값이다")

show_max(10,6)

i = 5
j = 5
show_max(i,j)

i = 10
j = 100
show_max(i,j)

def sum(a,b):
    return a + b #함수를 호출한 변수에 리턴 값으로 준다는 의미. 때문에 sum 함수에 대해서 변수 설정을 해 주어야 한다.

a = 20
b = 30
d = sum(a,b)

print(d)

# 인수가 없는 함수 (입력값이 없는 함수)
def show():
    return "Hello"

aa = show()
print(aa)

# 인수도 없고 리턴값도 없는 함수 
def show():
    print("안녕하세요")

show()

# 인수의 갯수를 예상할 수 없는 함수 
def sum(*a):
    tot = 0
    for i in a:
        tot += i
    return tot


res = sum(10,20,30)
print(res)


def cal(aa,*a):
    if aa == "sum":
        tot = 0
        for i in a:
            tot += i
    elif aa == "mul":
        tot = 1
        for i in a:
            tot *= i
    return tot

res = cal("mul",1,2,12,2)
print(res) 

#리턴 값의 유형
def return_value(a,b):
    return a+b, a-b

c = return_value(10,2)
print(c) #튜플 값으로 출력됨

#return만 단독으로 사용할 경우 함수를 바로 빠져나간다.
def  show(aa):
    if aa == 0:
        return
    else:
        print("0이 아니다")

show(1)
show(0)

# 인수에 초기값을 설정하는 방법
def show(name, age, gender = "M"): #설정하고자 하는 값은 마지막에 위치하는 것이 좋다.
    print("이름은", name)
    print("나이는", age)
    if gender == "M":
        print("남자입니다.")
    else:
        print("여자입니다")

show("홍길동", 30)
show("홍길동", 30, "F")
        