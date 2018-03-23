#제어문
#if 조건문

number = 1

if number:
    print("0이 아니다")
else:
    print("0이다")

#비교 연산자
x = 100
y = 1000

print(x>y)
print(x<=y)

#in 연산자
print("a" in ["a","b","c"]) #리스트
print("a" not in ["a","b","c"]) #리스트
print("a" in ("a","b","c")) #튜플
print("a" in "abcd") #문자열

aa =["a","b"]

flag = 1

#이중 if문

if 'c' in aa:
    print("a를 가지고 있습니다")
else:
    if flag:
        print("a를 가지고 있습니다")
    else:
        print("a를 가지고 있지 않습니다")

#elif
#다중 if문

if 'c' in aa:
    print("c를 가지고 있습니다")
elif 'a' in aa:
    print("a는 가지고 있고, c는 가지고 있지 않습니다")
else:
    print("a와 c가 aa에 없습니다")

#pass를 사용한 if문
dd = "c"
if "b" in dd:
    pass
else:
    print(dd+"는 없습니다.")

#if문을 단일문으로 처리하는 예
pp = ["a","b","c"]
if dd in pp: pass
else: print("없습니다")