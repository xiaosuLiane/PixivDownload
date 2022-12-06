# PixivDownload  
![cb8065380cd791232e8a0b10aa345982b2b78068](https://user-images.githubusercontent.com/42183711/205938027-86f86cd5-84fc-4720-84c2-889eacdad4c5.png)  
图片来源：www.Pixiv.net  
使用代理IP配合爬虫进行数据的爬取，每个都有重复机会  
如果你问我为什么设置这么多重试机会? 我只能说穷，目前使用的是网络上公开的免费代理不太稳定    
使用方法：  
（可采取的）  
1.如果要测试哪个可以访问Pixiv，可以使用源码内的main.py  
2.并且把代理复制写入进Proxy.txt文件，然后运行main.py进行代理连通测试（代理测试使用的是：https://www.sslproxies.org/  
3.代理复制格式请参考Successful.txt内容复制  
#爬虫使用方法  
1.确保Successful.txt里面存放了可以连接的外国Https代理（Pixiv被国家防火墙了）  
2.运行main_Spider.py爬虫程序  
3.输入需要搜索的关键字插画  
4.静静等待（看你连接代理的速度快不快了，不建议放太多代理）  
5.下载完一页之后将会自动切换下一页进行下载，如果没有内容则自动结束（判断为没有内容了）  
