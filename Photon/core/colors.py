import sys

colors = True #输出默认是有颜色的
machine = sys.platform #检测当前操作系统类型
if machine.lower().startswith(('os', 'win', 'darwin', 'ios')):
	colors = False #在mac&windows&系统下，colors改为 False
if not colors:
	end = red = white = green = yellow = run = bad = good = info = que = '' #当在mac&Windows系统下，其他颜色都为空
else:
	white = '\033[97m'    # 白色
	green = '\033[92m'    # 绿色
	red = '\033[91m'    # 红色
	yellow = '\033[93m'    # 黄色
	end = '\033[0m'    # 结束
	back = '\033[7;91m'    # 黑色
	info = '\033[93m[!]\033[0m'    # 显示黄色的 [!]，表示信息提示
	que = '\033[94m[?]\033[0m'     # 显示蓝色的 [?]
	bad = '\033[91m[-]\033[0m'     # 显示红色的 [-]
	good = '\033[92m[+]\033[0m'    # 显示绿色的 [+]，表示成功
	run = '\033[97m[~]\033[0m'     # 显示白色的 [~]， 表示运行中
