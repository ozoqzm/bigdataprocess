import pandas as pd
import csv 
from matplotlib import pyplot as plt

df = pd.read_csv('prac.csv')
print(df)

df2 = df.copy()

# 열 별 결측치 개수 출력
print(df.isna().sum())

# 자바, 파이썬의 결측치 0으로
df2[['자바', '파이썬']] = df2[['자바', '파이썬']].fillna("0")
df2[['응시여부', '확인여부']] = df2[['응시여부', '확인여부']].fillna("No")
print(df2)

print(df2[['이름', '자바', '파이썬']])

#자바 컬럼 값이 80이상, 파이썬 컬럼값 90 이상 데이터 추출&출력
df_filtered = df[(df['자바'] >= 80) & (df['파이썬'] >= 90)]
print(df_filtered)

# 반 별로 데이터 개수 집계해 출력
print(df.groupby('반').size())

print(df)

df3 = df[df['응시여부'] == '응시']
print(df3)

# 반별 성적 평균 구하기
average = df3.groupby('반')[['자바','파이썬']].mean()
print(average)

#df3 대상 그래프 그리기
plt.rcParams['font.family'] = 'Malgun Gothic' 
df3_plot = df3[['이름', '자바', '파이썬']]
df3_plot = df3_plot.set_index('이름')
df3_plot.plot(kind='bar', stacked=False) #True면 그래프 위에 쌓임
plt.title('이름, 자바, 파이썬')
plt.show()