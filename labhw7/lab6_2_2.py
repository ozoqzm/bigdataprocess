# result1 = [i*i for i in range(1, 10) if i % 2 == 0]
# print(result1)

result2 = list()
for i in range (1,10):
    if i % 2 == 0:
        result2.append(i * i)
for i in result2:
    print(i)


