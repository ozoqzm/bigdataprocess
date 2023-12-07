import pandas as pd

info = {"이름" : ["자두", "짱구", "유리", "맹구", "철수"], "키" : [150, 130, 125, 140, 140], "몸무게" : [45, 28, 30, 48, 35]}

df = pd.DataFrame(info)
print(df)
print("-"*20)

df["BMI"] = round(df["몸무게"] / (df["키"] / 100 * df["키"] / 100), 2)

result = []
for i in df["BMI"] :
    if i >= 30 : result.append("고도비만")
    elif i >= 25 : result.append("비만")
    elif i >= 23 : result.append("과체중")
    elif i >= 18 : result.append("정상")
    elif i < 18 : result.append("저체중")
df["비만도"] =result

print(df)
print("<<BMI 지수가 최소인 사람>>")
print(df.loc[df["BMI"] == df["BMI"].min(), ["BMI", "이름"]])

print("<<비만도를 기준으로 그룹핑한 결과>>")
print(round(df.groupby("비만도")["BMI"].mean(), 2))

print("<<비만도별 사람 수>>")
print(df["비만도"].value_counts())

df.to_csv("info.csv")
