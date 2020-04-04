#!/usr/bin/env python3
# _*_ coding : UTF-8 _*_
# 开发团队 ：寒夜方舟
# 开发人员 ：寒夜方舟
# 开发时间 ：2020/4/3 21:03
# 文件名称 ：eve-online-rule.py
# 开发工具 ：Visual Studio Code


""" 
主要是处理：
live.chat.eveonline.com
launcher.eveonline.com
resources.eveonline.com
binaries.eveonline.com

tranquility.servers.eveonline.com
已确定ip为87.237.34.200，应该不会变 ，但我还是让他获取吧
"""


import os
import sys
import argparse
import shutil      ##复制
from GlobalDNS import GlobalDNS     ##用来获取域名对应的所有ip
from ColorPrinter import color_print        ##增加颜色对比度
from IPy import IP                  ##处理ip地址

##表示版本
version = 0.1

version_msg = '当前eve-online-rule.py版本: ' + str(version)
color_print(version_msg, 2)

##载入临时储存ip文件，是akamTester.py原本的内容
working_dir = os.path.dirname(os.path.realpath(__file__))
ip_list_path = os.path.join(working_dir, 'ip_list.txt')

##第一个域名-live.chat.eveonline.com
host = 'live.chat.eveonline.com'
##开始获取ip，原作者是用-u参数允许别人提交，但我这个是仅供eve使用的，就不需要了
##下面是直接用akamTester.py内的写好的模块，我直接拿来用了，减少后面维护成本
try:
    akam = GlobalDNS(host)
    color_print('第一次解析:')
    ip_list = akam.get_ip_list()
    print()
    color_print('第二次解析:')
    akam.renew()
    ip_list = ip_list | akam.get_ip_list()
    print()
    color_print('第三次解析:')
    akam.renew()
    ip_list = ip_list | akam.get_ip_list()
except BaseException as e:
    color_print('进行全球解析时遇到未知错误: '+str(e), status=1)
    if os.path.exists(ip_list_path):
        color_print('将读取本地保存的ip列表', status=1)
        with open(ip_list_path, 'r', encoding='utf-8') as f:
            ip_list = f.read().splitlines()
    else:
        color_print('没有本地保存的ip列表！程序终止！', status=1)
        print()
        input('按回车退出')
        sys.exit(0)
else:
    # 保存解析结果
    with open(ip_list_path, 'w', encoding='utf-8') as f:
        for ip in ip_list:
            f.write(str(ip))
            f.write('\n')

##将临时ip_list.txt文件复制到一边live.txt
shutil.copyfile('ip_list.txt','live.txt')
##获取live.chat.eveonline.com的ip完成
print()
color_print('共取得 '+str(len(ip_list))+' 个 IP, 开始获取launcher.eveonline.com的IP')
print()






##第二个域名-launcher.eveonline.com
host = 'launcher.eveonline.com'
##开始获取ip，原作者是用-u参数允许别人提交，但我这个是仅供eve使用的，就不需要了
##下面是直接用akamTester.py内的写好的模块，我直接拿来用了，减少后面维护成本
try:
    akam = GlobalDNS(host)
    color_print('第一次解析:')
    ip_list = akam.get_ip_list()
    print()
    color_print('第二次解析:')
    akam.renew()
    ip_list = ip_list | akam.get_ip_list()
    print()
    color_print('第三次解析:')
    akam.renew()
    ip_list = ip_list | akam.get_ip_list()
except BaseException as e:
    color_print('进行全球解析时遇到未知错误: '+str(e), status=1)
    if os.path.exists(ip_list_path):
        color_print('将读取本地保存的ip列表', status=1)
        with open(ip_list_path, 'r', encoding='utf-8') as f:
            ip_list = f.read().splitlines()
    else:
        color_print('没有本地保存的ip列表！程序终止！', status=1)
        print()
        input('按回车退出')
        sys.exit(0)
else:
    # 保存解析结果
    with open(ip_list_path, 'w', encoding='utf-8') as f:
        for ip in ip_list:
            f.write(str(ip))
            f.write('\n')

