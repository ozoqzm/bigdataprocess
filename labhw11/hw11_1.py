
import csv #csv 모듈을 불러온다

print("서울 최저기온 찾기")

f = open("weather.csv") # 객체 변수
data = csv.reader(f) # 객체 변수
# header 제거 시에 if문 쓰지 말고 next함수 쓰기
header = next(data) #헤더 제거!!!!!
print("헤더 출력:", header) # 헤더값

cold = 1000
warm = -100

for row in data: # row는 하루의 데이터를 리스트로 변환
    try:
        if cold > float(row[3]):
            cold = float(row[3])
            day = row[0]
        if warm < float(row[3]):
            warm = float(row[3])
            dayw = row[0]
    except ValueError:
        pass

print(f"1980년 이후 {day}일이 {cold}도로 가장 추웠다")
print(f"1980년 이후 {dayw}일이 {warm}도로 가장 더웠다")

    
f.close()

