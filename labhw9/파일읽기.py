### read. 파일읽기

'''
in_file = open("input.txt", "r", encoding='utf8') #인코딩 형식 지정해야 한글 
#contents = in_file.read()
contents = in_file.readlines() #전체를 하나의 리스트로 가져옴. 엔터키까지 인식함 
print(type(contents))
print(contents)
in_file.close()
'''

# readline() 함수를 모든 내용 읽어오기
in_file = open("input.txt", "r", encoding='utf8')

while True:
    #line = in_file.readline().rstrip() #오른 쪽 빈칸을 제거하라(\n 제거). 공백:엔터키, 탭, 스페이스..
   line = in_file.readline() # 실행할 때마다 한줄씩 읽어오기
   if not line: # if line == "" (빈칸이냐), 라인에 아무것도 없으면
        break
    line = line.replace("\n", "") #줄바꿈 빈칸으로 대체
    print(line)
in_file.close()

