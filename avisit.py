#!/bin/usr/python
#coding by kadal-15
#remake please contact me 085336117892 / +6285336117892

import requests
from time import sleep
from bs4 import BeautifulSoup
import random
import sys


banner = '''
\033[1;32m   :##: \033[1;31m   ##:  :##                                       ©kadal-15
\033[1;32m    ##   \033[1;31m  ##    ##                                       v 1.2.5
\033[1;32m   ####  \033[1;31m  :##  ##:
\033[1;32m   ####   \033[1;31m :##  ##:
\033[1;32m  :#  #: \033[1;31m   ## .##
\033[1;32m   #::#  \033[1;31m   ##::## \033[0;37m             ##                  ##
\033[1;32m  ##  ##  \033[1;31m  ##::##           \033[0;37m   ""                  ""       ##
\033[1;32m  ###### \033[1;31m   :####:\033[0;37m  ##m  m##   ####     mm#####m   ####     #######
\033[1;32m .######. \033[1;31m  .####. \033[0;37m  ##  ##      ##     ##mmmm "     ##       ##
\033[1;32m :##  ##:  \033[1;31m  ####   \033[0;37m "#mm#"      ##      """"##m     ##       ##
\033[1;32m ###  ### \033[1;31m   ####   \033[0;37m  ####    mmm##mmm  #mmmmm##  mmm##mmm    ##mmm
\033[1;32m ##:  :##   \033[1;31m  ##    \033[0;37m   ""     """"""""   """"""   """"""""     """"
\033[1;33m===================================================================
\033[1;33m===================================================================
\033[1;34mAuthor By \033[1;0m :\033[1;32m Kadal-15    \033[1;30m                Istighfar Untuk Masa Lalu
\033[1;34mChannel YT\033[1;0m :\033[1;32m Jejaka Tutorial       \033[1;30m     Bersyukur Untuk Hari Ini
\033[1;34mWhatsapp  \033[1;0m :\033[1;32m 085336117892           \033[1;30m      Berdoa Untuk Masa Depan
'''
user_agent_list = [
   #Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)',
]

proxies_list = [
    'http://10.10.1.10:3128',
    'http://77.232.139.200:8080',
    'http://78.111.125.146:8080',
    'http://77.239.133.146:3128',
    'http://74.116.59.8:53281',
    'http://67.53.121.67:8080',
    'http://67.78.143.182:8080',
    'http://62.64.111.42:53281',
    'http://62.210.251.74:3128',
    'http://62.210.105.103:3128',
    'http://5.189.133.231:80',
    'http://46.101.78.9:8080',
    'http://45.55.86.49:8080',
    'http://40.87.66.157:80',
    'http://45.55.27.246:8080',
    'http://45.55.27.246:80',
    'http://41.164.32.58:8080',
    'http://45.125.119.62:8080',
    'http://37.187.116.199:80',
    'http://43.250.80.226:80',
    'http://43.241.130.242:8080',
    'http://38.64.129.242:8080',
    'http://41.203.183.50:8080',
    'http://36.85.90.8:8080',
    'http://36.75.128.3:80',
    'http://36.81.255.73:8080',
    'http://36.72.127.182:8080',
    'http://36.67.230.209:8080',
    'http://35.198.198.12:8080',
    'http://35.196.159.241:8080',
    'http://35.196.159.241:80',
    'http://27.122.224.183:80',
    'http://223.206.114.195:8080',
    'http://221.120.214.174:8080',
    'http://223.205.121.223:8080',
    'http://222.124.30.138:80',
    'http://222.165.205.204:8080',
    'http://217.61.15.26:80',
    'http://217.29.28.183:8080',
    'http://217.121.243.43:8080',
    'http://213.47.184.186:8080',
    'http://207.148.17.223:8080',
    'http://210.213.226.3:8080',
    'http://202.70.80.233:8080',

]
print (banner)
sleep(4)
print ('\033[1;36m\nExample : https://jejakakampret32.blogspot.com/2018/10/cara-mining-di-android-menggunakan.html')
sleep(2)
url = input('\033[1;31mMasukkan URL Blog Anda : ')
jml = int(input('Jumlah Visit: '))
time = int(input('Jeda : '))
print ('Try To Visit')
sleep(2)
for i in range(1, jml):
    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}
    proxies_a = random.choice(proxies_list)
    proxies = {'http': proxies_a}
    with requests.Session() as c:
         r = c.get (url, headers=headers, proxies=proxies)
         if r.status_code == requests.codes.ok:
            print ('\033[1;36m[\033[1;0m', i, '\033[1;36m] \033[1;34m[User-Agent]\033[1;0m ✔ \033[1;32m[Status]\033[1;0m', r.status_code, 'Ok \033[1;33m[Visit]\033[1;0m ==>\033[1;91m SUKSES :D')
            sleep(time)
         else:
            print ('\nCek URL Anda')
print ('Task Done')
