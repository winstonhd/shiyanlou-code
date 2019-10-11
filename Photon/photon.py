#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function #这个语句是Python2的概念，Python2是future，在Python2的环境下超前使用Python3的print 函数
from core.colors import bad, good, info, run, green, red, white, end

import argparse #命令行参数解析
import warnings #警告信息

#打印 banner
print('''%s   ___  __    _
      /%s__%s \/ /_ ___ //____ ___
     /%s/_/%s /__\/%s__%s\/ __/%s__%s \/ __\\ 
    / ___/ / / / %s/_/%s / / _/ %s/_/%s / / / /
   /__/  /_/ /_/\___/\___/\___/ _/ /_/%s1.2.1%s\n''' %(red, white, red, white, red, white, red, white, red, white, red, white, red, white, end))

#不打印匹配的警告
warnings.filterwarnings('ignore')

#创建解析步骤
parser = argparse.ArgumentParser()

#添加参数步骤
parser.add_argument('-u', '--url', help = 'root url', dest='root') #dest:参数别名
parser.add_argument('-c', '--cookie', help =  'cookie', dest = 'cook')
parser.add_argument('-r', '--regex', help = 'regex pattern', dest = 'regex')
parser.add_argument('-e', '--export', help = 'export format', dest = 'export')
parser.add_argument('-o', '--output', help = 'output directory', dest = 'output')
parser.add_argument('-l', '--level', help = 'level to crawl', dest = 'level', type = int)#type：参数类型
parser.add_argument('-t', '--threads', help = 'number of threads', dest = 'threads', type = int)
parser.add_argument('-d', '--delay', help = 'delay between requests', dest = 'delay', type = float)
parser.add_argument('-s', '--seeds', help = 'additional seed URLs', dest = 'seeds', nargs = "+", default = [])#nargs 应该读取的命令行参数个数，+表示一个或多个参数
parser.add_argument('--user-agent', help = 'custom user agent(s)', dest = 'user_agent')
parser.add_argument('--exclude', help = 'exclude URLs matching this regex',dest = 'exclude')
parser.add_argument('--timeout', help = 'http request timeout', dest = 'timeout', type = float)

#其他参数
parser.add_argument('--headers', help = 'add headers', dest = 'headers', action = 'store_true')
parser.add_argument('--dns', help = 'enumerate subdomains and DNS data', dest = 'dns', action='store_true')
parser.add_argument('--ninja', help = 'ninja mode', dest = 'ninja', action = 'store_true')
parser.add_argument('--keys', help = 'find secret keys', dest = 'api', action = 'store_true')
parser.add_argument('--only-urls', help = 'only extact URLs', dest = 'only_urls', action = 'store_true')
args = parser.parse_args() #返回一个命令空间，如果想要使用变量，可用 args.attr

headers = args.headers #提供headers
delay = args.delay or 0 #请求延时，默认为0
timeout = args.timeout or 6 #http请求超时，默认为6
cook = args.cook or None # Cookie,默认为None
api = bool(args.api) #判断是否有api，是布尔类型
ninja = bool(args.ninja) #切换Ninja模式
crawl_level = args.level or 2 #爬取的层数，默认为2层
thread_count =args.threads or 2 #线程数，默认值为2个线程
only_urls = bool(args.only_urls) #only_urls默认为False

keys = set() #秘钥
files = set() #pdf, css, png等类型的文件
intel = set() #邮箱地址，网站账号等网络相关信息
robots = set() #robots.txt 文件
custom = set() #由自定义的正则表达式匹配的字符串
faild = set() #没有成功爬取的URLs
scripts = set() #JS文件
external = set() #不属于目标网站范围的URLs
fuzzable = set() #已在其中获取参数的网址，比如：example.com/page.php
endpoints = set() #从js文件中找到的URLs
processed = set() #已爬取过的URLs
internal = set([s for s in args.seeds]) #属于目标网站范围内的URLs

bad_intel = set() #失效的网站URLs
bad_scripts = set() #失效的js文件URLs













