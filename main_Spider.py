import parser
import re
import threading
import time
from urllib import parse

import requests

_thread = 0
request = requests.Session()

def download_count(url,count,proxy_):
    global _thread
    print('try Connect Proxy Count：',count,'\tImage Address：',url)
    count = count -1
    for proxy__ in proxy_:
        proxy__ = proxy__.strip().split('	')
        # print(proxy__[0],' & ',proxy__[1])
        proxies = {
            "http": proxy__[0] + ':' + proxy__[1],
            "https": proxy__[0] + ':' + proxy__[1]
        }
        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'referer': 'https://www.pixiv.net/',
            'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
            'Connection':'close'
        }
        try:
            a = request.get(
                url=url,
                headers=header, proxies=proxies,timeout=180)
            a.close()
            index = cmpBytes(url)
            rightbyte = ''
            if index == -1:
                rightbyte = '.jpg'
            else:
                rightbyte = url[index:len(url)]
            with open(str(int(time.time()*1000000))+rightbyte, 'wb') as file:
                file.write(a.content)
            print('Download Image Successful. Use Proxy '+"IP: "+proxy__[0] + ':' + proxy__[1]+' '+proxy__[2])
            _thread = _thread - 1
            print('当前剩余线程:', _thread)
            return
        except:
            pass
    if count > 0:
        download_count(url,count,proxy_)
    else:
        print('一个线程下载失败')
        _thread = _thread - 1
        print('当前剩余线程:',_thread)

def cmpBytes(s):
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '.':
            return i
    return -1

def PixivConnect(Ip,Port,word,page):
    proxies = {
        "http": Ip+':'+Port,
        "https": Ip+':'+Port
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56'
    }
    try:
        # result = requests.get(url='https://www.pixiv.net', headers=headers, proxies=proxies, verify=False)
        # print(result.text)
        # print(result.cookies)
        t_word = {'word':word}
        result_ = request.get(url='https://www.pixiv.net/ajax/search/illustrations/'+word+'?'+parse.urlencode(t_word)+'&order=date_d&mode=all&p='+str(page)+'&s_mode=s_tag_full&type=illust_and_ugoira&lang=zh', headers=headers, proxies=proxies, verify=False)
        print(result_.url)
        result_.close()
        if result_.status_code != 200:
            return False
        if result_.text.__contains__('<HTML><HEAD><TITLE>302 Moved</TITLE></HEAD><BODY><H1>302 Moved</H1>.'):
            return False
        print(result_.cookies)
        print(result_.text)
        pattern = re.findall('"url":"https:\\\\/\\\\/i.pximg.net\\\\/c\\\\/250x250_80_a2\\\\/img-master\\\\/img(.*?_square1200.(?:jpg|jpeg|png|gif))",',result_.text)
        print(pattern)
        if len(pattern) == 0:
            print('也许已经最后一页了')
            exit(0)
        global _thread
        _thread = len(pattern)
        print('估计开启线程数:',_thread)
        for imgsrc in pattern:
            imgsrc = 'https://i.pximg.net/img-master/img'+str(imgsrc).replace('\\','')
            print(imgsrc)
            threading.Thread(target=download_count,args=(imgsrc,16,files,)).start()
            print('start a thread in imgsrc...')
            # download_count(imgsrc,5,files)
        return True
    except Exception as e:
        print('Try Next Proxy...',e.args)
        return False
def PixivRun(files,word,page):
    for line in files:
        line = line.strip()
        line_ = line.split('	')
        print('Use Proxy IP:' + line_[0] + ' Port:' + line_[1])
        ret = PixivConnect(line_[0],line_[1],word,page)
        if ret:
            return True
    return False
if __name__ == '__main__':
    word = input('输入关键字:')
    with open('Success.txt') as file:
        files = file.readlines()
        page = int(input('页数从多少开始:'))-1
        while True:
            nRet = False
            count = 16
            print('当前爬虫行走到了第 ',page+1,'页')
            while count > 0 and not nRet:
                print('剩余重试连接机会:', count)
                nRet = PixivRun(files, word,page)
                while nRet and _thread > 0:
                    pass
                count = count - 1
            page = page + 1