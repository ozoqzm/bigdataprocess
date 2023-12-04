def average(*args):
    cnt = 0
    sum = 0
    print("매개변수로 전달된 값: ", end="")
    
    for i in args:
        print(i, end=" ")
        cnt += 1
        sum += i
    print()
    return sum /cnt
    
    
print("평균: ", average(1, 2, 3, 4, 5))
print("-" * 40)

print("평균: ", average(30, 10, 20))
