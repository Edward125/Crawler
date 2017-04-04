import requests
from bs4 import BeautifulSoup

#使用headers，告诉网站，我是浏览器
header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
url = 'https://movie.douban.com/chart' #爬电影排行榜
response = requests.get(url,headers=header) #返回请求的结果
#print(response.text)
bsObj = BeautifulSoup(response.text,'lxml')
start_div = bsObj.find_all('div',{'class':'pl2'})
#print(type(start_div))
for next_div in start_div:
    #print(type(next_div.contents))
    print(next_div.contents[1].get_text().strip('\n').replace(' ','') + '\n')
    #for title in next_div.get_text():
    #    print(title)

