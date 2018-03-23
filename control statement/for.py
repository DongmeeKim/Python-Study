#For문

#예제 1
list1 = ["a","b","c"]

for i in list1:
    print(i)

#예제 2
jumsu = [90, 50, 60, 45, 80] #1번부터 5번까지 학생의 시험 점수
number = 0

for i in jumsu:
    number = number + 1

    if i>=60:
        print("%d번 학생의 점수는 %d점이고, 합격입니다." %(number,i))
    else:
        print("%d번 학생은 점수는 %d점이고, 불합격 되었습니다." %(number,i))



number = 0 #number 변수의 값을 0으로 초기화 하는 것

 #continue문 적용
for i in jumsu:
     number = number + 1
     if i < 60 : continue
     print("%d번 학생 합격입니다." %number)


#예제 3 - 튜플을 사용한 리스트 변수
aa = [('a','b'),('c','d'),('e','f')]
for (i,j) in aa:
    print(i+j)

#for문과 range함수
for i in range(1,5):
    print(i)
else: #반복문에서 else 절은 루프를 다 돌고 난 뒤에 항상 수행된다. break문을 사용했을 경우에는 수행되지 않는다. 
    print("반복문 종료")


#이중 for문 : range함수 이용하여 구구단 출력하기
for i in range(2,10):
    for j in range(1,10):
        print("%d*%d=%d" %(i,j,i*j),end=" ")
    print(" ")


#리스트 안에 for문을 이용하여 프로그램 해보기  = 리스트 내포(List comprehension)
aa = [1,2,3,4,5,6,7,8,9]
gugudan_2 = [] #2단 구구단 만들기

for i in aa:
    gugudan_2.append(i*2)
print(gugudan_2)

#위와 동일한 출력값을 만드는 코드
gugudan_2 = [i*2 for i in aa]
print(gugudan_2)

#5단 중에서 짝수 값만 출력하기
gugudan_5 = [i*5 for i in aa if i%2 == 0]
print(gugudan_5)

#전체 구구단값 list로 출력
gugudan = [i*j for i in range(2,10)
                for j in range(1,10)]

print(gugudan)


