num = int(input("라면 주문수량 입력: "))
print()
print("배송정보")
print("-" * 20)

result1 = 0
result2 = 0
result3 = 0
cnt1 = 0
cnt2 = 0
cnt3 = 0
while (num > 0):
    if num > 50:
        num = num - 50
        cnt1 = cnt1 + 1
    elif num > 30:
        num = num - 30
        cnt2 = cnt2 + 1
    else:
        num = num - 10
        cnt3 = cnt3 + 1

    
print(f"50개씩 묶음: {cnt1}")
print(f"30개씩 묶음: {cnt2}")
print(f"10개씩 묶음: {cnt3}")
print("-" * 20)




