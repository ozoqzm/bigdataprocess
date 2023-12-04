names = ['신짱구', '김철수', '유리', '맹구']
pythons = [100, 90, 60, 90]
java = [90, 98 , 70, 80]
c = [97, 89, 60, 91]

average = [sum(a) / 3 for a in zip(pythons, java, c)] #a는 튜플임(각각 하나를 하나의 튜플로)
#print(average)

result = [(a, b, '합격' if b >= 80 else '불합격') for a, b in zip(names, average)]
print(result)