import pandas as pd

titanic_data = pd.read_csv('titanic.csv')

# 1. 데이터의 일부 출력
print("1. 데이터 일부 출력:")
print(titanic_data.head())


# 2. 데이터의 기본 정보 확인
print("2. 데이터 기본 정보 확인:")
print(titanic_data.info())


# 3. 생존자 사망자 수 확인
print("3. 생존자와 사망자의 수:")
print(titanic_data['Survived'].value_counts())


# 4. 객실 등급별 승객 수 확인
print("4. 객실 등급별 승객 수:")
print(titanic_data['Pclass'].value_counts())


# 5. 성별에 따른 생존자 수 확인
print("5. 성별에 따른 생존자 수:")
print(titanic_data.groupby('Sex')['Survived'].value_counts())


# 6. 나이 분포 확인
print("6. 나이 분포 확인:")
print(titanic_data['Age'].describe())


# 7. 형제/배우자 수에 따른 생존자 수 확인
print("7. 형제/배우자 수에 따른 생존자 수:")
print(titanic_data.groupby('SibSp')['Survived'].value_counts())


# 8. 부모/자녀 수에 따른 생존자 수 확인
print("8. 부모/자녀 수에 따른 생존자 수:")
print(titanic_data.groupby('Parch')['Survived'].value_counts())


# 9. 승선 항구별 승객 수 확인
print("9. 승선 항구별 승객 수:")
print(titanic_data['Embarked'].value_counts())


# 10. 결측치 확인
print("10. 결측치 확인:")
print(titanic_data.isnull().sum())


# 11. 선실 등급에 따른 생존자 수 확인
print("11. 선실 등급에 따른 생존자 수:")
print(titanic_data.groupby('Pclass')['Survived'].value_counts())


# 12. 성별 및 선실 등급에 따른 생존자 수 확인
print("12. 성별 및 선실 등급에 따른 생존자 수:")
print(titanic_data.groupby(['Sex', 'Pclass'])['Survived'].value_counts())


# 13. 요금 분포 확인
print("13. 요금 분포 확인:")
print(titanic_data['Fare'].describe())


# 14. 선실 등급별 성별의 나이 평균 확인
print("14. 선실 등급별 성별의 나이 평균:")
print(titanic_data.groupby(['Pclass', 'Sex'])['Age'].mean())


# 15. 생존자 중 최고령자와 최연소자 확인
print("15. 생존자 중 최고령자와 최연소자:")
survived_passengers = titanic_data[titanic_data['Survived'] == 1]
print("최고령:", survived_passengers['Age'].max())
print("최연소:", survived_passengers['Age'].min())
