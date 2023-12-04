### 함수

def getFact(): #함수 정의
    fact = 1
    for i in range(10, 0, -1): #스택이 0까지니까 -1씩
        fact *= i
        if i == 1:
            print(f"{i}", end='') #줄바꿈 대신 띄어쓰기
        else:
            print(f"{i} *", end='')
    print(f" = {fact}")
    

def getFact1(n): #함수 정의, 매개변수 1개, 반환값O
    fact = 1
    for i in range(n, 0, -1): #스택이 0까지니까 -1씩
        fact *= i
        if i == 1:
            print(f"{i}", end='')
        else:
            print(f"{i} *", end='')
    
     #print(f" = {fact}")
    return fact #함수의 결과 반환

def getFact3(): #함수 정의, 매개변수X 반환값O
    fact = 1
    for i in range(10, 0, -1): #스택이 0까지니까 -1씩
        fact *= i
        if i == 1:
            print(f"{i}", end='')
        else:
            print(f"{i} *", end='')
    
     #print(f" = {fact}")
    return fact #함수의 결과 반환
    

#여러가지 값을 리턴해야하는 경우
#1~100 짝수의 합과 평균을 구하여 반환하는 함수
def getSumAvg():
    total = 0
    cnt = 0
    
    for i in range(2, 101, 2): #2씩 증가하면 짝수만 돌 수 있음
        total += i
        cnt += 1 #파이썬은 증감연산자 없음
    return total, total / cnt


#함수 호출 영역
getFact()

num = int(input("정수입력: "))
print(f" = {getFact1(num)}") #반환값을 출력하고 싶을 때

print(f" = {getFact3()}" ) #반환값을 출력하고 싶을 때

print(getSumAvg()) #tuple로 출력됨

#unpacking
total, avg = getSumAvg() #반환값 2개니까 변수 2개 씀
print (total, avg)


def spam(eggs):
    eggs.append(1) #기존 객체의 주소값에 [1] 추가
    eggs = [2, 3] #새로운 객체 생성
    
ham = [0]
spam(ham)
print(ham)
#  0 <- ham / 0 <- eggs(햄이 가리키던 자리 가리킴)
# 0,1 <- ham,eggs (둘이 같은 자리 가리킴)
# 0,1 <- ham / 2, 3 <- eggs(나 다른 자리 가리킬게)


def f(x):
    y = x 
    x = 5
    
    return y * y

def g(x):
    y = x
    global z #z라는 변수를 global로 선언(바깥에 있는 변수와 공유!!)
    z = z + 200
    x = 5
    
    return y * y

x = 3
z = 100
print(g(x)) # 9
print(z) #300
#print(f(x)) #9
#print(x) #3


###키워드 인수

# def 함수명(매개변수1, 매개변수2, 매개변수3):
#     함수 바디
#     
# #함수 호출
# 함수명(매개변수1=값1, 매개변수2=값2, 매개변수3=값3)

###예시
def getSum(a, b, c):
    result = a + b + c
    print(result)
    
###위치 인수
getSum (1, 2, 3)

###키워드 인수
#매개변수와 값을 동시에 줌
getSum (c=3, a=1, b=2)
getSum (1, 2, c=3)
#위치인수와 키워드인수를 같이 쓸거면 항상 키워드 인수는 맨 뒤에 있어야 함
#getSum (c=3, 2, 1) #xxx 오류

###키워드 가변 인수
def getSum3(a, b, **c): #키워드 가변인수는 딕셔너리 형태{}
    print(a, b, c)
    
    #키워드 가변인수 해제 (unpacking)
    print("가변인수 unpacking")
    for k in c:
        print(k, c[k])
           
getSum3(b=5, a=3, c=4)
getSum3(b=5, a=3, c=4, d=5)
getSum3(1, 2, c=4, d=6, e=8)


###가변 인수
def getSum2(a, b, *args): #매개변수에 기본값 설정
    print(a, b, args)
    print(f"합 = {sum(args)}")
    best = a if a > b else b
    # == best = (a > b ? a : b)
    
    for i in args: #args요소 출력
        if best < i:
            best = i
        print(i)
    print(f' 최댓값= {best}')
           
getSum2(1, 2, 3)
getSum2(1, 2, 3, 4)
getSum2(1, 2, 3,4,5,6,7,8) #매개변수와 인수의 수가 다르면 저 값들을 한꺼번에 가짐


###디폴트 인수
def getSum1(a, b, c=10): #매개변수에 기본값 설정
    result = a + b + c
    print(result)

getSum1(1, 2, 3)
getSum1(1, 2)











