# 클래스 변수와 객체 변수의 예

class Man:
    # 클래스 변수 (메소드 밖에 선언되었음)
    cnt = 0 

    def __init__(self, name): # 이 line의 name은 매개변수
        # 데이터 초기화 하기
        self.name = name # self.name에서 name은 객체변수 (메소드 내에 선언)
        print("(초기화 중...{})".format(self.name))

        # 클래스 변수의 접근
        Man.cnt += 1

    def die(self):
        # Man 객체가 죽었을 때
        print("{}는 죽었습니다!!".format(self.name))

        Man.cnt -= 1

        if Man.cnt == 0:
            print("{}는 최후의 생존자였다.".format(self.name))
        else:
            print("아직 {:d}명의 생존자가 남아있다.".format(Man.cnt))

    def say(self):
        print("안녕하세요. 제 이름은 {}입니다.".format(self.name))


# 클래스 매소드 선언하기
    @classmethod
    def how_many(self):
        # 현재 객체 수량 체크
        print("현재 {}명이 남아있습니다!!".format(Man.cnt))

gameActor1 = Man("맨1")
gameActor1.say()

Man.how_many()

gameActor2 = Man("맨2")
gameActor2.say()

Man.how_many()


gameActor2.die()
Man.how_many()