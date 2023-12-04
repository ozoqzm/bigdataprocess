### 문자열 슬라이스
ss = "Python"

print(ss[-3])
print(ss[1:3:1])
print(ss[0: 4: 2])
print(ss[:4]) #Pyth
print(ss[:]) #처음부터 끝까지
print(ss[::-1]) #역순문자열

### 문자열 연산
a = "python"
b = "is"
c = "fun"

result = a + "," + b + "," + c
print (result)

print("t" in a)

if "t" in "Python":
    print("찾았다")

for i in "Python":
    if (i == "t"):
        print("찾았다")
        
ss = "Python is Fun"
print(len(ss))
print(ss.upper())
print(ss.title())
print(ss.capitalize())

ss2 = "abc" * 10
print(ss2.count("abc"))