import matplotlib.pyplot as plt

#배경색
plt.rc('axes', edgecolor = '#0000ff')
plt.rc('axes', facecolor = '#ffff00')

#또는 
plt.rcParams['axes.edgecolor'] = "red"
plt.rcParams['axes.facecolor'] = "yellow"

#원 그래프
ratio = [10, 40, 10, 40] # 부채꼴 영역의 비율
labels = ['attendance', 'midterm', 'report' ,'final'] # 부채꼴 영역 이름
explode = [0.3, 0, 0, 0] # 부채꼴 파이 차트 중심에서 벗어나는 정도

plt.pie(ratio, labels=labels, autopct='%.1f%%', explode=explode, shadow=True)
plt.title("Evaluation rate")
plt.show()

 