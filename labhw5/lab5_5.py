numlist = []

while (True):
    num = input("수를 입력하시오(-1이면 입력끝): ")
    if num == "-1":
        break
    numlist.append(num)
    
key = input("찾고 싶은 값을 입력하시오: ")


print(f"찾는 값의 위치: {numlist.index(key)}")