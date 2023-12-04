inputfile = input("파일 이름을 입력하세요: ")
f = open(inputfile, "r")

cnt = 0
for line in f:
   cnt = cnt + len(line)
   if not line:
       break
print("파일 안에는 총 " + str(cnt) + "개의 글자가 있습니다.")
    
f.close()
