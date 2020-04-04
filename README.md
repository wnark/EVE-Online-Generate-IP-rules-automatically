# EVE-Online-Generate-IP-rules-automatically
本项目获取eve online域名对应的所有ip，储存并生成对应的rule文件

**本项目是 miyouzi/akamTester 的分支**

## 拿来即用

使用右键另存为 - 保存文件[Eve-online.rules](https://raw.githubusercontent.com/wnark/eve-online-Generate-IP-rules-automatically/master/Eve-online.rules "Eve-online.rules")

## 需要处理域名
```
tranquility.servers.eveonline.com
live.chat.eveonline.com
launcher.eveonline.com
resources.eveonline.com
binaries.eveonline.com
```


```Eve-online.rules``` 为最终生成的文件，适用sstap版本：1.0.9.7

**Eve-online.rules文件仅在本项目更新，偶尔在FQrabbit/SSTap-Rule内更新**
 


## 源码运行

安装依赖:
```
pip3 install requests beautifulsoup4 lxml termcolor pythonping dnspython IPy
```

执行 ```eve-online-rule.py```
```
python3 eve-online-rule.py
```

## 关于轮子

### GlobalDNS
```GlobalDNS``` 是个对域名进行全球解析的类, 使用 www.whatsmydns.net 的 API 进行解析，额外包含本地、谷歌、腾讯、阿里 DNS 的解析结果。

**导入**
```
from GlobalDNS import GlobalDNS
```

**使用**
```
akam = GlobalDNS('upos-hz-mirrorakam.akamaized.net')
ip_list = akam.get_ip_list()  # 取得全球解析结果, 返回一个 set
akam.renew()  # 重新解析
ip_list = akam.get_ip_list()  # 将返回最近一次全球解析的结果
```

### ColorPrinter
```ColorPrinter``` 染色输出工具, 可输出红绿及默认颜色(一般终端为白色), 可跨平台, 包括pyCharm中的运行窗口

**导入**
```
from ColorPrinter import color_print
```

**使用**
```
color_print('Hello World')  # 默认输出颜色
color_print('Hello World', status=1)  # 输出红色
color_print('Hello World', status=2)  # 输出绿色
```

### miyouzi/akamTester
使用它的轮子来获取每个域名的所有ip
```
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
```
