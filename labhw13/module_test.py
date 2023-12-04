import ex13_calc # 파일명 import

# __name__ 에 __main__ 저장 안 해주면
# add만이 아니라 전체가 다 불러와짐
print(ex13_calc.add(20, 20)) 

# 리스트가 가질 수 있는 속성(함수) 모두 보여 줌
#print(dir([1, 2, 3]))
print(dir("abc")) #아래 쪽-문자열에 종속되어지는 함수(문자열.함수())  위쪽- 일반함수