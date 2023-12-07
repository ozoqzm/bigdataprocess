import matplotlib.pyplot as plt

x = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', "Oct", 'Nov', 'Dec']
y = [0,0,100, 10, 5, 0, 400, 250, 550, 200, 80, 0]

plt.plot(x, y, marker="o")
plt.title("2022 월 평균 강수량 ")
plt.xlabel("월")
plt.ylabel("강수량")
plt.show()
