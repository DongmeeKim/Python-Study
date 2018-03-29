# 변수의 스코프 (Scope)
a = 20 #전역 변수(Global)

def func(a): #매개변수(인수) = 지역 변수
    print("a는 ",a)
    a = 10 #지역 변수
    print("로컬 변수 a는 ", a)
 
func(10)
print(a)



def func1(b):
    b = b + 1
    print(b)

func1(20)
#print(b) Global 변수가 없기 때문에 출력값은 없음 


#전역 변수
#return 함수를 사용하는 예
aa = 10

def aa_func(aa):
    aa = aa + 1
    return aa

aa = aa_func(aa) #함수 밖에서 선언된 변수의 값을 변경시키는 예 (return 함수 사용)
print(aa) 


#global 함수를 사용하는 예 (가능하면 global문은 사용하지 않는 것이 바람직하다) - 참고만 하기 
bb = 100

def bb_func():
    global bb #global은 함수 안에서 함수 밖의 변수를 직접 사용하겠다는 의미 
    bb = bb + 1

bb_func()
print(bb)