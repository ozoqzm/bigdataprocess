ss = input("문자열을 입력하세요: ")
key = input("찾을 문자를 입력하세요: ")

list = ss.part()
print(list)

ii = ss.index(key)
print(ii)

if key in ss:
    print(f"찾을 문자가 포함된 단어: {ss[ii]}")