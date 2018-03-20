#문자열 포맷팅/ 포맷코드의 기능
aa = "ABCD"
print(aa[1]) 

#aa[1] = "F"
#print(aa[1]) -> 에러발생

aa[:1]
print(aa[:1]) 
print(aa[2:])

aa = aa[:1] + "F" + aa[2:]
print(aa)

#문자열 포맷팅
#숫자 대입 방법
print("제 나이는 %d살 입니다." %2)
print("제 나이는 %d살 입니다." %21)

#문자열 대입 방버법
print("제 이름은 %s 입니다" %"김동미")
print("제 이름은 %s 입니다" %"홍길동")

#숫자형 변수로 대입하기
age = 22
print("제 나이는 %d살 입니다" %age)

#여러 개의 값을 대입하기
name = "김동미"
age = 27
print("저의 이름은 %s 입니다. 나이는 %d살 입니다." %(name, age))

#포멧 코드
print("%0.5f" %2.454545)
print("%10s" %"hello")
print("%-10s" %"hello")
print("%-10sPython" %"comeon")
print("%3.5f" %2.454545)