infile = open("lab14_4.txt", "r")

search_word = input("단어 입력: ")
word_dic = {}

contents = infile.read().lower()
contents = contents.replace(',', '')  # 전체 문자열에서 쉼표(,)를 제거
word_list = contents.split()

# 각 단어의 빈도수를 계산하여 딕셔너리에 저장
for word in word_list:
    if word in word_dic:
        word_dic[word] += 1
    else:
        word_dic[word] = 1
#print(word_dic)

for k, v in word_dic.items(): 
    if k == search_word:
        print(f"{search_word} 빈도: {v}")

infile.close()
