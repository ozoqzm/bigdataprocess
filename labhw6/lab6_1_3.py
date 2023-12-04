items = {"커피":7, "펜": 3, "종이컵": 2, "우유": 1, "콜라": 4, "책": 5}

print("--재고관리--")
print("1. 모든 상품 재고수량 확인")
print("2. 특정 상품 재고수량 확인")
print("3. 상품 판매")
print("4. 상품 입고")
print("5. 종료")
print()

while(True):
    print("-" * 20)
    num = input("메뉴 입력: ")
    if num == "5":
        break
    elif num == "1":
        for k in items:
            print(f"{k}: {items[k]}개")
    elif num == "2":
        key = input("상품명 입력: ")
        if key in items.keys(): 
            print(f"재고수량: {items[key]}")
        else:
            print("상품명 입력 오류")
    elif num == "3":
        key = input("판매 상품명 입력: ")
        if key in items.keys(): 
            quantity = int(input("판매 수량 입력: "))
            if quantity > items[key]:
                print("상품이 부족합니다")
            else:
                items[key] = items[key] - quantity
                print("상품이 판매되었습니다")
    elif num == "4":
        key = input("입고 상품명 입력: ")
        if key in items.keys(): 
            quantity = int(input("입고 개수 입력: "))
            items[key] = items[key] + quantity
            print("상품이 입고되었습니다")
        
        