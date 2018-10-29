#!/usr/bin/python3
# --*-- coding:utf-8 --*--
import requests, os, bs4
#url = input("请输入一个网址例如'www.baidu.com'：")         #从一个漫画网站开始
url = 'http://xkcd.com'
os.makedirs('comic',exist_ok=True) #当前目录创建一个存储漫画的目录
while not url.endswith('#'):
    #下载相关网页
    print('Dowloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text) #打印url用raise_for_status()方法在遇到下载问题时抛出异常，否则就创建beauifulsoup对象
    #在url里面查找相关漫画图片
    comicElem = soup.select('#comic img')   #查找soup对象中的img格式的漫画
    if comicElem == []:
        print('无法发现image格式的漫画.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')  #获取网页源码中的关键连接
        #下载获取的imge格式图片
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        #保存相关image图片到建好的当前目录./comic下
        imageFile = open(os.path.join('comic', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    #获得前一张漫画的url
    prevLink = soup.select('a[rel="prev"]')[0]
#    url = url + prevLink.get('href')
    url = 'http://xkcd.com' + prevLink.get('href')
print('完成')
