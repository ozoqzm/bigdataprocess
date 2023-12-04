###중첩 반복문 사용
for i in range(10):
    for j in range(i):
        print("*", end='')
    print() #줄바꿈
    
###단일 반복문 사용
for i in range(10):
    print("*" * i)
