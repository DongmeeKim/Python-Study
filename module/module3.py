# 모듈의 name 속성("__name__") 

def sum(i,j):
    return i+j

def differ(i,j):
    return i-j

if __name__ == "__main__":
    print(sum(1,2))
    print(differ(1,2))