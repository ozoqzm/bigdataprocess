# 시험범위 아님
from bs4 import BeautifulSoup

html = '''
<h1 id="title">한빛출판네트워크</h1><div class="top"><ul
class="menu"><li><a href=http://www.hanbit.co.kr/member/login.html
class="login">로그인 </a></li></ul><ul class="brand"><li><a href="http://www. 
hanbit.co.kr/media/>한빛미디어<li><a href="http://www.hanbit.co.kr/
academy/">한빛아카데미</a></li></ul></div>
'''
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())

tag_h1 = soup.h1
print(tag_h1)
print(tag_h1.get_text())
tag_ul_all = soup.find_all("ul")
print(tag_ul_all)
tag_ul_2 = soup.find('ul', attrs={'class':'brand'})
print(tag_ul_2)
li_list = soup.select("div>ul.brand>li")

for i in li_list:
    print(i)

 

 