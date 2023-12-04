cnt = 0

for i in range(11, 100101):
    if i % 55 == 0: continue
    cnt = cnt + i
else:
    print(cnt)
    