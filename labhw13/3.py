#산포도 그래프 
#산점도 그래프

import matplotlib.pyplot as plt
import random

n = 20
x = [random.randint(1, 10)*10 for i in range(n)]
y = [random.randint(1, 10)for i in range(n)]

plt.xlabel('score')
plt.scatter(x, y)
plt.show()

#축 눈금 크기 조절
plt.rc('xtick', labelsize=8)  # x축 눈금 폰트 크기
plt.rc('ytick', labelsize=8)  # y축 눈금 폰트 크기
