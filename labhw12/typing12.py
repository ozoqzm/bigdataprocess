import pandas as pd
import matplotlib.pyplot as plt


### 리스트로 데이터 프레임 생성
info = [['김봄', 19, '남자', 3.45],
        ['오여름', 22, '여자', 4.1],
        ['나가을', 20, '남자', 3.9],
        ['이겨울', 26, '여자', 4.5]]

df = pd.DataFrame(info)
df.columns = ['이름', '나이', '성별', '평점']
print(df)

df1 = df.set_index(keys=['이름']) #인덱스를 이름으로 변경
# 기존에는 인덱스가 그냥 0 1 2 3 이었음
print(df1)

# df1 = df1.reset_index() #인덱스 원래대로
# print(df1)

### 데이터 추출
# df1 데이터프레임 이용

# 열 단위로 뽑아오기-> 만약 인덱스로 설정돼있으면 못 가져옴
print(df1['성별'])
print(df['이름'])

print(df1.loc['나가을']) # .loc는 위치 정보 가져옴  # 행추출
print(df1.loc[['나가을'], ['성별']]) # df1.[행, 열]

print()
print("iloc 사용법")
print(df1.iloc[2,1]) #인덱스를 이용해 가져옴
print(df1.iloc[:]) #모든 데이터
print(df1.iloc[0]) #인덱스 0인 데이터(이름 김봄 데이터)

print(df1.loc[df1['평점'] >= 3.5, ['평점']]) #평점이 3.5 이상인 사람의 평점만 출력

# 평점을 기준으로 내림차순 정렬
# (vlaue에 의해서 sorting)
df2 = df.sort_values(by=['평점'], ascending=False)
print(df2)


### 열추가 & 행추가

# df에 새로운 열 추가
df['주소'] = ['서울', '대구', '부산', '제주']
print(df)

# 마지막에 데이터 추가 (행 추가)
last_row = df.shape[0] # 행의 개수-> 행의 개수가 추가될 인덱스랑 같으니까
df.loc[last_row] = ['홍길동', 100, '남자', 3.2, '한양']
print(df)


# 데이터프레임에서 데이터 삭제하여 새로운 데이터 프레임 생성
df3 = df.drop(columns='주소') # 열 삭제
print(df3)

df4 = df.drop(index=[1, 2])
print(df4)

# 빈도 수
print(df['성별'].value_counts()) # 성별 그룹 빈도 수
print(df.value_counts()) #모든 데이터에 대해서

# 성별을 기준으로 평점의 평균 구하기
print(df.groupby('성별')['나이'].mean())

# 결측치 처리
df['계절'] = ['봄', '여름', None, None, None]
print(df)

df['계절'] = df['계절'].fillna('없음') #없는 데이터 없음으로 채움
print(df)


# 시각화
df.plot(kind='line')
plt.show()










