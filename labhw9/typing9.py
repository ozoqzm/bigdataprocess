### 예외 처리 구문

score = input("Enter the score: ")
grade=[]

try:
    score = int(score)
    if score >= 90:
        grade[0] = 'A+'
    elif score < 60:
        print("당신의 점수는" + score)
except ValueError:
    print("형식 오류 ")
except IndexError:
    print("첨자 범위 오류")
except TypeError:
    print("데이터 타입 오류")
else:
    print(score)
    

# raise문(고의적으로 예외를 발생시키는 코드, try구문 안에 들어가 있어야 함)
score = input("Enter the score: ")
for digit in score:
    if digit not in "0123456789":
        raise ValueError("숫자값을 입력하지 않음")
score = int(score)
print(score)

try:
    score = int(input("Enter the score: "))
    assert score > 0, '점수는 0 이상이어야 함'
except AssertionError as e:
    print(e)
else:
    print(score)
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
