num = [100, 96, 209, 22, 30, 117]
new = []

for i in num:
    if i % 2 == 0:
        new.append(i / 10)
    else:
        new.append(i)
        
print(new)
