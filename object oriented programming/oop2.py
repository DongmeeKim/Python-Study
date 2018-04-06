# class 내의 메소드와 일반 함수의 차이점 : Self 인자 사용 유무

class Person:
    def say(self):
        print("Hello my friend")


p1 = Person()
p1.say() # self 대입값을 전달하지 않았음에도 에러 없이 출력 가능


#객체화 하는 과정

class Person1:
    pass

p2 = Person1()
print(p2) # 결과 값으로 메모리 주소가 출력된다. 객체화 되었다는 뜻.


# init 메소드

class Person3:
    def __init__(self,name):
        self.name = name # init 함수 내의 필드(self.name) = name 매개변수
    def say(self):
        print("My name is", self.name)


p3 = Person3("Daniela") # Person3 class를 객체화하면 자동으로 init 메소드를 실행함. 여기에 매개변수 입력해 줘야함.

p3.say() # say 메소드에는 self인자만 지정되어 있기 때문에, 매개변수 입력X



