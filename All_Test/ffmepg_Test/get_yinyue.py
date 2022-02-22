# -*- encoding : utf-8 -*-
# @Author : Fenglchen
import requests
headers= {
    'Referer': 'https://www.bilibili.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
}
url = 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/75/99/301799975/301799975-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1632756941&gen=playurlv2&os=cosbv&oi=1963793854&trid=0ad60d4eab0b43288a1876a7f06d5624u&platform=pc&upsig=f385020f60b21f50a312804d2091d52b&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=639790907&bvc=vod&nettype=0&orderid=1,3&agrr=0&logo=40000000'
#url = 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/75/99/301799975/301799975-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1632756941&gen=playurlv2&os=cosbv&oi=1963793854&trid=0ad60d4eab0b43288a1876a7f06d5624u&platform=pc&upsig=f385020f60b21f50a312804d2091d52b&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=639790907&bvc=vod&nettype=0&orderid=0,3&agrr=0&logo=80000000'
#url = 'https://upos-sz-mirrorcosb.bilivideo.com/upgcxcode/33/23/159552333/159552333-1-30064.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1632756189&gen=playurlv2&os=cosbbv&oi=1963793854&trid=030b6929eef740019caba991d6f2ab97u&platform=pc&upsig=0437a2c82009fc59039c36bb5c347837&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=639790907&bvc=vod&nettype=0&orderid=2,3&agrr=0&logo=40000000'
response = requests.get(url=url,headers=headers)
with open('1.mp3', mode='wb') as w:
    w.write(response.content)
