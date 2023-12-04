import random

print("<<덧셈 문제 연습 게임>>")
print('-' * 20)

cnt = 0
trying = 0
while True:
    n1 = random.randint(1, 99)
    n2 = random.randint(1, 99)
    sum = n1 + n2
    
    answer = int(input(f"{n1} + {n2} = "))
    if cnt == 5:
        break;
    if sum == answer:
        print("맞았다.")
        cnt = cnt + 1
    else:
        print("틀렸다.")
    trying = trying + 1

print(f"시도횟수: {trying}")
    
    
