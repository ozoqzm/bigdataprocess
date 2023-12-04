def BMI(height, weight): #리턴문 있음
    bmi = weight / (height * height)
    print(f"당신의 체지방지수는 %.2f입니다"%bmi)
    
    return bmi
    
def result_print(result): #여기서 print
    if result < 18.5:
        print("당신은 저체중입니다")
    elif result < 22.9:
        print("당신은 정상입니다")
    elif result < 24.9:
        print("당신은 과체중입니다")
    elif result < 29.9:
        print("당신은 경도 비만입니다")
    else:
        print("당신은 고도비만입니다")



h = float(input("키를 m단위로 입력: "))
w = float(input("몸무게를 kg단위로 입력: "))

result = BMI(h, w)
result_print(result)