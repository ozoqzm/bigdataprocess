str1 = "the language of truth is simple"
print(f"평문: {str1}")

p1 = "abcdefghijklmnopqrstuvwxyz"
p2 = "defghijklmnopqrstuvwxyzabc"

str2 = ""
for char in str1:
    if char in p1:
        index = p1.index(char) #주어진 문자열의 인덱스 구하기
        str2 = str2 + p2[index]
    else:
        str2 = str2 + char

print(f"암호문: {str2}")
