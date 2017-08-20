import time
import urllib
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import random
import re

import string
import os

class Zhanlang(object):

    def __init__(self):
        self.user_agent_list=["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
 "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
 "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
 "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
 "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
 "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
 "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
 "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
 "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
 "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
 "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
 "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
 "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
        self.iplist =['220.166.240.90:8118', '182.88.27.67:8118', '183.10.143.71:8118', '42.84.254.52:80', '60.255.186.169:8888', '218.27.168.81:8118', '106.44.80.17:8118', '122.72.32.88:80', '42.231.174.138:8118', '175.42.102.252:8118', '49.87.224.204:8118', '61.160.6.158:81', '115.48.34.140:80', '115.234.212.213:8118', '122.192.66.50:808', '122.72.32.74:80', '60.214.118.170:63000', '110.73.14.192:8123', '171.39.73.194:8123', '180.175.219.46:63000', '119.115.234.156:8118', '124.166.179.132:8118', '60.178.125.126:8118', '171.118.110.36:8118', '112.114.77.173:8118', '180.107.172.244:8118', '27.43.166.5:80', '112.114.92.19:8118', '123.171.5.99:65309', '112.85.88.76:9131', '220.174.141.204:8118', '27.40.147.35:808', '113.123.93.7:8118', '39.75.49.63:8118', '112.123.248.155:9745', '171.39.112.17:8123', '182.242.171.36:8118', '221.219.30.214:8118', '180.140.167.214:8118', '175.167.238.128:5767', '182.35.237.50:8118', '120.8.82.191:80', '118.72.29.214:80', '111.155.116.220:8123', '36.57.90.108:808', '27.43.166.110:80', '110.73.54.255:8123', '175.173.109.85:8118', '125.127.144.236:8118', '110.72.19.175:8123', '115.225.200.161:8118', '60.176.205.21:8888', '122.72.32.72:80', '115.46.250.95:8123', '101.94.200.52:8123', '182.90.105.125:8123', '121.31.147.221:8123', '121.31.87.89:8123', '111.155.116.233:8123', '119.184.149.106:8118', '175.154.84.115:8118', '180.175.0.112:63000', '180.175.0.112:63000', '111.155.116.239:8123', '115.215.51.12:8118', '117.78.51.231:3128', '61.178.238.122:63000', '123.146.99.123:65309', '110.83.60.76:53281', '112.64.102.157:8118', '42.178.228.67:80', '111.155.116.200:8123', '121.31.151.174:8123', '121.31.193.162:8123', '112.114.99.96:8118', '112.123.249.51:9745', '112.114.77.249:8118', '112.114.78.156:8118', '113.227.71.175:80', '180.175.95.189:63000', '59.32.43.178:53281', '27.185.148.223:8118', '110.216.60.43:80', '58.40.131.10:8118', '125.81.79.40:8123', '182.90.116.96:8123', '111.155.116.196:8123', '183.16.28.173:8123', '114.107.16.34:808', '112.85.44.20:8118', '110.73.6.254:8123', '117.68.192.230:808', '110.72.36.136:8123', '110.51.136.212:80', '121.31.156.55:8123', '58.49.123.86:53281', '221.204.72.56:80', '49.70.167.28:8118', '182.112.20.2:8118', '110.72.19.145:8123', '117.64.237.107:808', '42.122.179.154:8998', '121.31.137.41:8123', '182.90.107.188:8123', '121.31.100.56:8123', '171.38.66.124:8123', '110.73.7.248:8123', '110.73.52.108:8123', '113.233.82.50:80', '218.56.236.50:8118', '27.194.220.230:8118', '123.185.131.73:8118', '124.152.251.147:7895', '222.195.76.103:80', '182.90.78.86:8123', '110.73.10.97:8123', '119.118.81.192:80', '112.114.78.118:8118', '36.40.80.103:80', '111.155.116.207:8123', '49.75.91.216:808', '113.123.27.254:808', '117.80.232.228:8118', '1.196.143.156:8998', '122.228.179.178:80', '117.92.122.143:808', '114.228.36.177:8118', '182.246.210.233:80', '112.85.11.171:9131', '112.114.97.207:8118', '110.18.207.178:80', '39.64.41.36:8118', '117.92.122.143:808', '117.92.197.150:808', '122.233.192.251:8118', '112.85.10.65:9131', '112.85.3.147:9131', '113.121.43.172:808', '112.85.11.248:9131', '110.73.52.248:8123', '112.114.96.19:8118', '171.38.65.170:8123', '182.241.107.67:8118', '110.73.3.231:8123', '171.38.5.196:8123', '219.144.61.61:80', '110.72.32.106:8123', '110.73.4.206:8123', '171.39.30.142:8123', '42.87.167.33:80', '112.114.96.255:8118', '112.114.92.63:8118', '116.248.161.175:80', '121.31.101.53:8123', '110.73.48.4:8123', '111.195.231.50:8123', '175.174.83.232:80', '182.88.91.165:8123', '60.24.157.103:8118', '140.250.142.29:808', '39.68.16.101:8118', '61.135.155.82:443', '60.13.14.134:7895', '111.224.84.70:8118', '111.155.116.238:8123', '112.114.96.9:8118', '112.114.92.161:8118', '112.85.2.141:9131', '180.213.187.127:53281', '110.73.55.111:8123', '182.88.167.94:8123', '121.57.27.36:8118', '110.73.3.73:8123', '110.73.0.79:8123', '120.26.121.109:80', '175.44.46.96:65309', '112.114.93.228:8118', '110.73.14.26:8123', '110.73.35.8:8123', '110.73.9.216:8123', '112.85.106.182:9131', '182.88.88.28:8123', '110.73.6.63:8123', '121.31.139.89:8123', '111.155.124.72:8123', '110.73.32.232:8123', '182.88.135.249:8123', '42.84.176.141:53281', '111.155.116.236:8123', '140.237.115.15:808', '112.85.9.241:9131', '125.123.239.93:8998', '112.85.56.202:9131', '119.162.50.35:8118', '221.7.175.149:8123', '182.88.185.91:8123', '112.85.72.25:9131', '110.73.9.40:8123', '112.85.110.110:9131', '112.85.11.81:9131', '110.73.2.116:8123', '110.73.29.50:8123', '112.85.106.238:9131', '110.73.3.218:8123', '110.73.9.145:8123', '110.51.214.119:80', '110.73.2.208:8123', '110.73.0.239:8123', '111.155.116.217:8123', '112.85.72.199:9131', '112.114.93.18:8118', '101.25.243.107:80', '101.25.186.44:80', '175.162.119.21:53281', '111.224.107.100:808', '27.214.244.147:8118', '171.88.42.118:53281', '110.73.11.172:8123', '182.88.4.164:8123', '111.155.116.229:8123', '58.45.203.71:80', '110.73.13.180:8123', '112.85.107.183:9131', '110.72.22.109:8123', '112.85.3.75:9131', '112.114.95.241:8118', '110.73.5.128:8123', '110.73.10.207:8123', '112.85.74.9:9131', '112.114.96.215:8118', '112.85.108.174:9131', '112.114.95.64:8118', '182.88.129.113:8123', '114.239.148.232:808', '112.85.106.12:9131', '110.73.14.34:8123', '182.90.58.251:8123', '110.73.33.20:8123', '112.85.88.109:9131', '111.195.35.205:8123', '171.37.166.197:8123', '115.46.79.140:8123', '182.88.164.172:9999', '218.18.232.29:8080', '112.232.187.2:8118', '121.31.149.9:8123', '110.73.55.70:8123', '153.37.94.96:80', '110.73.7.134:8123', '110.73.5.236:8123', '110.73.28.89:8123', '125.81.187.130:8123', '112.114.98.79:8118', '110.72.27.7:8123', '112.85.109.91:9131', '113.123.119.199:808', '112.85.84.145:9131', '175.16.65.24:80', '112.114.93.23:8118', '183.53.134.225:5853', '111.155.116.211:8123', '110.73.54.187:8123', '112.114.99.104:8118', '112.85.85.170:9131', '42.84.226.46:80', '112.85.87.155:9131', '115.215.214.22:8118', '112.85.111.0:9131', '110.73.51.202:8123', '112.85.110.204:9131', '182.88.88.169:8123', '114.228.155.122:808', '110.73.29.63:8123', '121.31.153.114:8123', '110.73.49.31:8123', '116.226.223.110:63000', '112.114.97.82:8888', '1.82.154.234:80', '112.85.10.162:9131', '112.114.92.140:8118', '112.254.124.23:8118', '221.200.69.200:80', '121.31.149.37:8123', '118.79.52.193:80', '112.85.84.208:9131', '110.73.54.41:8123', '110.73.48.111:8123', '110.73.1.202:8123', '121.31.88.49:8123', '121.31.73.97:8123', '112.85.75.242:9131', '115.46.117.164:8123', '110.73.48.188:8123', '180.110.254.100:3128', '115.46.77.214:8123', '182.90.17.172:80', '115.46.64.91:8123', '125.211.202.26:53281', '115.213.240.19:808', '115.219.3.172:53281']


    def Url(self):
        url_duan = "https://movie.douban.com/subject/26363254/reviews?start="
        start_urls = [url_duan + str((i - 1) * 20) for i in range(1, 342)]
        for url in start_urls:
            self.spider(url)

    def data(self):
        #cookie = open("cookie.txt", "r")
        ua = random.choice(self.user_agent_list)
        data = {
            "Accept": "text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, * / *;q = 0.8",
            "Accept - Encoding": "gzip, deflate, sdch, br",
            "Accept - Language": "zh - CN, zh;q = 0.8, en;q = 0.6",
            "Connection": "keep - alive",
            #"cookie": cookie,
            "Host": "movie.douban.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": ua,
            }
        data = urllib.parse.urlencode(data).encode('utf-8')
        return data

    def spider(self,url):
        time.sleep(2)
        proxy_support = urllib.request.ProxyHandler({'sock5':random.choice(self.iplist)})
        opener = urllib.request.build_opener(proxy_support)
        urllib.request.install_opener(opener)
        html = opener.open(url, data= self.data())
        htm = html.read().decode("utf-8")
        soup = BeautifulSoup(htm,"lxml")
        reviewer_urls = soup.find_all('a', 'title-link')
        reviewer_url =[]
        for i in range(len(reviewer_urls)):
            reviewer_url.append(reviewer_urls[i]['href'])
        #print(reviewer_url)
        for i in range(len(reviewer_url)):
            #print(reviewer_url[i])
            self.spider_1(reviewer_url[i])

    def spider_1(self,url):
        proxy_support = urllib.request.ProxyHandler({'sock5':random.choice(self.iplist)})
        opener = urllib.request.build_opener(proxy_support)
        urllib.request.install_opener(opener)
        f = oener.open(url,data= self.data(),timeout=10)
        soup = BeautifulSoup(f.read().decode('utf-8'), 'lxml')
        #得到评论人
        reviewer = soup.find_all('span', property='v:reviewer')[0].get_text()
        #if not os.path.exists(reviewer+'.txt'):
            #exit()
        string_1 = string.punctuation
        for str_1 in string:
            reviewer= reviewer.replace(str_1,'')
        content = []
        ##方法一：之前只知道用find_all，不知道find，所以用之前的方法，现在利用find和find_all的组合试试,但是必须将结果修改为字符串才行。
        content_1 = soup.find('div', property='v:description').find_all('p')
        for i in range(len(content_1)):
            content.append(content_1[i].string)
        with open(reviewer+'.txt', 'w+', encoding= 'utf-8') as f:
            for i in range(len(content)):
                try:
                    f.write(content[i]+'\n')
                except TypeError as e:
                    f.write('\n')
        #os.mknod('/ping/'+reviewer+'.txt')

'''
        ##方法二：将content的内容变为字符串，再利用re的正则sub删掉不符合的东西，看起来有点乱，写得有点多。
        content = soup.find_all('div',property='v:description')
        str_content = str(content)
        str1=re.sub('<.*?>','',str_content)
        str2 = str1.strip('[]')
        content_a = str2.strip('\n')
        with open(reviewer+'.txt', 'w', encoding= 'utf-8') as f:
            f.write(content_a)
'''

if __name__ == "__main__":
    main = Zhanlang()
    main.Url()

