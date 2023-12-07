import pandas as pd

info = {'이름': ['신짱구', '최자두', '코난', '맹구'],
        '국어': [50, 91, 90, 99],
        '영어': [80, 85, 90, 95]}

df1 = pd.DataFrame(info)

print(df1)

print("데이터의 크기 :", df1.shape)  # 행과 열, 튜플로 반환.


# 특정 컬럼명 데이터만 확인
#이름만 추출하여 리스트로 변경해 출력
print("이름만 출력: ", df1["이름"].tolist())

#코난 정보만 출력

print(df1.loc(2))




