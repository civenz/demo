# -*- coding: utf-8 -*-
# Passed - python 3.7

import io
import re
import sys
import random
import requests

###############################################################################
DEFAULT_ENCODING    = 'utf-8'
python2x                = re.search('^2.', sys.version)
python3x                = re.search('^3.', sys.version)
if python3x:
    sys.stdin           = io.TextIOWrapper(sys.stdin.detach(), encoding = DEFAULT_ENCODING)
    sys.stdout          = io.TextIOWrapper(sys.stdout.detach(), encoding = DEFAULT_ENCODING)
elif python2x:
    reload(sys)
    sys.setdefaultencoding(DEFAULT_ENCODING)
#-----------------------------------------------------------------------------#
try:
    locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )
except:
    pass
#-----------------------------------------------------------------------------#
## 设置递归深度 [Max value: Signed long value] ##
## Default maximum depth is: 1000 ##
sys.setrecursionlimit( sys.maxsize )
###############################################################################


###############################################################################
## 简化 HTML ##

def simpHtml( content ):
    if content and len( content ) > 0:

        content = content.strip()
        content = re.sub( '<!--[\d\D]*?-->', '', content )              # 去除注释 <!-- -->
        content = re.sub( '<head[\d\D]*?</head>', '', content )         # 去除标签 head
        content = re.sub( '<meta[\d\D]*?>', '', content )               # 去除标签 meta
        content = re.sub( '<link[\d\D]*?>', '', content )               # 去除标签 link
        content = re.sub( '<style[\d\D]*?</style>', '', content )       # 去除标签 style
        content = re.sub( '<script[\d\D]*?</script>', '', content )     # 去除标签 script
        content = re.sub( '<noscript[\d\D]*?</noscript>', '', content ) # 去除标签 noscript
        content = re.sub( '&nbsp;', ' ', content )                      # 替换 &nbsp; 为 空格

        #---------------------------------------------------------------------#
        content = re.sub( '\s+', ' ', content )                         # 替换 &nbsp; 为 空格
        content = re.sub( '> <', '><', content )
        #---------------------------------------------------------------------#

    return content

###############################################################################

###############################################################################
## GET 参数 ##
paramsCustom = {
    'key1': 'value1',
    'key2': ['value2', 'value3'],
}
#-----------------------------------------------------------------------------#
## POST 参数 ##
dataCustom = {'key':'value'}
#json.dumps(dataCustom)
#-----------------------------------------------------------------------------#
## 定制请求头 ##
userAgentList = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)',

    'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',

    'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
    'Mozilla/5.0 (compatible; Baiduspider-render/2.0; +http://www.baidu.com/search/spider.html)',
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',

    'Chrome/71.0.3578.98',
    'Firefox/60.0',
    'Internet Explorer 11.0',
    'Internet Explorer 7.0',
]
#-----------------------------------------------------------------------------#
headersCustom = {
    'User-Agent': random.choice(userAgentList),
    'Accept-Encoding': 'gzip, deflate',
}
#-----------------------------------------------------------------------------#
## 禁止重定向 ##
# allow_redirects = False
## 超时设置 connect 和 read ##
timeoutCustom = (10, 120)
#-----------------------------------------------------------------------------#
## 设置代理访问,可以直接使用 SOCKS5
proxiesList = {
    #"http": "http://127.0.0.1:8899",
    #"https": "https://127.0.0.1:8899",
}
#-----------------------------------------------------------------------------#

## 调试 HTTP(S) 请求的页面 ##
url = 'http://httpbin.org/cache'

#-----------------------------------------------------------------------------#

dataCustom = False # [GET方法请求, 出现错误 - 411 Length Required] 需要设置为 False
r = requests.request('GET', url, data = dataCustom, params = paramsCustom, headers = headersCustom, timeout = timeoutCustom, proxies=proxiesList)

###############################################################################

###############################################################################
## ++++++++ 解决乱码 Start ++++++++ ##

#-----------------------------------------------------------------------------#
## 日文: Windows-1254 乱码解决; 其他语言如果出现乱码可以参考此方法:
#### 01. 将[真实编码]为 Windows-1254 的[网页编码]设置成 SHIFT_JIS
#### 02. 其他[网页编码]的页面直接设置成[真实编码]

## 查看 [真实编码] ##
#print(r.apparent_encoding)

if r.apparent_encoding == 'Windows-1254':
    r.encoding = 'SHIFT_JIS'
#-----------------------------------------------------------------------------#
else:
    r.encoding = r.apparent_encoding
#-----------------------------------------------------------------------------#

## ++++++++ 解决乱码 End ++++++++ ##
###############################################################################

###############################################################################
## 保存请求 URL 的内容 ##

#-----------------------------------------------------------------------------#
if r.headers['Content-Type'].lower() == 'text/html':
    pass
if r.headers['Content-Type'].lower() == 'application/json':
    pass
#-----------------------------------------------------------------------------#

content = simpHtml(r.text)
f = open('demo.html.txt', 'a', encoding = DEFAULT_ENCODING)
f.write(content + '\n')
f.close()
###############################################################################

if __name__ == '__main__':
    print('抓取结果请查看: demo.html.txt')
    #input("按 【回车键】 退出！")




'''
###############################################################################
[真实编码] request.apparent_encoding | 网页源码 <meta charset="utf-8"> 的[网页编码]
-------------------------------------------------------------------------------
UTF-8        | HTML Charset: GB2312     - https://www.sina.com/
GB2312       | HTML Charset: GB2312     - https://www.qq.com/
-------------------------------------------------------------------------------
UTF-8        | HTML Charset: UTF-8      - http://www.nihon-u.ac.jp
Windows-1254 | HTML Charset: Shift_JIS  - http://charset.7jp.net/sjis.html
SHIFT_JIS    | HTML Charset: Shift_JIS  - http://www.russel.co.jp/hp/adult/clover_hearts/clover_top.html
Big5         | Big5                     - http://ch.gcforum.org.tw/
windows-1251 | windows-1251             - http://www.softtime.ru/forum/
-------------------------------------------------------------------------------
testString = 'përshëndetje » cześć » привет » Hallå » 안녕하세요 » こんにちは http://www.ebay.com/fashion/ € £ ß 哈 哈 球'
-------------------------------------------------------------------------------
code page   - http://en.wikipedia.org/wiki/Code_page
    932     - Janpanese
    936     - Simplified Chinese
    949     - Korean
    950     - Traditional Chinese
    1251    - Russian [Cyrillic alphabet]
###############################################################################
'''