import random

jeom = 0 #점수
cnt = 0 #맞은 갯수
qq = 0 #문제수

list1 = ["+", "-", "*", "//"]

while True:
    a = random.randint(1,9)
    b = random.randint(1,9)
    op = random.randint(0, 3)   
    if op == 0:
        key = a + b
    elif op == 1:
        key = a - b
    elif op == 2:
        key = a * b
    else:
        key = a // b

    answer = int(input(f"{a} {list1[op]} {b} = "))

    if answer == key:
       print("잘했어")
       cnt = cnt + 1
       jeom = jeom + 20
       qq = qq + 1
    else: 
       print("아쉽네")
       jeom = jeom - 10
       qq = qq + 1
    
    if jeom >= 50:
        print(f"점수: {jeom}")
        print(f"문제수: {qq}")
        print(f"맞은 갯수: {cnt}")
        break
        