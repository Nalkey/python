#Monitor the availability of the service IP
import http.client
import os
import dns.resolver

#定义域名IP列表和业务域名
iplist = []
#www.baidu.com返回CNAME类型记录www.a.shifen.com.
appdomain = "www.a.shifen.com."

#域名解析并把IP加入iplist
def get_iplist(domain=""):
    try:
        #解析A类型记录
        A = dns.resolver.query(domain, 'A')
    except Exception as e:
        print("dns resolver error:{}".format(e))
        return
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)
    return True

def checkip(ip):
    checkurl = ip + ':80'
    getcontent = ""
    #定义HTTP连接超时为5秒
    http.client.socket.setdefaulttimeout(5)
    #创建http连接对象
    conn = http.client.HTTPConnection(checkurl)
    try:
        conn.request("GET", "/", headers = {"Host": ip})
        r = conn.getresponse()
        #获取页面前15个字符
        getcontent = r.read(15).decode('utf-8')
    finally:
        #当前15个字符与此处定义字符串相同时，判断连接良好
        if getcontent == "<!DOCTYPE html>":
            print("{} [OK]".format(ip))
        else:
            print("{} [ERROR]".format(ip))

if __name__ == "__main__":
    if get_iplist(appdomain) and len(iplist) > 0:
        for ip in iplist:
            checkip(ip)
    else:
        print("dns resolver error.")
