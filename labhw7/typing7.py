#변수 = 조건이 참일 때 값 if 조건 else 조건이 거짓일 때 값
#변수 = 조건1이 참일 때 값 if 조건1 else 조건2가 참일 때 if 조건2 else 조건2가 거짓일 때 값

# 비어있는 리스트에 0~9추가
list1 = [] #list1 = list()

for i in range(0, 10):
    list1.append(i)
print(list1)

# 또다른 방법: 리스트 컴프리헨션 (반복문 + 리스트 => 새로운 리스트 간단히)
result = [i for i in range(10)]
print(result)



###리스트 컴프리헨션 용법 필터링

#짝수만
# list1 = [] #list1 = list()
list1.clear() #초기화

for i in range(0, 10):
    if i % 2 == 0:
        list1.append(i)
print(list1)

#짝수만 리스트컴프리헨션
result = [i for i in range(10) if i % 2 == 0]
print(result)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [i if i % 2 == 0 else i * 10 for i in nums]
print(result)

#조건식 여러개인 경우
result = [i for i in range(20) if i % 3 == 0 if i % 4 == 0]
print(result)

#elif구조 리스트 컴프리헨션
scores = [99, 70, 85, 65, 89]
grade = []

#원래는
for score in scores:
    grade.append("A" if score >= 90 else "B" if score >= 80 else "C")
print(grade)

#리스트 컴프리헨션(조건문 뒤에 반복문)
grade = ["A" if score >= 90 else "B" if score >= 80 else "C" for score in scores]
print(grade)



### 리스트 컴프리헨션 용법 중첩 반복문
word_1 = "Hello"
word_2 = "World"
list1 = []
ss = ""

for i in word_1:
    for j in word_2:
        list1.append(i+j)
print(list1)

#리스트 컴프리헨션
case1 = ["A", "B", "C"]
case2 = ["D", "E", "A"]

result = [i + j for i in case1 for j in case2 if i != j] #반복문 끝에 if문
print(result)

###리스트 컴프리헨션 용법: 이차원 리스트
words = "The quick brown for jumps over the lazy dog"
list1 = words.split() #리스트로 반환
stuff = []

for w in list1:
    sub1 = []
    sub1.append(w.upper())
    sub1.append(w.lower())
    sub1.append(len(w))
    stuff.append(sub1)
print(stuff)

#리스트 컴프리헨션
stuff = [[w.upper(), w.lower(), len(w)] for w in list1]

[i+j for i in case1 for j in case2]  
[[i+j for i in case1] for j in case2]
print(stuff)


#enumerate(): 리스트의 인덱스와 데이터 분리해 함께 반환
datas = ["tic", "tac", "toe"]
for i in range(len(datas)):
    print(i, datas[i])

for i, v, in enumerate(datas):
    print(i, v)
    
#zip()
x = (1, 2, 3)
y = (10, 20, 30)
z = (100, 200, 300)

result = list()
for i in range(len(x)):
    result.append(x[i]+y[i]+z[i])
print(result)

#리스트 컴프리헨션
result = [sum(a) for a in zip(x, y, z)] #a는 튜플임(각각 하나를 하나의 튜플로)
print(result)

str1 = "hello"
str2 = "world"
result = [a[0]+a[1] for a in zip(str1, str2)]
print(result)

#람다 함수
#filter(): 조건에 맞는 것만 추출, 리스트 반환
datas = [10, -6, 4, 50, 20, -9]
f = lambda x: x < 5
result = list(filter(f, datas))

#map(): map(변환 함수, 순회 가능 데이터) 필터링 기능
ex = [1, 2, 3, 4, 5]
f = lambda x : x ** 2
for value in map(f, ex):
    print(value)

#다른 방법
result = [x * x for x in ex]
print(result)
