import pandas as pd
from matplotlib import pyplot as plt

info = [['김봄', 19, '남자', 3.45],
        ['오여름', 22, '여자', 4.1],
        ['나가을', 20, '남자', 3.9],
        ['이겨울', 26, '여자', 4.5]]

df = pd.DataFrame(info)
df.columns = ['이름', '나이', '성별', '평점']

# 시각화
df.plot(kind='line')
plt.show()

#maltplotlib 없이 pandas 내에서 그래프 그릴 수 있음
#plt는 꼭 있어야 함