# 클래스 선언방법

class Test: # 클래스명은 첫 글자를 대문자로 사용한다.
    str = "클래스 개념잡기" # str은 Test class의 요소(Attribute, field) 또는 멤버라고 말할 수 있다.

Test1 = Test() # Test1 객체는 Test class로 인해 만들어진 인스턴스이다.


# 해당 클래스의 멤버에 접근하기

print(Test1.str) # (class의 인스턴스.멤버)를 출력하면 된다.


