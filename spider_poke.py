import sys
from PyQt5.Qt import *
from bs4 import BeautifulSoup
import urllib.request
import sqlite3
from lxml.etree import HTML
from requests import get as rqget

#连接数据库


url='https://wiki.52poke.com/wiki/%E7%A7%8D%E6%97%8F%E5%80%BC%E5%88%97%E8%A1%A8%EF%BC%88%E7%AC%AC%E4%B8%83%E4%B8%96%E4%BB%A3%EF%BC%89'
# 获取网页内容，把 HTML 数据保存在 page 变量中
page = urllib.request.urlopen(url)
# 用 Beautiful Soup 解析 html 数据，
# 并保存在 soup 变量里
soup = BeautifulSoup(page, 'html.parser')

r = rqget(url)
r.encoding = r.apparent_encoding 
html = HTML(r.text)
small_rule = '//*[@id="mw-content-text"]/div/table[#]/tbody/tr/td/small/a/text()'

# 在表格中查找数据
table = soup.find('table', {"class":"sortable"})
results = table.find_all('tr')
database={'编号':0,'宝可梦':0,'Hp':0,'攻击':0,'防御':0,'特攻':0,'特防':0,'速度':0}##录入标题
#遍历每一行数据
for result in results:
    data = result.find_all('td')
    if len(data)==0:
        continue
    if result==results[-1]:
        continue
    small = html.xpath(small_rule.replace('#',str(results.index(result))))[0].strip()
    num=data[0].getText()
    name=data[2].getText()
    Hp=data[3].getText()
    att=data[4].getText()
    dfs=data[5].getText()
    sat=data[6].getText()
    sde=data[7].getText()
    spd=data[8].getText()
    #写入字典方便录入数据库
    database['编号']=int(num)
    database['宝可梦']=name[0:-1]
    database['Hp']=int(Hp)
    database['攻击']=int(att)
    database['防御']=int(dfs)
    database['特攻']=int(sat)
    database['特防']=int(sde)
    database['速度']=int(spd)
    print('one is ok')

    




##该段是针对第八世代的数据库爬写，仅添加第八世代新宝可梦种族，对于过去宝可梦改后期重新对数据库改写
url='https://wiki.52poke.com/wiki/%E7%A7%8D%E6%97%8F%E5%80%BC%E5%88%97%E8%A1%A8%EF%BC%88%E7%AC%AC%E5%85%AB%E4%B8%96%E4%BB%A3%EF%BC%89'
# 获取网页内容，把 HTML 数据保存在 page 变量中
page = urllib.request.urlopen(url)
# 用 Beautiful Soup 解析 html 数据，
# 并保存在 soup 变量里
soup = BeautifulSoup(page, 'html.parser')
# 在表格中查找数据
table = soup.find('table', {"class":"sortable"})
results = table.find_all('tr')
#遍历每一行数据
for result in results:
    data = result.find_all('td')
    if len(data)==0:
        continue
    if result==results[-1]:
        continue
    ifGen8=int(data[0].getText())
    if ifGen8<=809:
        continue

    
    num=data[0].getText()
    name=data[2].getText()
    Hp=data[3].getText()
    att=data[4].getText()
    dfs=data[5].getText()
    sat=data[6].getText()
    sde=data[7].getText()
    spd=data[8].getText()
    #写入字典方便录入数据库
    database['编号']=int(num)
    database['宝可梦']=name[0:-1]
    database['Hp']=int(Hp)
    database['攻击']=int(att)
    database['防御']=int(dfs)
    database['特攻']=int(sat)
    database['特防']=int(sde)
    database['速度']=int(spd)
    print(database)

    