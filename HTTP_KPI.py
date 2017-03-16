#探测HTTP服务质量
import os, sys
import time
import pycurl

URL = "http://www.baidu.com"
c = pycurl.Curl()
#定义请求的URL常量
c.setopt(pycurl.URL, URL)
#定义请求连接的等待时间
c.setopt(pycurl.CONNECTTIMEOUT, 5)
#定义请求超时
c.setopt(pycurl.TIMEOUT, 5)
#屏蔽下载进度条
c.setopt(pycurl.NOPROGRESS, 1)
#完成交互后强制断开连接，不重用
c.setopt(pycurl.FORBID_REUSE, 1)
#指定HTTP重定向最大数
c.setopt(pycurl.MAXREDIRS, 1)
#设置DNS缓存有效期为30秒
c.setopt(pycurl.DNS_CACHE_TIMEOUT, 30)
indexfile = open(os.path.dirname(os.path.realpath(__file__))+"/content.txt","wb")
#将返回的HTTP HEADER定向到indexfile文件对象
c.setopt(pycurl.WRITEHEADER, indexfile)
#HTML内容也定向到indexfile
c.setopt(pycurl.WRITEDATA, indexfile)
try:
    #提交请求
    c.perform()
except Exception as e:
    print("connection error: {}".format(e))
    indexfile.close()
    c.close()
    sys.exit()

#获取DNS解析时长
NAMELOOKUP_TIME = c.getinfo(c.NAMELOOKUP_TIME)
#建立连接时长
CONNECT_TIME = c.getinfo(c.CONNECT_TIME)
#从建立连接到准备传输消耗时长
PRETRANSFER_TIME = c.getinfo(c.PRETRANSFER_TIME)
#从建立连接到传输开始消耗时长
STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)
#传输的总时长
TOTAL_TIME = c.getinfo(c.TOTAL_TIME)
HTTP_CODE = c.getinfo(c.HTTP_CODE)
SIZE_DOWNLOAD = c.getinfo(c.SIZE_DOWNLOAD)
HEADER_SIZE = c.getinfo(c.HEADER_SIZE)
#平均下载速度
SPEED_DOWNLOAD = c.getinfo(c.SPEED_DOWNLOAD)

print("{}\n{}\n{}\n{}\n{}\n{}\n{}Bytes\n{}Bytes\n{}Bytes/s".format(NAMELOOKUP_TIME,CONNECT_TIME,PRETRANSFER_TIME,STARTTRANSFER_TIME,TOTAL_TIME,HTTP_CODE,SIZE_DOWNLOAD,HEADER_SIZE,SPEED_DOWNLOAD))
indexfile.close()
c.close()
