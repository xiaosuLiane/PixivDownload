# PixivDownload  
本脚本国内使用需要配合Clash代理  
如果在国外,请把代码中的proxies删除并把requests.get后面的proxies也删除  
(如果需要找Cookie的，不知道的可以往最下面看)  
使用教程：  
#1、安装Clash  
網址：https://ikuuu.me/user/tutorial  
選擇自己的系統類型並配置好ikuuu的免費代理  
並設置好自己的端口進入下一步。  
#2、更改脚本代理端口  
![捕获](https://github.com/xiaosuLiane/PixivDownload/assets/42183711/cd9354a8-a210-4430-8f94-93b5be273a6a)  
默认端口为7890，如果不想改就改脚本内的端口  
找到下载的main.py脚本  
#2.1、更改脚本端口  
如果你上一个步骤已经改了7891就不需要2.1步骤了，配置完成。  
![无标题](https://github.com/xiaosuLiane/PixivDownload/assets/42183711/2028c58f-d1e2-4c48-8b99-79621971683d)  
图个方便使用记事本打开快捷键ctrl+F搜索全部叫7891的端口改成7890直到没有7891端口的文本为止。  
  
如何使用脚本？  
以Pycharm（pythonIDE）运行为例  
![无标题](https://github.com/xiaosuLiane/PixivDownload/assets/42183711/ba7feb44-0a10-4f6b-bc92-e259f88c3fe2)  
运行之后默认会从第一页爬取，输入你想要搜索的插画（例如：风景）目前只弄了插画  
回车运行即可  

# 我該如何找到Cookie?
（在做下面步骤之前请先在你的浏览器登录你的Pixiv账户）
1、在浏览器上Pixiv登录账号之后,按下电脑F12点击红色箭头按键
![US_R~QXYA~GQT~~HH~Q})71](https://github.com/xiaosuLiane/PixivDownload/assets/42183711/5ba2e2f2-cf2a-41be-b55a-48fafe4c4ca9)

2、刷新当前网页
![)KTLRHJQU DYR%2WK{4@HSF](https://github.com/xiaosuLiane/PixivDownload/assets/42183711/3f8a325f-f9fa-46a1-8123-d39e78cdc1eb)
3、随机点一个，找到有cookie的就复制cookie：后面的值
![R%F3O)7 )IYU$OG(GONI@ 4](https://github.com/xiaosuLiane/PixivDownload/assets/42183711/ab9f6a22-1234-4774-a1ae-f603ce59adfe)
![4KXT _IMS_3EMLZO _Z551](https://github.com/xiaosuLiane/PixivDownload/assets/42183711/27b80bd0-fee9-4a4c-aa3b-3f3b4be04d8f)

4、复制进脚本让你输入Cookie的地方回车即可。
