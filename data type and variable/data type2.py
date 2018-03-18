#문자열의 연산
a = "You've got"
b  = " a freind"
c = "Hello"

print(a+b)
print(c*3)

#인덱싱과 슬라이싱 (0부터 카운트함)
#인덱싱
str = "You've got a friend"
print(str[4])
print(str[3])
print(str[6])
print(str[13])
print(str[-1])

str1 = str[-6] + str[-5] + str[-4] + str[-3] + str[-2] + str[-1]
print(str1)

#슬라이싱
print(str[-6:])
print(str[:])

#예시
str = "20150613121320"
date = str[:8]
time = str[8:]

year = date[:4]
month = date[4:6]
day = date[6:8]

print(year+"년"+month+"월"+day+"일")