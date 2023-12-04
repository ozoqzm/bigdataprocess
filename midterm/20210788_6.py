products = [{'name' : '우유500', 'price' : 3200 , 'amount': 20},
            {'name' : '라면', 'price' : 800 , 'amount': 50},
            {'name' : '빵', 'price' : 2000 , 'amount': 15},
            {'name' : '김밥', 'price' : 3500 , 'amount': 10},
            {'name' : '커피', 'price' : 1500 , 'amount': 30}]

list1 = list()
# for i in products:
#     list1.append(i['name'])
    
list1 = [i['name'] for i in products]
print(f"품목명: {list1}")

list2 = list()
# for i in products:
#     if i['amount'] >= 20:
#         list2.append(i)
        
list2 =[i for i in products if i['amount'] >= 20]
        
print(f"재고량수량이 20개 이상 품목리스트: {list2}")

list3 = list()
for i in products:
    cnt = cnt + i['price']
list3 = [sum(i['price'] for i in products)]
print(f"마트의 총 자산: {cnt}")
         
         