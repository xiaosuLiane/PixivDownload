import threading

import requests

def _Proxy(files):
    for line in files:
        try:
            line = line.strip()
            split = line.split('	')
            print('Connect ', split[0], ':', split[1])
            proxies = {
                "http": split[0] + ":" + split[1],
                "https": split[0] + ":" + split[1]
            }
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56'
            }
            result = requests.get(url='https://www.pixiv.net', headers=headers, proxies=proxies, verify=False)
            if result.status_code != 200:
                print(split[0], ':', split[1], ' 连接成功，但是访问不了网页')
                continue
            print(split[0], ':', split[1], ' 连接成功')
            print('HTTPCode:', result.status_code.__str__())
            who.write(split[0] + '	' + split[1] + '	' + split[2] + '-' + split[
                3] + '	' + result.status_code.__str__() + '\n')
            who.flush()
        except Exception as e:
            print(split[0], ':', split[1], ' 连接失败', '\t', e.args)
if __name__ == '__main__':
    who = open('Success.txt', 'a')
    with open('proxy.txt') as file:
        files = file.readlines()
    for i in range(0,len(files),10):
        list = files[i:i+10]
        threading.Thread(target=_Proxy,args=(list,)).start()