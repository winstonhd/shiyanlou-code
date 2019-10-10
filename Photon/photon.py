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
