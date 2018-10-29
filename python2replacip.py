#!/usr/bin/python
# --*-- coding:utf-8 --*--
from socket import gethostbyname
list = ["host"]  #域名列表

"""for i in list:
    out = os.popen('ping -c 1 ' + str(i))
    print (out.read())"""
for host in list:
    ip = gethostbyname(host.strip('\n'))
    print(ip)

    with open("file path","r") as f:      #读取的源文件
        lines = f.readlines()
    with open("filenew path","w") as f_w:   #要更改的文件
        for line in lines:
            if str(host) in line:
                line = line.replace(str(host),str(ip))
            f_w.write(line)
f_w.close()
f.close()
