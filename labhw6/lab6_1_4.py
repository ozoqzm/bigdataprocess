str1 = input("문자열을 입력하시오: ")
dict1 = {}

# for i in str1:
#     if i in dict1.keys():
#         dict1[i] = dict1[i] + 1
#     else:
#         dict1[i] = 1
# print(dict1)

#더 간단한 버전-> get사용해서!!
for i in str1:
    dict1[i] = dict1. get(i, 0) + 1
   
print(dict1)