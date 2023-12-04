f = open("outout9_3.txt", "w")

num = int(input("정수를 입력하시오: "))

f.write(str(num) + ":")
for i in range(1, num + 1):
    if num % i == 0:
        print(f"{i} ", end="")
        f.write(str(i) + " ")
f.close()