score = [2, 5, 8, 7, 6]
score1 = score.copy() #카피
score1.reverse() #리스트를 역순으로

print(f"역순: {score1}")

#메모리 방식
score1 = score #score가 가리키는 자리를 score1이 가리킨다

score1.sort(reverse=True) 
print(f"내림차순: {score1}")

country = ["Korea", "japan", "CHINA", "america", "***", "한글"]
#한글이 뒤로가고 영어가 앞에옴 (오름차순 정렬하면)

country1 = country.copy() #카피

country1.sort()
print(f"오름차순: {country1}")

country.sort(key = str.lower) #대소문자 무시
print(f"문자정렬(대소문자 무시): {country}")

# sorted는 글자를 분리해서 sort. 리스트가 아닌 문자열에도 쓸 수 있음
sortCountry = sorted(country)
print(f"새로운 리스트: {sortCountry}")
what = sorted("computer")
print(what)

score = [98, 77, 88, 90, 75, 99, 100, 85, 78, 90]

best = max(score)
bestIndex = score.index(best)

print(f"{bestIndex + 1} 학생이 {best}로 최고점이다")


### 튜플
t1 = (1, 2, 3)
print(t1[0])

list1 = [3] # 원소 하나인 리스트
t2 = (1, ) # 원소가 1개인 튜플일 땐 , 해줘야 함

#공백 리스트 생성
list1 = []
list1 = list()

list2 = [None] * 5 #리스트를 none이라는 값을 가지고 5개 만들어놓음
#이미 리스트가 만들어져있는 거기에 append하지 않아도 값 추가 가능
list2[0] = 100 #그냥 이렇게

t3 = tuple(list2)


### 세트
colors = {'red', 'green', 'blue'}
print(colors)

s1 = set() # 공집합
print(colors)
print(set("python")) #순서 상관없이 출력됨
print(list("python"))


s = {1, 2, 3}
s.add(4)
s.add(3) #이미 있는 거 추가 X (중복 허용X)
print(s) 

s.remove(2)
print(s)

s.update([5, 6, 7, 8, 3]) # 추가 됨
print(s)
s.clear() # 모두 지움 
print(s) #set()이 출력됨 (공집합)

s = {1, 2, 3}
t = {1, 7, 6, 3}
print(s.union(t)) #합집합
print(s & t) #교집합
print(s-t) #차집합


### 딕셔너리

country_code = {"America" : 1, "Korea" : 82, "China" : 86, "Japan" : 81}
print(country_code)

# 요소를 찾기 전에 있는지 확인부터 해야 함
print(country_code['Korea'])
#print(country_code['France']) #없으면 에러남

if 'France' in country_code.keys(): # 이렇게 써줘야함
    print(country_code['France'])
    
#get() 함수 이용
print(country_code.get('France', "없는 국가이다")) #get은 없으면 None이라고 출력되기 때문에 에러 안 남


#리스트처럼 사용할 수 있지만 완전한 리스트는 아님
print(country_code.keys())
print(country_code.values()) # dict_values([1, 82, 86, 81])
print(country_code.items())

#출력할 땐 이렇게
for k in country_code.keys():
    print(k)
    
for k in country_code: #위와 같음. 키값만 가져옴
    print(k)
    
for k in country_code: 
    print(k, country_code[k]) # 아이템 출력
    
for k in country_code.values():
    print(k)
    
for k, v in country_code.items():
    print(k, v)
    
country_code.update(Korea = 108) #값을 바꾸기
print(country_code)

country_code.update(France = 108) #없었으면 값을 추가
print(country_code)

country_code.update({'France' : 108, 'Gana': 23}) #여러개 업데이트할 땐 딕셔너리 형식으로
print(country_code)

country_code['Gini'] = 200 #이렇게 키로 추가해도 됨
print(country_code)

datas = [[1, '홍길동'], [2, '홍길동'], [3, '이겨울'], [4, '임영웅'], [5, '영탁']]
print( dict(datas) ) # 리스트를 딕셔너리로 형변환 (2차원 리스트만 가능)


aList = [1, 2, 3, 4, 5]
bList = ['하나', '둘', '셋', '넷', '다섯']

# digits = {}
# for i in range(len(aList)):
#     digits[aList[i]] = bList[i]
# print(digits)
    
digits = {}
print(f"zip한 결과 리스트로 반환: {list(zip(aList, bList))}")
for k, v in zip(aList, bList):
    digits[k] = v
print(digits)


