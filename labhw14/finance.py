import re
import requests

url = "http://finance.naver.com/item/main.nhn?"

response = requests.get(url)
response = requests.get(url, {"code":"005930"})

html_contents = response.text

# r을 쓰는 경우는 
stock_results = re.findall("(\<dl class=\"blind\"\>)([\s\S]+?)(\<\/dl\>)", html_contents)

samsung_stock=stock_results[0] #2개의 튜플 값 중 첫번째 패턴, dt
samsung_index=samsung_stock[1] #3개의 튜플 값 중 두번째 패턴, 

# print("ss: ", samsung_stock[1])
# print("----------------------")
# print("h: ", samsung_index)

# 주식 정보만 추출함
index_list= re.findall("(\<dd\>)([\s\S]+?)(\<\/dd\>)", samsung_index)
for index in index_list:
    print(index[1]) # 세 개의 튜플 값 중 두 번째 값

