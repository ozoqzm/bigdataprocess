infile = open("num.txt", "r")  # num.txt를 읽기 모드로 열기

lines = infile.readlines()  # 파일의 모든 줄을 리스트로 읽어옴

sum1 = 0
cnt = 0

for line in lines:
    try:
        value = int(line)
        sum1 += value
        cnt += 1
    except ValueError: #예외처리 해줘야 함
        pass

infile.close()

outfile = open("num.txt", "a") # num.txt를 추가 모드로 열기
outfile.write(f"합은 {str(sum1)}\n")
outfile.write(f"평균은 {str(sum1 / cnt)}\n")


outfile.close()