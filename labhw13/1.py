import matplotlib.pyplot as plt

x = ['커피', '콜라', '사이다', '물']
y1 = [10, 20, 15, 30]
y2 = [20, 15, 20, 35]

plt.rcParams['font.family'] = 'Malgun Gothic' 
plt.plot(x, y1, x, y2)
plt.title("음료수 종류별 전년대비 판매량 ")
plt.xlabel("음료수 종류")
plt.ylabel("판매량")
plt.legend(['2022', '2023'], loc="upper right")
plt.show()
