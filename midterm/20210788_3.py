import random

num = int(input("리스트의 원소 수를 입력하시오: "))

list1 = list()
list2 = list()
list3 = list()

i = 0

while (i < num):
    one = random.randint(1, 20)
    if one not in list1: 
        list1.append(one)
        i = i + 1

print(f"생성된 데이터: {list1}")

for i in list1:
    if i > 10:
        list2.append(i)
    else:
        list3.append(i)
    
print(f"10초과 데이터: {list2}")
print(f"10이하 데이터: {list3}")

if 10 in list1:
    print(f"10은 인덱스 {list1.index(10)}에 있다.")
else:
    print("10이 없다.")