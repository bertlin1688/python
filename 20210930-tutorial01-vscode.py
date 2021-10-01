#Hell World
print("hell world")

#測試爬蟲
import requests
from bs4 import BeautifulSoup as bs

#PPT網址
url="https://www.ptt.cc/bbs/movie/M.1632928031.A.49B.html"
res=requests.get(url)
#print(res.text)


#解析網頁
soup=bs(res.text,"lxml")

#定位article-meta-value
raw_data=soup.select("span.article-meta-value")

#清理資料
title=raw_data[2].text
#print(title)

author=raw_data[0].text
#print(author)

category=raw_data[1].text
#print(category)

data={
    "author":author,
    "title":title,
    "category":category
    
}

data



