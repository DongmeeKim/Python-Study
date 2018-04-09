# 모듈

# 내부 모듈 sys 실행 예제

import sys

print("명령줄 인수 체크하기!!!")
for n in sys.argv:
    print(n)

# 외장 모듈인 경우 sys.path에 정의된 디렉토리 알아보기

print("\n\n 파이썬의 sys.path 디렉토리",sys.path)