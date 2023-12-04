# 아이디 추출하는 정규 표현식

import re # 정규 표현식 관련 모듈
import requests #http 와 관련

'''
url = "http://goo.gl/U7mSQ1"
print(url.upper())
response = requests.get(url)
html_contents=response.text
# 여기까지는 html 문서 읽어오기
'''

# 임시방편..
html_contents="cotb7*** abc**abc 13*** %***"

#find_all의 결과는 리스트임. 모두 찾아라
id_results=re.findall(r"([A-Za-z0-9]+\*\*\*)", html_contents) #

for result in id_results:
    print(result)