##将临时ip_list.txt文件复制到一边launcher.txt
shutil.copyfile('ip_list.txt','launcher.txt')
##获取launcher.eveonline.com的ip完成
print()
color_print('共取得 '+str(len(ip_list))+' 个 IP, 开始获取resources.eveonline.com的IP')
print()






##第三个域名-resources.eveonline.com
host = 'resources.eveonline.com'
##开始获取ip，原作者是用-u参数允许别人提交，但我这个是仅供eve使用的，就不需要了
##下面是直接用akamTester.py内的写好的模块，我直接拿来用了，减少后面维护成本
try:
    akam = GlobalDNS(host)
    color_print('第一次解析:')
    ip_list = akam.get_ip_list()
    print()
    color_print('第二次解析:')
    akam.renew()
    ip_list = ip_list | akam.get_ip_list()
    print()
    color_print('第三次解析:')
    akam.renew()
    ip_list = ip_list | akam.get_ip_list()
except BaseException as e:
    color_print('进行全球解析时遇到未知错误: '+str(e), status=1)
    if os.path.exists(ip_list_path):
        color_print('将读取本地保存的ip列表', status=1)
        with open(ip_list_path, 'r', encoding='utf-8') as f:
            ip_list = f.read().splitlines()
    else:
        color_print('没有本地保存的ip列表！程序终止！', status=1)
        print()
        input('按回车退出')
        sys.exit(0)
else:
    # 保存解析结果
    with open(ip_list_path, 'w', encoding='utf-8') as f:
        for ip in ip_list:
            f.write(str(ip))
            f.write('\n')

##将临时ip_list.txt文件复制到一边resources.txt
shutil.copyfile('ip_list.txt','resources.txt')
##获取resources.eveonline.com的ip完成
print()
color_print('共取得 '+str(len(ip_list))+' 个 IP, 开始获取binaries.eveonline.com的IP')
print()






##第四个域名-binaries.eveonline.com
host = 'binaries.eveonline.com'
##开始获取ip，原作者是用-u参数允许别人提交，但我这个是仅供eve使用的，就不需要了
##下面是直接用akamTester.py内的写好的模块，我直接拿来用了，减少后面维护成本
try:
    akam = GlobalDNS(host)
    color_print('第一次解析:')
    ip_list = akam.get_ip_list()
    print()
    color_print('第二次解析:')
    akam.renew()
    ip_list = ip_list | akam.get_ip_list()
    print()
    color_print('第三次解析:')
    akam.renew()
    ip_list = ip_list | akam.get_ip_list()
except BaseException as e:
    color_print('进行全球解析时遇到未知错误: '+str(e), status=1)
    if os.path.exists(ip_list_path):
        color_print('将读取本地保存的ip列表', status=1)
        with open(ip_list_path, 'r', encoding='utf-8') as f:
            ip_list = f.read().splitlines()
    else:
        color_print('没有本地保存的ip列表！程序终止！', status=1)
        print()
        input('按回车退出')
        sys.exit(0)
else:
    # 保存解析结果
    with open(ip_list_path, 'w', encoding='utf-8') as f:
        for ip in ip_list:
            f.write(str(ip))
            f.write('\n')

##将临时ip_list.txt文件复制到一边binaries.txt
shutil.copyfile('ip_list.txt','binaries.txt')
##获取binaries.eveonline.com的ip完成
print()
color_print('共取得 '+str(len(ip_list))+' 个 IP, 开始获取tranquility.servers.eveonline.com的IP')
print()






##第五个域名-tranquility.servers.eveonline.com
host = 'tranquility.servers.eveonline.com'
##开始获取ip，原作者是用-u参数允许别人提交，但我这个是仅供eve使用的，就不需要了
##下面是直接用akamTester.py内的写好的模块，我直接拿来用了，减少后面维护成本
try:
    akam = GlobalDNS(host)
    color_print('第一次解析:')
    ip_list = akam.get_ip_list()
    print()
    color_print('第二次解析:')
    akam.renew()
    ip_list = ip_list | akam.get_ip_list()
    print()
    color_print('第三次解析:')
    akam.renew()
    ip_list = ip_list | akam.get_ip_list()
