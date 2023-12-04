import pandas as pd

data = {'이름': ['신짱구', '최자두', '코난', '맹구'],
        '국어': [50, 91, 90, 99],
        '영어': [80, 85, 90, 95]}

df1 = pd.DataFrame(data)

print(df1)


# 조건 1: 데이터의 크기 출력
print(f"데이터 크기: {df1.shape}")

# 조건 2: 이름만 추출하여 리스트로 변경하여 출력
names = df1['이름'].tolist()
print(f"이름 데이터만 이름으로 변경 후 출력: {names}")

# 조건 3: 데이터프레임 중 코난의 정보만 추출하여 출력
conan_info = df1[df1['이름'] == '코난']
print("코난 정보만 추출하여 출력:\n", conan_info)

# 조건 4: 인덱스를 제외하고 모든 데이터를 추출하여 2차원 배열로 출력
data_array = df1.drop('이름', axis=1).values
print("데이터만 추출:\n", data_array)

# 조건 5: 이름이 인덱스가 되도록 새로운 데이터프레임 df2 생성하여 출력
df2 = df1.set_index('이름')
print("이름을 인덱스로 변경 후 출력:\n", df2)

# 조건 6: 파이썬 시험 점수를 df2에 추가하여 출력
df2['파이썬'] = [100, 60, 80, 93]
print("파이썬 점수를 추가하여 출력:\n", df2)

# 조건 7: 코난과 맹구의 정보를 함께 출력
conan_and_mangu = df2.loc[['코난', '맹구']]
print("코난과 맹구의 정보를 함께 출력:\n", conan_and_mangu)

# 조건 8: 최자두의 영어 점수 출력
choi_english_score = df2.loc['최자두', '영어']
print("최자두의 영어 점수:", choi_english_score)

# 조건 9: 신짱구와 맹구의 국어와 파이썬 점수만 추출하여 새로운 데이터프레임 df3 생성하여 출력
df3 = df2.loc[['신짱구', '맹구'], ['국어', '파이썬']]
print("신짱구와 맹구의 국어와 파이썬 점수만 추출하여 출력:\n", df3)


