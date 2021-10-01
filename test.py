#import urllib.request as req
#url="https://www.ptt.cc/bbs/movie/index.html"

#request=req.Request(url, headers={
#    'User-Agent': 'Mozilla/5.0'
#    })
#import urllib.request
#with urllib.request.urlopen('https://www.ptt.cc/bbs/movie/index.html') as response:
#   html = response.read()
#print(html)


# with req.urlopen(url) as response:
#    data=response.read().decode("utf-8")
# print(data)


import urllib.parse
import urllib.request

url = 'https://www.twfanti.com/book/HaoXuHanSanQianSuYingXia.html'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
values = {'name': 'Michael Foord',
          'location': 'Northampton',
          'language': 'Python' }
headers = {'User-Agent': user_agent}

data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data, headers)
with urllib.request.urlopen(req) as response:
   the_page = response.read().decode("utf-8")
#print(the_page)

import bs4
root=bs4.BeautifulSoup(the_page , "html.parser")
titles=root.find_all("div",class_="pt-chapter-cont-detail full")
#if "pt-chapter-cont-detail full" in titles:
#    if "pt-chapter-cont-detail full".a !=   None:
#print(titles)
#print(titles)
#print(root.find_all('a'))
#import re
#print(root.find("span", title=re.compile("RAM")).text)

from bs4 import BeautifulSoup 
r  = requests.get("https://www.twfanti.com/book/HaoXuHanSanQianSuYingXia.html").content

soup = BeautifulSoup(r,"lxml")
cont = soup.select_one("div.systemRequirementsRamContent")
ram = cont.select_one("span")
print(ram["title"], ram.text)
for span in soup.select("div.systemRequirementsSmallerBox.sysReqGameSmallBox span"):
        print(span["title"],span.text)

