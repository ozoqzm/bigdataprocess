# 여기가 스크립트 모드

# 변수 선언/정의를 하지 않음
a = 10
b = 20

print(a + b)
b = b + 10

print('pp', end='#');print('fun') # pp#fun
print (10, '+', 20)
print(10, '+', 20, sep='') #띄어쓰기
print(10, 20, 30, sep='/')
print(3.14); print("원주율") #줄바꿈 됨
print(3.14, end=' '); print("원주율") # 줄바꿈 없이 띄어쓰기

# 3.14를 소수점 5번째 자리까지 출력
print("%.5f"%3.14) #, 대신 %

#old ver
a = 5
b = 12.5678
print("%d %f"%(a, b))
print("%d %.2f"%(a, b))


#new ver (f-문자열 이용)

#값은 중괄호로 묶고 문자로 출력하고 싶은 건 그대로..
print(f'{a} + {b} = {a + b}')

x = 3.1276; y = 3.1234
print(f'x = {x:.2f}, y = {y:.2f}')


###입력문
# 
# #input 함수로 입력되면 무조건 문자열 (입력된 값 무조건 문자열(연산x))
# print("Enter your name: "); somebody=input()
# somebody = input('Enter your name: ')
# 
# #정수형으로 입력받고 싶을 때
# num = input('Enter the num: '); num = int(num)
# num = int(input('Enter the num: ')) #간결한 ver

###자료형
a = 0b11001
print(a)

poet = '''죽는 날까지 하늘을 우러러
한 점 부끄럼이 없기를
잎새에 이는 바람에도
나는 괴로워했다'''
print(poet)

# '''는 변수에 안 담으면 여러 줄 주석으로 사용됨

###아스키 코드
print('A', ord('A'))
print('a', ord('a')) #97부터 소문자 알파벳
print(chr(80))
print(chr(91)) #91~96은 특수문자




