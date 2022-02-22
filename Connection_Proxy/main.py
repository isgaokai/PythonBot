#coding=utf-8
import requests
import os

#请求地址
targetUrl = "https://www.xbiquge.la"

#代理服务器
proxyHost = "122.226.191.23"
proxyPort = "1"

proxyMeta = "http://%(host)s:%(port)s" % {

    "host" : proxyHost,
    "port" : proxyPort,
}
print(proxyMeta)
#pip install -U requests[socks]  socks5
# proxyMeta = "socks5://%(host)s:%(port)s" % {

#     "host" : proxyHost,

#     "port" : proxyPort,

# }

proxies = {
    "http": proxyMeta,
    "https": proxyMeta
}
resp = requests.get(targetUrl, proxies=proxies)
print(resp.text)
res = requests.get(url='http://httpbin.org/ip', proxies=proxies)
print(res.text)
