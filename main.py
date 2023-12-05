import json
import re
import time
from urllib.parse import quote

import requests

def download(imgsrc):
    split = str(imgsrc).split('/')
    filename = split[len(split)-1]
    print(imgsrc)
    header_ = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
        'Referer': 'https://www.pixiv.net/'
    }
    url = requests.get(url=imgsrc,headers=header_,verify=False,proxies=proxies)
    with open(filename,'wb') as file:
        file.write(url.content)
    file.close()
proxies = {
    'http': 'http://127.0.0.1:7891',
    'https': 'http://127.0.0.1:7891'
}
YourInfo = json.loads(requests.get('http://ip-api.com/json/').text)
print('Your Country:',YourInfo['country'],'query:',YourInfo['query'])
word = input('输入搜索内容:')
word = quote(word)
print(word)
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
    'Referer':'https://www.pixiv.net/tags/'+word
}
p_ = 1
while True:
    print('第'+str(p_)+'页数')
    content = requests.get(
        url='https://www.pixiv.net/ajax/search/illustrations/'+word+'?word='+word+'&order=date_d&mode=all&p='+str(p_)+'&s_mode=s_tag_full&type=illust_and_ugoira&lang=zh&version=bf07d0532eb0d64f97fc7ee14124b809cad3d6d3',
        headers=header, verify=False, proxies=proxies).text
    #print(content)
    if(content.__contains__('error\":true')):
        print('Stop Bacause error is true')
        break
    p = re.compile('https:\\\/\\\/i.pximg.net\\\/c\\\/250x250_80_a2\\\\/custom-thumb\\\\/img(.*?)custom1200.jpg\",')
    m = p.findall(content)
    print(m)
    for i in m:
        imgsrc = 'https://i.pximg.net/img-master/img' + str(i).replace('\\', '') + 'master1200.jpg'
        download(imgsrc)
        time.sleep(2.5)
    p_ += 1