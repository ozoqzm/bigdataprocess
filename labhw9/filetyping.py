### write

f = open("output.txt", "wt") # w는 wt와 같다

f.write("hello world\n") #줄바꿈이 안되는 함수 /n 필요
f.write("hello world\n")
f.write("hello world\n")
f.close()

g = open("output1.txt", "w")
print("sjpark", file = g)
g.close() #close를 안하면 파일은 생기지만 내용 안들어감


# Q.
# 리스트에 5개의 정수가 저장되어있다.
# 리스트에 저장된 데이터의 합과 평균을 구해 파일 저장하시오.
# 단, 합계와 평균은 각각 다른 줄에 저장된다.

f = open("output_new.txt", "w") # w는 wt와 같다

list1 = [3, 5, 7, 9, 6]
#f.write(f"{sum(list1)}") # 이렇게 적어줘도 됨 (문자열 변환)
f.write(str(sum(list1))+ "\n") #write는 문자데이터만 저장 가능
f.write(str(sum(list1) / len(list1)))
f.close()
