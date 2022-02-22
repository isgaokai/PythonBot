# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import requests
from lxml import etree

headers = {
    'authority': 'pvp.qq.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://pvp.qq.com/raiders/',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,zh-HK;q=0.6',
    'cookie': 'RK=oxAVl3q7Ud; ptcz=2f08b61beafb33230606f01195cddc94abc69f0358e7f773a89e0cc14ba3d93f; pgv_pvid=6066919414; eas_sid=s12671z0e9R687u7g2T184P4n5; tvfe_boss_uuid=1bfb04c3e7e6e4d1; ptui_loginuin=1143552064; eas_entry=https%3A%2F%2Fwww.baidu.com%2Fother.php%3Fsc.0s0000KqFaBw-szO9hx9F5SpDQGQ8ltoYNb6hhgBzQjTjC53n8oO8hFOQvV8BJ3Z4fEPCoiUPO7U3XJWUM5DQh3YRcoHAvnfSouxKJVlPbiGm47tkNhhq7ZM4zGzpdD1GDRbN_XN__C-NXYuF6KRFlgfKwwpUCY8tboh9p_TC3rWlsNfnJrnK8RR6p-hdbZ09hjM8TIRv_W6BuIl5_vqDKZT8PTc.Db_NR2Ar5Od66kOwWtEueDf2N9h9moLers0.TLFWgv-b5Hczn1D0TLFWpyfqnWc1nfKk5fKYUHLPqIgxzPMiJsKdTvNzgLw4TARqn0K9u7qYXgK-5Hn0IvqzujLPqIgxzPMiJsKzmLmqnfKdThkxpyfqnHR1njn1nWDsnsKVINqGujYkPjfvPHDYP0KVgv-b5HDknHfkrj0L0AdYTAkxpyfqnHc1PWR0TZuxpyfqn0KGuAnqiDF70ZKGujY10APGujYYnW60mLFW5HcdPW01%26ck%3D1460.21.118.248.189.464.115.81%26dt%3D1633955793%26wd%3D%25E7%258E%258B%25E8%2580%2585%25E8%258D%25A3%25E8%2580%2580%26tpl%3Dtpl_12365_25907_22136%26l%3D1530332103%26us%3DlinkName%253D%2525E9%252580%25259A%2525E6%2525A0%25258F%2525E6%2525A0%252587%2525E5%252587%252586%2525E7%2525BB%252584%2525E4%2525BB%2525B6-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E7%25258E%25258B%2525E8%252580%252585%2525E8%25258D%2525A3%2525E8%252580%252580%2526linkType%253D; LW_sid=h1h6a37359n5B5N8Z2v7p5D109; LW_uid=u1d673u3R9z5r5E8Q2M7K5s222; pgv_info=ssid=s338616506; isHostDate=18911; PTTuserFirstTime=1633910400000; isOsSysDate=18911; PTTosSysFirstTime=1633910400000; isOsDate=18911; PTTosFirstTime=1633910400000; ts_refer=www.baidu.com/other.php; ts_uid=4700043420; weekloop=0-0-0-42; ieg_ingame_userid=uaEauBTKrEtcaq7BM1i7Oiabx0Xq2FvR; ts_last=pvp.qq.com/web201605/herodetail/155.shtml; pvpqqcomrouteLine=index_index_a20181201camp_raiders_herolist_herodetail_herodetail; PTTDate=1633955980523',
    'if-modified-since': 'Mon, 11 Oct 2021 12:30:00 GMT',
}

response = requests.get('https://pvp.qq.com/web201605/herolist.shtml', headers=headers)
etr = etree.HTML(response.text)
print('2')
all_href = etr.xpath('//div[@class="herolist-content"]/ul/li/a/@href')
print('1')
with open('all_urls.txt', mode='a+') as wa:
    for href in all_href:
        wa.write('https://pvp.qq.com/web201605/'+href)
        wa.write('\n')
