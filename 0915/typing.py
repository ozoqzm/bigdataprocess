for i in range(1, 11):
    print(i, end=' ')
    
price =  123
n100 = price // 100 # 정수로 나누기
n10 = (price % 100)
    
###for문 사용법

# 1. for 변수명 in range(start, end, step)
for i in range(1, 10, 1):
    print(i)
    
for i in range(10):
    print(i)
    
for i in range(1, 10): #step생략 (step==1)
    print(i)
    
# 2. for 변수 in 문자열:
# 문자열만큼 반복, 변수는 문자열의 문자를 하나씩 갖는다
for ch in 'abcde':
    print(ch) # a b c d e
    
#3. for 변수 in 리스트:
for i in [10, 20, 30, 40]:
    print(i) # 리스트의 원소가 하나씩 출력됨 (리스트의 수만큼 알아서 반복됨)
    
###continue문 (반복문 제어 역할)
for i in range(10):
    if i == 5: continue #i가 5가 되면 출력 안하고 이어서..
    print(i)

    
for i in range(10):
    print(i)
else:
    print("End of Program") #어떤 조건이 완전히 끝났을때 한번더 실행해주는 역할을 함
    
#소수 구하기 프로그램
    
#기존 ver
num = int(input("숫자 입력: "))

prime = 1
for i in range(2, num): #i는 num 보다 큰 값 가질 수 없음. range니까
    if num % i == 0:
        prime = 0
        print("소수 아님")
        break
if prime == 1:
    print("소수이다")
    
# else ver
num = int(input("숫자 입력: "))   
for i in range(2, num): #i는 num 보다 큰 값 가질 수 없음
    if num % i == 0:
        print(f"{i}는 소수 아님")
        break
else:
    print("소수이다")
    
    
###20까지 볼 것임(소수인지 아닌지)
for n in range(2, 21): #i는 num 보다 큰 값 가질 수 없음. 21로 해야..
    for i in range(2, n):
        if n % i == 0:
            print(f"{n}는 소수 아님")
            break
    else:
        print(f"{n}는 소수이다") #나누어 떨어지는 게 없이(조건이 거짓이어서 종료) 내부 반복문이 종료되었을 경우 출력



###2부터 시작해서 20까지의 약수 구하기
for i in range(2, 21): #range는 for문이랑 다르게 end에 + 1!
    print(f"{i}의 약수:", end=' ')
    for j in range(1, i+1): #1부터 자기자신까지 반복
        if (i % j == 0):
            print(j, end=' ')
    print() #이것도 줄바꿈


#프로그램 작성 시: 특정 블럭의 코드가 생각나지 않을 때
# if 조건이 참일 때, 거짓일 때 코드가 생각나지 않아.. 코드를 나중에 완성하고 싶다!!할 때 pass씀
# if 조건식:
#     pass
# else:
#     pass

###어떤 하나의 문자열을 역순으로 출력하기

#역순문자열1
strr = input("문자열 입력: ")
str2= ""
for ch in strr:
    str2 = ch + str2
print(str2) #문자열 출력
    
print('-' * 20)

# 역순문자열2
str1= "hello"
print(str1[::-1])
    

###이진수 출력

# num = int(input("숫자 입력: "))
# str2 = ""
# for i in range(1, num + 1):
#     str2 = str2 + str(int(num % 2))
#     num = num // 2
#     if num == 0:
#         break
# 
# print(str2)


result=""
num = int(input("숫자 입력: "))
while num > 0:
    r = num % 2 #나머지
    result = str(r) + result #여기서 오류 뜸... 뭘까?
    num = num // 2
print(f"{num}을 이진수 반환하면 {result}이다")
    
    

###난수 생성
import random #import 해주기!!

n = random.randint(1, 10) # 1 <= n <= 10
print(n)

n = random.randrange(1, 10) # 1 <= n < 10
print(n)

n = random.random() # 0 <= n < 1
print(n)

n = random.choice(['red', 'green', 'blue']) #n은 red, green, blue중 하나
print(n)

n =  random.choice(range(20, 30)) # 20 < n < 30
print(n)

n = random.choice("abcde") #a, b, c, d, e 중 하나
print(n)

#1이상 100이하 수 중 하나를 난수 생성한 후 그 수를 맞추는 게임

#무한 루프 O
num = random.randint(1, 10)
print(f"난수는 {num}")

cnt = 0

while True:
    answer = int(input("정답은 "))
    if answer == num:
        print("당첨")
        break
    elif num > answer :
        print("up")
    else:
        print("down")
    

# 무한루프X
answer = random.randint(1, 100)
print(f"난수는 {answer}")
guess = int(input("정답: "))

while answer != guess:
    if answer > guess:
        print("up")
    else:
        print("down")
    guess = int(input("정답: "))
print("당첨")

    
# 횟수 제한

num = random.randint(1, 10)
print(f"난수는 {num}")

for i in range(5): 
    while True:
        answer = int(input("정답은 "))
        if answer == num:
            print("당첨")
            break
        elif num > answer:
            print("up")
        else:
            print("down") 
else:
    print("5번 끝! 실패")
  
    







