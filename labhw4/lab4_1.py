def game369(num):
    strnum = "" #초기화
    while num > 0:
        key = num % 10 
        num //= 10
        if (key == 3 or key == 6 or key == 9):
            strnum = "짝" + strnum
        else:
            strnum = str(key) + strnum
    return strnum
            

for i in range(1, 50):
    print(game369(i), end=" ")
    
    
