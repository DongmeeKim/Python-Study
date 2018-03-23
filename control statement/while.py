#while문

aa = 0
while aa < 10:
    aa = aa + 1
    print("aa 값은 %d입니다." %aa)
    if aa == 10:
        print("종료합니다.")

#무한루프의 예
#while 1:
#    <실행할 명령문 1>
#    <실행할 명령문 2>
#    ....

#보조제어문 (break, continue)
#break문 : while문을 완료하여 빠져나갈 수 있게 해준다. 

m = 100
n = 10
while m:
    n = n - 1
    print("현재 %d 입니다." %n)

    if not n:
        print("n의 값은 0입니다.")
        break

#continue문
#1부터 10까지의 정수 중 홀수를 출력하는 코드
i = 0
while i < 10:
    i = i + 1
    if i % 2 == 0 : continue
    print(i)
