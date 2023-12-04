# 에러의 소지가 있는 파일 읽기는 예외처리 해주기
# 프로그램은 디테일이 필요~!

try:
    f = open("dream1.txt", "r")
except FileNotFoundError as e:
    print(e) #파이썬에서 제공하는 에러메세지
    print("파일을 찾을 수 없습니다.")
else:   
    '''
    contents = f.read() #파일의 내용을 하나의 문자열로 반환
    print(contents)
    '''

    # 줄단위로 읽기  
    for line in f:
        #print(line, end='') #역슬래시 제거
        line = line.rstrip() #공백 오른 쪽에서 제거
        print(line, end='')
    f.close()


### with문 사용
    
# try:
#     with open("dream.txt", "r") as my_file:
#         content_list = my_file.readlines() #한줄씩 리스트로
#         print(content_list)
#         #줄 단위 출력
#         for line in content_list:
#             print(line)        
# except:
#     print("파일 없음")
#     


# 등장 단어 빈도 수 세기 (read()사용)
worddic = {}

with open("dream.txt") as f:
    contents = f.read()
    list1 = contents.split() # split은 리스트 반환
    # split() vs split(" ")
    # split()은 엔터, 스페이스 다 포함
    
    for word in list1:
        if word in worddic.keys():
            worddic[word] += 1
        else:
            worddic[word] = 1
    print(worddic)
    
    for k, v in worddic.items():
        print(k, "===", v)
    
    
    # 총 단어 수
    contents = contents.rstrip() #공백 오른 쪽에서 제거
    contents = contents.replace("\n", " ") #엔터를 빈칸으로 대체!!(책에는 없음)
    words = contents.split(" ")
    print(words)
    # 빈칸을 기준으로 split되면 엔터로 분리된 것은 분리가 안됨
    print(len(words))
    
    # 총 줄 수
    lines = contents.split("\n")
    print(len(lines))
    
    

    



