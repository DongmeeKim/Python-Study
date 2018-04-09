# 상속

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("{}객체를 만드는 중".format(self.name))

    def speak(self):
        print("내 이름은 '{}' 나이는 '{}'".format(self.name,self.age))


# Person 클래스를 상속받아 Student 클래스를 만드는 방법
class Student(Person):
    def __init__(self,name,age,hakbun):
        Person. __init__(self,name,age)
        self.hakbun = hakbun
        print("{}학생 객체를 만드는 중...".format(self.name))

    def speak(self):
        Person.speak(self)
        print("나는 {:d}학번입니다.".format(self.hakbun))

# Person 클래스를 상속받아 Professor 클래스를 만드는 방법
class Professor(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self,name,age)
        self.pay = pay
        print("{}교수 객체 생성중...".format(self.name))

    def speak(self):
        Person.speak(self)
        print("페이가 {:d}인 교수".format(self.pay))


s = Student("홍길동", 15, 2017100127)

p = Professor("김교수", 38, 3000)

# speak 메소드 값을 한 번에 출력하는 경우 

member = [s,p]

for aa in member:
    aa.speak() 

# speak 메소드 값을 각각 출력하는 경우

s.speak()
p.speak()