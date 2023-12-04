line_count = 0;
weathers = [] # 전체 데이터 리스트에 저장할 예정

with open("weather.csv") as f:
    for data in f:
        data = data.replace("\n", "") #data.rstrip()
        if not data: #while문에서만 씀 (for문일 때는 안써도 됨)
            break
        if line_count == 0: #첫번째 줄인 경우
            data_header = data.split(",")
        else:
            weathers.append(data.split(",")) #반환된 리스트를 리스트안에 집어넣음
        line_count += 1
        
print("Header: ", data_header)
for i in range(10):
    print(f"Data{i} : {weathers[i]}")
    
    
    
### csv 모듈 사용
    
import csv #csv 모듈을 불러온다

f = open('weather.csv') # 객체 변수
data = csv.reader(f) # 객체 변수

cnt = 0
for row in data:
    if cnt < 10:
        print("Data", cnt, ":", row)
    else:
        break
    cnt += 1
    
f.close()

import csv #csv 모듈을 불러온다

print("서울 최저기온 찾기")

f = open('weather.csv') # 객체 변수
data = csv.reader(f) # 객체 변수
# header 제거 시에 if문 쓰지 말고 next함수 쓰기
header = next(data) #헤더 제거!!!!!
print("헤더 출력:", header) # 헤더값

cold = 1000

for row in data: # row는 하루의 데이터를 리스트로 변환
    try:
        if cold > float(row[3]):
            cold = float(row[3])
            day = row[0]
    except ValueError:
        pass

print("최저 기온 Day:", day)
print("최저기온: ", cold)
    
f.close()


### csv writer

import csv

with open("output.txt", "w", newline="") as outf:
    writer = csv.writer(outf)
    datas = 'hello,python'
    writer.writerow(datas)
    

    
    
    
    
    
    
    
    
    
    
    
    
    


        