except BaseException as e:
    color_print('进行全球解析时遇到未知错误: '+str(e), status=1)
    if os.path.exists(ip_list_path):
        color_print('将读取本地保存的ip列表', status=1)
        with open(ip_list_path, 'r', encoding='utf-8') as f:
            ip_list = f.read().splitlines()
    else:
        color_print('没有本地保存的ip列表！程序终止！', status=1)
        print()
        input('按回车退出')
        sys.exit(0)
else:
    # 保存解析结果
    with open(ip_list_path, 'w', encoding='utf-8') as f:
        for ip in ip_list:
            f.write(str(ip))
            f.write('\n')

##将临时ip_list.txt文件复制到一边tranquility.txt
shutil.copyfile('ip_list.txt','tranquility.txt')
##获取tranquility.servers.eveonline.com的ip完成
print()
color_print('共取得 '+str(len(ip_list))+' 个 IP, 已获取所有IP，开始处理生成规则文件')
print()





##合并live.txt|launcher.txt|resources.txt|binaries.txt|tranquility.txt
##tranquility.txt与live.txt使用指定ip
##launcher.txt|resources.txt|binaries.txt最后一位处理成0/24

##清空文件eve_online_ip.txt
eve_online_ip = open('eve_online_ip.txt','w+')
eve_online_ip.close()

with open('launcher.txt','r') as file3, open('eve_online_ip.txt','a+') as file6:
    while True:                             ##开始处理launcher.txt
        launcher = file3.readline()         ##循环读取ip好处理
        if '.' in launcher:                                     ##如果读取到内包含'.'，则代表是ip，可以转换
            eve_online_ip = IP(launcher).make_net('255.255.255.0')      ##将ip转换成0/24格式
            file6.write(str(eve_online_ip)+'\n')                                  ##将处理好的ip换行追加到综合所有ip的文件内
        else:
            break

with open('resources.txt','r') as file4, open('eve_online_ip.txt','a+') as file6:
    while True:                            ##开始处理resources.txt
        resources = file4.readline()         ##循环读取ip好处理
        if '.' in resources:                                     ##如果读取到内包含'.'，则代表是ip，可以转换
            eve_online_ip = IP(resources).make_net('255.255.255.0')      ##将ip转换成0/24格式
            file6.write(str(eve_online_ip)+'\n')                                  ##将处理好的ip换行追加到综合所有ip的文件内
        else:
            break

with open('binaries.txt','r') as file5, open('eve_online_ip.txt','a+') as file6:
    while True:                            ##开始处理binaries.txt
        binaries = file5.readline()         ##循环读取ip好处理
        if '.' in binaries:                                     ##如果读取到内包含'.'，则代表是ip，可以转换
            eve_online_ip = IP(binaries).make_net('255.255.255.0')      ##将ip转换成0/24格式
            file6.write(str(eve_online_ip)+'\n')                                  ##将处理好的ip换行追加到综合所有ip的文件内
        else:
            break

##删除eve_online_ip.txt重复的ip段,生成Eve-online.rules
##清空文件Eve-online.rules
eve_online_rule = open('Eve-online.rules','w+',encoding='utf-8')
eve_online_rule.write('#Eve-online,Eve-online欧服,0,0,1,0,0,0,By-寒夜方舟'+'\n')
eve_online_rule.close()

with open('eve_online_ip.txt','r') as file7,open('tranquility.txt','r') as file8, open('live.txt','r') as file9, open('Eve-online.rules','a+') as file10 :
    eve_online_ip = file7.readlines()
    file10.writelines(set(eve_online_ip))       ##去重并写入rule文件
    while True:
        live = file9.readline()         ##循环读取聊天服务器使用的ip
        if '.' in live:
            live = live.replace('\n','')
            live = live+'/32'+'\n'
            file10.writelines(str(live))           ##写入规则
        else:
            break
    while True:
        tranquility = file8.readline()          ##循环读取游戏服务器使用的ip
        if '.' in tranquility:
            tranquility = tranquility.replace('\n','')
            tranquility = tranquility+'/32'+'\n'
            file10.writelines(str(tranquility))        ##写入规则
        else:
            break


print()
input('Eve-online.rules生成完成'+'\n'+'请将Eve-online.rules文件复制到rule文件夹中'+'\n'+'按回车退出')
sys.exit(0)