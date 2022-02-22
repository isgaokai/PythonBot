# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import requests
from lxml import etree
import gzip

ua = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        'Referer': 'http://wsgg.sbj.cnipa.gov.cn:9080/tmann/annInfoView/annSearch.html?annNum=1757',
        'cookie':'UM_distinctid=17bf277bf8e763-0ffbad3484099a-113f6757-129790-17bf277bf8f5fa; tmas_cookie=2272.7689.15400.0000; goN9uW4i0iKzS=54p9Oh5.nujnJ0R0cPqirtGqmxM8Pw5PubKqi_THKJH_OkYtSJAecv2MWdHnLwvB70xqjh1dClvFUFeiso93Biq; 018f9ebcc3834ce269=307cd64d3da74d84b192c7fbed332298; JSESSIONID=00005rqzNLjFRRQaAeYRFCIT7hd:1bm104p42; goN9uW4i0iKzT=53VA_gbmlHkLqqqm4ZL3hjqhOiMOYnWmsTOTI3PfqTwwXvTGUujVveRbV1t2dcaLtFDZGtWjUc0aeD4_SSuDTneIllah1DmM7YRT0H0ncrJgDMiykbbzEkrvUvZi6moCDnqkxRIrvq7nmwWt6Yps7QUcUcF79QadeDldlaQGJNuD4LWMBv46Gy9MdPa8k1Z1UWFTCc9hdjXRa4NdzX4r7v_TWV5GRGLediImd878Ro3K8zOTDfcvKZ5pKv6wqTwbgO1vY1EybCpqNFAfNYOWvTY',
        'Connection':'keep-alive',
        'Referer': 'http://wsgg.sbj.cnipa.gov.cn:9080/tmann/annInfoView/annSearch.html?annNum=1757',
        'Host':'Host: wsgg.sbj.cnipa.gov.cn:9080',
        'Content-Type': 'application/x-www-form-urlencoded'
}

data = {
        'page':'1',
        'rows':'2',
        'annMun':'1757',
        'totalYOrN':'true'
}
#test_url ='http://wsgg.sbj.cnipa.gov.cn:9080/tmann/annInfoView/annSearch.html?annNum=1757'
test_url = 'http://wsgg.sbj.cnipa.gov.cn:9080/tmann/annInfoView/annSearchDG.html?O56fzBVE=58rv890wQhEntMUJN1Bhkk65SfRMe_RWL4Jnsoa0tqnPViQWrRWb2Ag5BLZMvkrIKpMhTaypIhkP9osttolb0gbl0ND0ZQ8vytjUc8O130HUcaUwDMquVNOhIYx1KluT45royWtUoR3WX4w4cQ5.STI2NJYy2RbwkxmtpdIUqsYgelNHucDIjajQoTTFSti7oFGwBkySXejdAXfH2PJzK87xKN2fz5d4pS1r5IpYajV1AXsv22Hh8fdr9b0znH5xhJ5zcdvjLvrDD1VBstRC.gJAPSge72zS8vrLs88Ihe42hwnpeFvx4jspjOBgOn4HU'

test_res = requests.get(test_url, headers=ua,data=data)
test_res = test_res.content
test_res = test_res.decode()


# test_res = test_res.decode('gb')

print(test_res)
test_etree = etree.HTML(test_res)

goal_ = test_etree.xpath('//div[@class="jsJg"]/text()')
print(goal_)
